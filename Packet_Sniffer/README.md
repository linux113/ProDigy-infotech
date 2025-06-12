Got it! You want a **clean, properly formatted README.md** for the Packet Sniffer tool, like this:

```markdown
# 🛰️ Packet Sniffer Tool by LK

A powerful Python-based packet sniffer built with **Scapy** for educational and ethical penetration testing tasks.

---

## ⚠️ Legal & Ethical Use

> This tool is intended **only for educational and authorized use**. Do not run this on networks you do not own or have explicit permission to monitor.

---

## 🎯 Features

- Captures live packets using Scapy
- Displays:
  - Timestamp
  - Source & Destination IPs
  - Protocol (TCP/UDP/ICMP)
  - Ports
  - Raw payload (decoded)
- Powerful banner interface

---

## 📁 Project Structure

```

Packet\_Sniffer\_LK/
├── packet\_sniffer.py       # Main script
├── requirements.txt        # Dependencies
└── README.md               # Documentation

````

---

## 🛠️ Installation

```bash
git clone https://github.com/linux113/Prodigy-infotech.git
cd Prodigy-infotech/Packet_Sniffer_LK
pip install -r requirements.txt
````

---

## ▶️ Run the Sniffer

> You **must run this with root/administrator privileges**:

```bash
sudo python3 packet_sniffer.py
```

Then enter your network interface when prompted (e.g., `wlan0`, `eth0`, etc.).

---

## ✅ Tested On

* Kali Linux
* Ubuntu
* Windows (with Administrator & WinPcap/Npcap)
* Python 3.6+

---

