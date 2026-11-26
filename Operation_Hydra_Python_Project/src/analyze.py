"""Offline forensic analysis of wholly synthetic Operation Hydra evidence."""
import argparse
import csv
import hashlib
import ipaddress
import json
import re
from collections import defaultdict
from email import policy
from email.parser import BytesParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def email_findings():
    dns = json.loads((ROOT / 'data/dns/records.json').read_text())
    rows = []
    for path in sorted((ROOT / 'data/emails').glob('*.eml')):
        raw = path.read_bytes()
        msg = BytesParser(policy=policy.default).parsebytes(raw)
        sender = msg['From'].addresses[0].domain.lower()
        reply = msg['Reply-To'].addresses[0].domain.lower() if msg['Reply-To'] else ''
        received = str(msg['Received'] or '')
        ips = [s for s in re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', received) if ipaddress.ip_address(s).is_global]
        body = msg.get_body(preferencelist=('plain',))
        content = body.get_content() if body else ''
        links = re.findall(r'https?://[^\s<>]+', content)
        rows.append({'file': path.name, 'sha256': hashlib.sha256(raw).hexdigest(), 'from_domain': sender,
                     'reply_to_domain': reply, 'received_ip': ips[0] if ips else 'none (reserved fixture)',
                     'authentication_results': str(msg['Authentication-Results'] or 'unavailable'),
                     'fixture_dns': dns.get(sender, {'status':'not in offline fixture'}), 'urls': links,
                     'attachments': [p.get_filename() for p in msg.iter_attachments()]})
    return rows


def payload_findings():
    p = ROOT / 'data/payload.json'
    raw = p.read_bytes()
    obj = json.loads(raw)
    allowed = {'credential_prompt', 'fake_session_capture', 'payment_redirection', 'persistence_claim'}
    return {'sha256': hashlib.sha256(raw).hexdigest(), 'classification':'Trojan-style lure simulation',
            'behaviors': [b for b in obj['behaviors'] if b in allowed], 'iocs': obj['iocs'],
            'note':'JSON describes behavior only; nothing is executed or decoded into code.'}


def trace():
    with (ROOT/'data/transactions.csv').open(newline='') as f:
        rows = list(csv.DictReader(f))
    by_sender = defaultdict(list)
    for row in rows:
        by_sender[row['from_account']].append(row)
    paths = []
    def walk(account, chain, visited):
        edges = by_sender.get(account, [])
        if not edges:
            paths.append(chain)
            return
        for edge in edges:
            dest = edge['to_account']
            if dest in visited:
                paths.append(chain + [edge['id'] + ' (cycle)'])
            else:
                walk(dest, chain + [edge['id']], visited | {dest})
    walk('victim', [], {'victim'})
    inflow = defaultdict(int)
    outflow = defaultdict(int)
    for row in rows:
        amount = int(row['amount_inr'])
        inflow[row['to_account']] += amount
        outflow[row['from_account']] += amount
    return {'transactions': rows, 'paths_by_transaction_id': paths,
            'account_totals_inr': {a: {'incoming': inflow[a], 'outgoing': outflow[a]}
                                   for a in sorted(set(inflow)|set(outflow))},
            'caution':'Paths indicate recorded transfers, not proof of beneficial ownership; amounts can split or combine.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default=str(ROOT/'output/analysis.json'))
    args = parser.parse_args()
    result = {'case':'Operation Hydra (synthetic)', 'email_analysis':email_findings(),
              'payload_analysis':payload_findings(), 'financial_trace':trace()}
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(f'Analyzed {len(result["email_analysis"])} emails; output: {out}')
    for row in result['email_analysis']:
        print(row['file'], row['from_domain'], row['authentication_results'])
    print('Transaction paths:', result['financial_trace']['paths_by_transaction_id'])

if __name__ == '__main__':
    main()
