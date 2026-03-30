# PowerShell Scripts

Automation scripts for SOC and detection engineering workflows.

## Scripts

| Script | Description |
|--------|-------------|
| `update-ossec-config.ps1` | Programmatically updates `ossec.conf` using PowerShell XML parsing to add Sysmon log ingestion, bypassing permission issues and enabling repeatable configuration changes. |

---

## Use Case: Programmatic Configuration Update

This script automates updates to the Wazuh/OSSEC agent configuration file (`ossec.conf`) by:

- Parsing the file as XML
- Appending a `<localfile>` entry for Sysmon logs
- Saving changes safely without manual editing

---

## Usage

```powershell
# Run PowerShell as Administrator
.\update-ossec-config.ps1
