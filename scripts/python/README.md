# Python Scripts

Python tools for SSH automation, log parsing, and security orchestration.

## Scripts

| Script | Description |
|--------|-------------|
| `deploy_rule.py` | Automates the deployment of Sigma rules to a remote Wazuh Manager via SSH/SFTP using the **Paramiko** library. |

---

## Use Case: Automated Rule Deployment (CI/CD)

This script bridges the gap between the development environment (VS Code) and the SIEM infrastructure by:

- Establishing a secure SSH tunnel to the Wazuh Manager.
- Programmatically transferring YAML-based Sigma rules to the correct directory (`/var/ossec/etc/rules/`).
- Redacting sensitive credentials to ensure Git/GitHub security compliance.

---

## Usage

```bash
# Ensure you are in the virtual environment
source .venv/bin/activate

# Execute the deployment
python3 deploy_rule.py
