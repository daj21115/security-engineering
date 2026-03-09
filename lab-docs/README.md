# SOC Lab Documentation

Build logs and architecture docs for a production-grade home SOC lab.

Each doc links to the corresponding Medium blog post.

## Lab Components

- **SIEM:** Wazuh
- **Endpoint:** Windows VM with Sysmon (custom config)
- **Network detection:** Suricata
- **Cloud SIEM:** Microsoft Sentinel (Azure free tier)
- **Adversary emulation:** Atomic Red Team
- **Detection pipeline:** Sigma → sigma-cli → Sentinel/Wazuh CI/CD

## Build Log

| Doc | Topic | Status |
|-----|-------|--------|
| [01-architecture.md](./01-architecture.md) | Lab design and tool selection | Coming soon |
