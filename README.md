# security-engineering

Detection rules, automation scripts, and security engineering projects.

Built by a cybersecurity analyst targeting Detection Engineering roles.  
Tools: Microsoft Sentinel · CrowdStrike · KQL · Wazuh · MITRE ATT&CK · Sigma · YARA · Snort

---

## Repository Structure

| Folder | Contents |
|--------|----------|
| [`/sigma-rules`](./sigma-rules/) | Platform-agnostic detection rules (Sigma format) |
| [`/yara-rules`](./yara-rules/) | File-based malware detection rules |
| [`/snort-rules`](./snort-rules/) | Network-based detection rules |
| [`/kql-rules`](./kql-rules/) | EDR/SIEM detection rules and hunting queries (LimaCharlie/Sentinel)
| [`/scripts/powershell`](./scripts/powershell/) | PowerShell automation scripts for SOC/detection workflows |
| [`/scripts/python`](./scripts/python/) | Python tools for log parsing, IOC lookup, triage automation |
| [`/projects`](./projects/) | Standalone security engineering projects |
| [`/lab-docs`](./lab-docs/) | SOC lab build documentation (linked to Medium blog series) |

---

## Projects

### ARP Spoof Detector
Detects ARP spoofing attacks on a local network by monitoring ARP traffic for inconsistencies.  
→ [`/projects/arp-spoof-detector`](./projects/arp-spoof-detector/)

---

## SOC Lab Build — Medium Blog Series

Documenting the full build of a production-grade SOC lab from scratch.

| Post | Topic | Status |
|------|-------|--------|
| 01 | Architecture overview + tool selection | Coming soon |
| 02 | Wazuh SIEM setup and first detections | Coming soon |
| 03 | Windows endpoint with Sysmon | Coming soon |
| 04 | Network detection with Suricata | Coming soon |
| 05 | Connecting to Microsoft Sentinel + KQL hunts | Coming soon |
| 06 | Atomic Red Team: emulate, detect, tune | Coming soon |
| 07 | Full CI/CD pipeline for detection rules | Coming soon |

---

## Connect

- Medium: *(coming soon)*
- LinkedIn: *(coming soon)*
