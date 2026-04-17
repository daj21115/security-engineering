# ARP Spoof Detector

Detects ARP spoofing attacks on a local network by monitoring ARP traffic for MAC/IP inconsistencies.

## What It Does

- Captures ARP traffic on the local network interface
- Builds a table of IP → MAC mappings
- Alerts when an IP address is seen with a different MAC than previously recorded
- Logs suspicious activity with timestamps

## Use Case

ARP spoofing is a common man-in-the-middle attack vector. This tool provides passive detection
on a network segment useful in a SOC lab or on a monitored subnet.

## Tools / Libraries

- Python 3
- Scapy (packet capture + ARP parsing)

## Status

In development.
