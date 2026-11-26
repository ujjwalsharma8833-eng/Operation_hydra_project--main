# Operation Hydra

A complete offline Python case study for Assignment 2, Unit 2, Types of Cyber Crimes. It reconstructs a fictional phishing, spoofing, Trojan-style lure and payment fraud sequence. Every person, domain, IP and transaction is synthetic. No sample collects credentials, contacts a network, or executes malware.

## Run

Requires Python 3.11 or later. No Python packages are needed.

```bash
python src/analyze.py
python src/check_project.py
```

Read `output/analysis.json` for hashes, email indicators and payment paths. The source evidence is in `data/`, the legal and impact report is `docs/report.pdf`, and tool commands are in `docs/tools.md`.

## Evidence workflow

1. Inspect the four original `.eml` fixtures and their SHA-256 values.
2. Compare From, Reply-To and Authentication-Results; the DNS file is a declared mock record set.
3. Read the inert JSON payload description and classify the claimed behavior.
4. Follow transaction IDs T01–T05 through the two branches. The victim loses a simulated INR 40,000; each branch represents a transfer path, not verified ownership.
5. Consult the report's crime mapping, impact, legal caveats and primary references.

## Limitations

The public documentation IP ranges and `.example` domains cannot be traced to a real actor. Authentication-Results can be forged in untrusted headers, and this project does not perform cryptographic DKIM validation. The purported bank message with pass results illustrates that authentication alone does not establish benign intent. There are no screenshots of live tool results; `output/analysis.json` is the reproducible analysis log. Cite these boundaries in any presentation.

## Authorship declaration

This repository contains an original synthetic educational scenario and reproducible Python analysis. The submitting student should add their own name and institution here after reviewing the code, report, results and citations; they should not claim live investigation or original malware acquisition.
