# SOAR Automation Samples

## 📌 Overview
This repository contains examples of SOAR playbooks, scripts, and tool-specific automation snippets designed to accelerate incident response and improve security operations efficiency.

## ⚡ Purpose
Showcase real-world automation patterns and helper scripts for:
- Phishing triage
- IOC enrichment
- Cloud incident remediation
- Notifications and integrations

## 📁 Contents

### 📝 Playbooks
- `playbooks/phishing-triage-pseudocode.md` — Pseudocode for automating phishing triage.
- `playbooks/ioc-enrichment-workflow.md` — Workflow for automated IOC enrichment.
- `playbooks/cloud-remediation-pseudocode.md` — Pseudocode for cloud security incident auto-remediation.

### 🛠 Common Scripts
- `scripts/extract-iocs.py` — Extracts indicators (URLs, IPs) from text for automation workflows.
- `scripts/enrich-url.py` — Stub script for querying URL reputation APIs (e.g., VirusTotal).
- `scripts/slack-notify.py` — Sends Slack alerts from automated workflows.

### 🔧 Tool-Specific Examples

#### XSOAR
- `xsoar/phishing-extract-indicators.yml` — Extract indicators from emails using XSOAR automation.

#### Splunk SOAR
- `scripts/splunk-soar/enrich-ip.json` — Playbook node for enriching IPs with threat intel queries.

#### Microsoft Sentinel
- `sentinel/isolate-vm-logicapp.json` — Logic App JSON for isolating VMs upon critical alert detection.

---

## 🚀 Status
🚧 In progress — More playbooks, code samples, and diagrams coming soon!
