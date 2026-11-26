# Tools and commands

| Tool | Command | Why |
| --- | --- | --- |
| Python 3.11 standard library | `python src/analyze.py` | Parse email headers, hash samples and trace a transaction graph offline. |
| Python structure check | `python src/check_project.py` | Validate fixture count, required deliverables and starting amount. |
| Markdownlint CLI | `npx --yes markdownlint-cli@0.45.0 README.md docs/*.md` | Check repository Markdown formatting in CI. |
| SHA-256 | Produced by `python src/analyze.py` | Identify precise evidence bytes for reproducibility. |

SPF, DKIM and DMARC values in `data/dns/records.json` and email headers are **simulated assertions**, not live verification. WHOIS is intentionally unavailable for reserved `.example` domains. A real investigation would preserve originals, query authorized DNS/registration sources, and record access time and provenance. No VirusTotal or AbuseIPDB submission was made; the fixtures are not real internet indicators.
