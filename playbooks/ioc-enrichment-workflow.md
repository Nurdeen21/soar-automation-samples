# IOC Enrichment Workflow (Pseudocode)

## Purpose
Automate enrichment of indicators of compromise to accelerate threat investigation.

## Workflow Steps
1️⃣ Receive IOC (manual entry, API, or automated feed)  
2️⃣ Query threat intel sources (VirusTotal, OTX, internal DB)  
3️⃣ Aggregate and score results  
4️⃣ Update SOAR case/ticket with enrichment data  
5️⃣ Trigger further playbooks if high risk detected  

## Notes
Designed for SOAR platforms — can be integrated with SIEM alerts.
