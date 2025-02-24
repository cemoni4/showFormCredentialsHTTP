# HTTP Packet Monitor & Form Sniffer 🛡️

## Description 📘
This project is a Python script that captures and analyzes HTTP traffic, detects GZIP-compressed content, and extracts form data (like usernames and passwords) sent through POST requests. It uses `netfilterqueue` and `scapy` for packet manipulation.

## Features ⚡
- **HTTP Packet Interception**: Captures HTTP packets on port 80.
- **GZIP Decompression**: Detects and decompresses GZIP-encoded responses.
- **Form Data Extraction**: Parses POST requests to extract form credentials.
- **Real-Time Monitoring**: Displays packet and form data in real time.

## Requirements 🛠️
- Python 3
- Libraries:
  - `netfilterqueue`
  - `scapy`

Install the required libraries with:
```bash
pip install netfilterqueue scapy
```

## Firewall Configuration 🔥
To make the script work, you need to set up an iptables rule to forward traffic to the Netfilter queue:
```bash
iptables -I FORWARD -j NFQUEUE --queue-num 1
```

For local testing:
```bash
iptables -I OUTPUT -j NFQUEUE --queue-num 1
iptables -I INPUT -j NFQUEUE --queue-num 1
```

After running the script, reset the rules with:
```bash
iptables --flush
```

## Execution ▶️
Run the script with:
```bash
sudo python3 http_sniffer.py
```

## Warning ⚠️
Running this script requires superuser privileges and modifies firewall rules. HTTP transmits data in plaintext, so this tool highlights how attackers might intercept sensitive information. Use responsibly and only in controlled environments for educational or testing purposes!

## License 📄
Distributed under the MIT License.

---
