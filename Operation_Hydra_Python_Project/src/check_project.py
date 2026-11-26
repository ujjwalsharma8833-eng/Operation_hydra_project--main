from pathlib import Path
from analyze import email_findings, payload_findings, trace
root = Path(__file__).resolve().parents[1]
required = ['README.md', 'docs/report.pdf', 'docs/tools.md', 'data/payload.json', 'data/transactions.csv', 'data/dns/records.json', '.github/workflows/checks.yml']
assert all((root / p).is_file() for p in required), 'Missing project deliverable'
assert len(email_findings()) == 4
assert len(trace()['transactions']) == 5
assert sum(x['amount_inr'] for x in [{'amount_inr':int(r['amount_inr'])} for r in trace()['transactions'] if r['from_account']=='victim']) == 40000
assert payload_findings()['classification'].startswith('Trojan')
print('Project structure and fixture invariants passed')
