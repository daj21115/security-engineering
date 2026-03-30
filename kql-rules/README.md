# KQL Threat Hunting Queries

Kusto Query Language (KQL) scripts for proactive threat hunting and detection in LimaCharlie EDR and Microsoft Sentinel.

## Queries

| Query | Target TTP | Description |
|-------|------------|-------------|
| `encoded_powershell_hunt.kql` | **T1059.001** | Identifies PowerShell processes executed with Base64 encoded command flags. |

---

## Use Case: Proactive Hunting for Obfuscation

While automated alerts catch known threats, KQL allows for "Hunting" across historical telemetry to find stealthy persistence or discovery methods. This query:

- Filters for all process creation events.
- Scans the command line for common encoding flags (`-enc`, `-EncodedCommand`).
- Allows an analyst to quickly pivot from a single detection to an environment-wide investigation.

---

## Usage

```kql
// Paste into the LimaCharlie Hunting
event_type == "PROCESS_CREATION" 
| where command_line contains "-enc" or command_line contains "-EncodedCommand"
