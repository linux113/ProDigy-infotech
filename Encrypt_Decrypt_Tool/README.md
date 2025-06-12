🔐 Encrypt_Decrypt_Tool.py
Encrypt_Decrypt_Tool.py is a Python command-line tool that combines a secret-key-based Caesar cipher with AES-GCM encryption. It provides a stylish terminal interface for secure message encryption and decryption.

✨ Features
✅ Caesar Cipher with secret-key-based alphabet shuffling

✅ AES-GCM encryption with password-based key derivation (PBKDF2)

✅ Base64 encoding/decoding for transmission-friendly output

✅ Simple interactive CLI menu

✅ Easy-to-read code for educational use## 📦 Requirements

Python 3

pycryptodome

🚀 Installation
git clone https://github.com/linux113/lk-encrypt.git
cd encrypt_decrypt_tool.py
python3 -m venv venv
source venv/bin/activate
pip install pycryptodome

🚀 How to Use
Run the tool with:

bash
python3 new.py


You'll be presented with an interactive menu:

==================================================
🛡  LK Encrypt - Hybrid Cipher Tool (Caesar + AES)
==================================================
1. Encrypt with Caesar Cipher
2. Decrypt with Caesar Cipher
3. Encrypt with AES
4. Decrypt with AES
Follow the prompts to encrypt or decrypt your message using the chosen method.



🔐 Encryption Details
Caesar Cipher
Uses a custom shuffled alphabet based on a secret key

Applies a user-defined shift for substitution

AES Encryption
AES-GCM mode (secure, authenticated encryption)

Key derived from password using PBKDF2 + salt

Encrypted output is Base64-encoded


👨‍💻 Author
linux113
🔗 GitHub: github.com/linux113

📝 License
This project is licensed under the MIT License.

❤️ Contributions
Pull requests, ideas, and improvements are welcome. Feel free to fork and contribute!

yaml
Copy
Edit

---

Let me know if you'd like me to include:
- A screenshot of the terminal tool (ASCII UI)
- A sample `.gif` or video demo
- Auto-installation shell script for new users

I can generate those too.
