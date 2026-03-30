# Sigma Rules

Platform-agnostic detection rules written in Sigma format for cross-platform SIEM visibility.

## Rules

| Rule | ATT&CK Technique | Description |
|------|------------------|-------------|
| `win_encoded_ps.yml` | **T1059.001** | Detects obfuscated PowerShell execution by monitoring **ScriptBlock Logging (Event ID 4104)** for encoded command flags. |

---

## Use Case: De-obfuscated Command Detection

Standard command-line logging often misses the "inner" payload of an encoded command. This rule focuses on the **PowerShell Operational** log channel to:

- Trigger on `-EncodedCommand`, `-enc`, and `-e` flags.
- Target the `scriptBlockText` field to capture the script content after Windows has de-obfuscated it.
- Provide high-fidelity alerts (Level 15) for potential "Ingress Tool Transfer" (T1105) behavior.

---

## Usage

```bash
# Convert to Wazuh/Elastic format using sigma-cli
sigma convert -t es-qs -p windows_powershell win_encoded_ps.yml
