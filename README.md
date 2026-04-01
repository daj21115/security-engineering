# Security Engineering Repo

Detection rules, automation scripts, and security engineering projects demonstrating practical skills in detection engineering and SOC workflows.

## Repository Structure

| Folder | Contents |
|--------|----------|
| [`/sigma-rules`](./sigma-rules/) | Platform-agnostic detection rules (Sigma format) |
| [`/kql-rules`](./kql-rules/) | EDR/SIEM detection rules and hunting queries (LimaCharlie / Microsoft Sentinel) |
| [`/detections/lima-charlie`](./detections/lima-charlie/) | Detection rules and alerts specific to LimaCharlie EDR |
| [`/scripts/powershell`](./scripts/powershell/) | PowerShell automation scripts for SOC/detection workflows |
| [`/scripts/python`](./scripts/python/) | Python tools for log parsing, IOC lookup, and triage automation |
| [`/projects`](./projects/) | Standalone security engineering projects |

## Highlights
- Hands-on experience with SIEM, EDR, detection rules, threat hunting, and automation  
- Practical use of Microsoft Sentinel, CrowdStrike, Wazuh, Sigma, YARA, Snort, LimaCharlie EDR, and Python  

## Projects

### ARP Spoof Detector
Detects ARP spoofing attacks on a local network by monitoring ARP traffic for inconsistencies.  
→ [`/projects/arp-spoof-detector`](./projects/arp-spoof-detector/)
