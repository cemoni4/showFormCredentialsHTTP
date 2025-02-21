# showFormCredentialsHTTP
# Packet Sniffer for GZIP Decompression and Form Data Extraction 🐍🔍

This Python script is designed to monitor and analyze network traffic, specifically focusing on GZIP compression in HTTP responses and extracting form data (username and password) from HTTP POST requests.

## Features ✨

- **GZIP Decompression**: Automatically detects and decompresses GZIP-encoded data in HTTP responses.
- **Form Data Extraction**: Captures form data (such as usernames and passwords) from HTTP POST requests.
- **Packet Sniffing**: Uses Scapy and NetfilterQueue to monitor packets in real-time.

## Requirements ⚙️

Before running the script, ensure you have the following Python packages installed:

- `scapy`
- `netfilterqueue`
- `zlib`
- `urllib.parse`

You can install the required packages using `pip`:

CODICE
pip install scapy netfilterqueue
CODICE

> ⚠️ **Note**: The script requires **root privileges** to capture network traffic.

## How It Works 🛠️

1. **GZIP Detection**: The script scans HTTP packets for the `Content-Encoding: gzip` header. When it detects this header, it decompresses the corresponding GZIP-encoded data.
2. **Form Data Extraction**: When a POST request is detected, the script attempts to extract form data (specifically `username` and `password`) from the HTTP body.
3. **Packet Monitoring**: The script uses NetfilterQueue to capture and inspect network packets in real-time.

## Usage 🚀

1. Make sure you have **root privileges**, as this script needs to capture packets on the network.
2. Run the script:

CODICE
sudo python3 packet_sniffer.py
CODICE

3. The script will start monitoring packets and will display:

   - Detected **GZIP-encoded data** in HTTP responses.
   - Extracted **form data (username and password)** from HTTP POST requests.

4. Press `Ctrl+C` to stop the script.

## Example Output 📊

- **GZIP Detected**: The script will print a message when it detects GZIP-encoded data.

    CODICE
    Dati GZIP rilevati nella risposta.
    CODICE

- **Form Data Extracted**: If form data is successfully extracted, it will display the username and password.

    CODICE
    Form trovato: Username:  ['user123']  Password:  ['password456']
    CODICE

## License 📜

This project is licensed under the MIT License.
