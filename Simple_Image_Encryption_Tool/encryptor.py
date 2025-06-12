from PIL import Image

def banner():
    print("\n=============================")
    print("🔐 LK Image Encryptor Tool")
    print("Internship Project - ProDigy Infotech")
    print("=============================\n")

def encrypt_image(input_path, output_path):
    banner()
    img = Image.open(input_path)
    pixels = img.load()
    
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (255 - r, 255 - g, 255 - b)
    
    img.save(output_path)
    print(f"[+] Encrypted image saved to: {output_path}")
    return output_path

def decrypt_image(input_path, output_path):
    banner()
    return encrypt_image(input_path, output_path)
