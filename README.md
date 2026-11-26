# 🛡️ Operation Hydra
### Digital Forensics | Cybercrime Investigation | Phishing & Financial Fraud Analysis

**Operation Hydra** is a Python-based digital forensic investigation project developed as an educational case study on cybercrimes. It demonstrates how phishing emails, email spoofing, Trojan-style lures, and fraudulent financial transactions can be examined using structured digital evidence analysis.

The project reconstructs a fictional cybercrime scenario and applies forensic techniques to identify suspicious email indicators, analyze authentication information, calculate file hashes, and trace simulated financial transactions.

> **Disclaimer:** This project uses entirely synthetic evidence, fictional domains, and simulated transactions. It does not contain functional malware, collect credentials, or interact with real financial systems.

---

## 🎯 Project Objectives

- Understand different types of cybercrimes through a practical case study.
- Examine suspicious email headers and sender information.
- Identify inconsistencies between From and Reply-To addresses.
- Analyze SPF, DKIM, and DMARC authentication assertions.
- Generate SHA-256 hashes for digital evidence integrity.
- Examine Trojan-style behavior descriptions without executing malicious files.
- Trace simulated financial transactions and identify possible money-flow paths.
- Generate structured forensic analysis reports using Python.

## 🔍 Investigation Modules

### 1. Email Forensic Analysis
Examines four synthetic email samples to identify:
- Sender and Reply-To domains.
- Email authentication results.
- Suspicious URLs.
- Attachment information.
- SHA-256 evidence hashes.
- Available synthetic DNS records.

### 2. Email Spoofing Analysis
Examines simulated SPF, DKIM, and DMARC results to understand email authentication failures and inconsistencies.

### 3. Trojan-Style Lure Analysis
Analyzes an inert JSON description containing simulated behaviors such as:
- Credential prompts.
- Fake session capture.
- Payment redirection.
- Indicators of compromise (IOCs).

No executable malware is included or executed.

### 4. Financial Transaction Tracing
Reconstructs a simulated financial fraud transaction flow.

**Initial simulated amount: ₹40,000**

The transaction is divided into two branches:
- Branch 1: ₹25,000
- Branch 2: ₹15,000

The analysis follows five transaction records to demonstrate how funds move between intermediary accounts and simulated endpoints.

### 5. Evidence Integrity
Uses SHA-256 hashing to calculate digital fingerprints of the email samples and payload metadata for reproducibility and evidence identification.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.11 | Core programming language |
| Email Parser | Email header analysis |
| hashlib | SHA-256 hashing |
| JSON | Evidence and IOC processing |
| CSV | Transaction analysis |
| ipaddress | IP address validation |
| Git & GitHub | Version control |
| GitHub Actions | Automated project checks |

**Dependencies:** Python Standard Library. No additional Python packages are required.

---

## 📂 Project Structure

```text
Operation_Hydra_Python_Project/
│
├── .github/
│   └── workflows/
│       └── checks.yml
│
├── data/
│   ├── dns/
│   │   └── records.json
│   ├── emails/
│   │   ├── 01_kyc.eml
│   │   ├── 02_invoice.eml
│   │   ├── 03_otp.eml
│   │   └── 04_followup.eml
│   ├── payload.json
│   └── transactions.csv
│
├── docs/
│   ├── report.pdf
│   └── tools.md
│
├── output/
│   └── analysis.json
│
├── src/
│   ├── analyze.py
│   └── check_project.py
│
└── README.md
```

---

## ⚙️ Installation & Execution

### Step 1: Clone the repository

```bash
git clone https://github.com/Kartik311209/Operation_hydra_project-.git
```

### Step 2: Navigate to the project directory

```bash
cd Operation_hydra_project-/Operation_Hydra_Python_Project
```

### Step 3: Run the forensic analysis

```bash
python src/analyze.py
```

### Step 4: Validate the project

```bash
python src/check_project.py
```

### Step 5: View the generated results

```text
output/analysis.json
```

The generated JSON contains email analysis, SHA-256 hashes, payload classification, and simulated financial transaction paths.

---

## 📊 Expected Investigation Outcomes

| Investigation | Expected Output |
|---|---|
| Email Analysis | 4 analyzed email samples |
| Email Authentication | SPF, DKIM and DMARC assertions |
| Evidence Integrity | SHA-256 hashes |
| Payload Analysis | Trojan-style lure classification |
| Financial Analysis | 5 transaction records |
| Money Flow | 2 simulated transaction branches |
| Financial Amount | ₹40,000 simulated initial transfer |

---

## 🔐 Digital Forensics & Evidence Limitations

This project is designed for educational and academic purposes.

- All email messages and financial records are synthetic.
- The `.example` domains are fictional.
- DNS authentication information represents simulated evidence, not live verification.
- Email authentication headers are not independently cryptographically verified.
- Transaction paths do not establish actual ownership or identify real suspects.
- No live WHOIS, VirusTotal, or AbuseIPDB investigation has been performed.
- No real malware has been acquired or executed.

The results should therefore be interpreted as a simulated forensic reconstruction rather than a real-world cybercrime investigation.

---

## 📚 Documentation

The repository includes:
- `docs/report.pdf` – Project investigation report.
- `docs/tools.md` – Tools, commands, and forensic workflow.
- `output/analysis.json` – Machine-generated analysis results.

---

## 🎓 Academic Purpose

This project demonstrates the application of digital forensic concepts, cybercrime investigation techniques, email security analysis, evidence integrity, and financial transaction reconstruction.

It provides a structured practical understanding of how digital evidence can be examined and documented during a simulated cybercrime investigation.

---

## 👨‍💻 Author

**Kartik Kumar**

GitHub: [@Kartik311209](https://github.com/Kartik311209)

Project: [Operation Hydra](https://github.com/Kartik311209/Operation_hydra_project-)

---

### ⭐ Support

If you find this project useful for learning about cybercrime investigation and digital forensics, consider giving the repository a star!

**Operation Hydra — Reconstructing Digital Evidence, One Trace at a Time.**
