#!/usr/bin/env python3

import base64
import random
import string
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

# --- Caesar Cipher Functions ---

def generate_keyed_alphabet(secret_key):
    seed = sum(ord(c) for c in secret_key)
    random.seed(seed)
    alphabet = list(string.ascii_letters + string.digits + string.punctuation + " ")
    random.shuffle(alphabet)
    return ''.join(alphabet)

def caesar_with_key(text, shift, secret_key, mode='encrypt'):
    custom_alphabet = generate_keyed_alphabet(secret_key)
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char in custom_alphabet:
            idx = custom_alphabet.index(char)
            new_idx = (idx + shift) % len(custom_alphabet)
            result += custom_alphabet[new_idx]
        else:
            result += char
    return result

def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def base64_decode(text):
    return base64.b64decode(text.encode()).decode()

# --- AES Functions ---

SALT_SIZE = 16
KEY_SIZE = 32
ITERATIONS = 100_000

def derive_key(password, salt):
    return PBKDF2(password, salt, dkLen=KEY_SIZE, count=ITERATIONS)

def aes_encrypt(plaintext, password):
    salt = get_random_bytes(SALT_SIZE)
    key = derive_key(password, salt)
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())
    encrypted_data = salt + cipher.nonce + tag + ciphertext
    return base64.b64encode(encrypted_data).decode()

def aes_decrypt(encrypted_b64, password):
    try:
        encrypted_data = base64.b64decode(encrypted_b64)
        salt = encrypted_data[:SALT_SIZE]
        nonce = encrypted_data[SALT_SIZE:SALT_SIZE+16]
        tag = encrypted_data[SALT_SIZE+16:SALT_SIZE+32]
        ciphertext = encrypted_data[SALT_SIZE+32:]
        key = derive_key(password, salt)
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        return plaintext.decode()
    except Exception as e:
        return f"❌ Decryption failed: {str(e)}"

# --- Main Menu with Stylish Output ---

def main():
    # ANSI color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

    banner = f"""{RED}{BOLD}
██╗     ██╗  ██╗    ███████╗███╗   ██╗ ██████╗ ██████╗ ███████╗ ██████╗████████╗
██║     ██║  ██║    ██╔════╝████╗  ██║██╔════╝██╔═══██╗██╔════╝██╔════╝╚══██╔══╝
██║     ███████║    █████╗  ██╔██╗ ██║██║     ██║   ██║█████╗  ██║        ██║   
██║     ██╔══██║    ██╔══╝  ██║╚██╗██║██║     ██║   ██║██╔══╝  ██║        ██║   
███████╗██║  ██║    ███████╗██║ ╚████║╚██████╗╚██████╔╝███████╗╚██████╗   ██║   
╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝   ╚═╝   
                         {CYAN}🛡  LK Encrypt - Hybrid Cipher Tool{RED}
{RESET}"""

    print(banner)
    print(f"{BOLD}🔐 Choose an option:{RESET}")
    print(f"{GREEN}1.{RESET} Encrypt with Caesar Cipher")
    print(f"{GREEN}2.{RESET} Decrypt with Caesar Cipher")
    print(f"{GREEN}3.{RESET} Encrypt with AES")
    print(f"{GREEN}4.{RESET} Decrypt with AES\n")

    choice = input(f"{CYAN}Choose an option (1-4): {RESET}").strip()

    if choice == '1':
        text = input("Enter your message: ")
        secret_key = input("Enter your secret key (used to shuffle alphabet): ")
        try:
            shift = int(input("Enter shift value (e.g., 3): "))
        except ValueError:
            print("❌ Shift must be an integer.")
            return
        encrypted = caesar_with_key(text, shift, secret_key, mode='encrypt')
        encoded = base64_encode(encrypted)
        print(f"{GREEN}🔒 Final Encrypted Output (Base64):{RESET} {encoded}")

    elif choice == '2':
        text = input("Enter Base64 encrypted message: ")
        secret_key = input("Enter your secret key (used to shuffle alphabet): ")
        try:
            shift = int(input("Enter shift value (e.g., 3): "))
        except ValueError:
            print("❌ Shift must be an integer.")
            return
        try:
            decoded = base64_decode(text)
        except Exception:
            print("❌ Base64 decode failed. Message may be corrupted.")
            return
        decrypted = caesar_with_key(decoded, shift, secret_key, mode='decrypt')
        print(f"{GREEN}🔓 Decrypted Message:{RESET} {decrypted}")

    elif choice == '3':
        text = input("Enter your message: ")
        password = input("Enter password for AES encryption: ")
        encrypted = aes_encrypt(text, password)
        print(f"{GREEN}🔐 AES Encrypted Output (Base64):{RESET} {encrypted}")

    elif choice == '4':
        encrypted = input("Enter AES encrypted Base64 message: ")
        password = input("Enter password for AES decryption: ")
        decrypted = aes_decrypt(encrypted, password)
        print(f"{GREEN}🔓 AES Decrypted Output:{RESET} {decrypted}")

    else:
        print("❌ Invalid option.")

if __name__ == "__main__":
    main()
