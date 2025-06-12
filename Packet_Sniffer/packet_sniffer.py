from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
import datetime

def print_banner():
    banner = r"""
 ____            _        _    _____       _  __         
|  _ \ __ _  ___| | _____| |_ | ____|_ __ (_)/ _| ___    
| |_) / _` |/ __| |/ / _ \ __||  _| | '_ \| | |_ / _ \   
|  __/ (_| | (__|   <  __/ |_ | |___| | | | |  _| (_) |  
|_|   \__,_|\___|_|\_\___|\__||_____|_| |_|_|_|  \___/   

          🛰️ Network Packet Sniffer
           👨‍💻 Developed by: LK
---------------------------------------------------------
> Educational Use Only | Run with proper permissions
> Capturing live packets on your network interface
---------------------------------------------------------
"""
    print(banner)

def analyze_packet(packet):
    print("="*60)
    print(f"📦 Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if IP in packet:
        ip_layer = packet[IP]
        print(f"🔹 Source IP      : {ip_layer.src}")
        print(f"🔸 Destination IP : {ip_layer.dst}")
        print(f"📡 Protocol       : {ip_layer.proto}")
    
    if TCP in packet:
        print("🧱 TCP Segment")
        print(f"    - Src Port: {packet[TCP].sport}  →  Dst Port: {packet[TCP].dport}")
    
    elif UDP in packet:
        print("🔧 UDP Datagram")
        print(f"    - Src Port: {packet[UDP].sport}  →  Dst Port: {packet[UDP].dport}")
    
    elif ICMP in packet:
        print("📢 ICMP Packet")

    if Raw in packet:
        payload = packet[Raw].load
        print("📄 Payload (raw):")
        try:
            print(payload.decode('utf-8', errors='ignore'))
        except:
            print("    [Binary or non-printable data]")

def main():
    print_banner()
    iface = input("🛠️ Enter interface to sniff (e.g., eth0, wlan0): ")
    print(f"🔍 Sniffing on interface: {iface}... Press Ctrl+C to stop.")
    sniff(iface=iface, prn=analyze_packet, store=False)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Sniffing stopped by user.")
