import tkinter as tk
from tkinter import filedialog, messagebox
from encryptor import encrypt_image, decrypt_image

def select_file():
    file_path.set(filedialog.askopenfilename())

def encrypt_action():
    if not file_path.get():
        messagebox.showwarning("Warning", "Select an image file first.")
        return
    out = filedialog.asksaveasfilename(defaultextension=".png")
    encrypt_image(file_path.get(), out)
    messagebox.showinfo("Done", "Image encrypted and saved.")

def decrypt_action():
    if not file_path.get():
        messagebox.showwarning("Warning", "Select an image file first.")
        return
    out = filedialog.asksaveasfilename(defaultextension=".png")
    decrypt_image(file_path.get(), out)
    messagebox.showinfo("Done", "Image decrypted and saved.")

app = tk.Tk()
app.title("LK Image Encryptor")
app.geometry("420x250")
app.resizable(False, False)

file_path = tk.StringVar()

# ====== LK BANNER ======
tk.Label(app, text="🔐 LK Image Encryptor", font=("Helvetica", 16, "bold"), fg="blue").pack(pady=10)

tk.Label(app, text="Image Path:").pack(pady=5)
tk.Entry(app, textvariable=file_path, width=50).pack(pady=5)
tk.Button(app, text="Browse", command=select_file).pack(pady=5)
tk.Button(app, text="Encrypt", width=20, command=encrypt_action).pack(pady=5)
tk.Button(app, text="Decrypt", width=20, command=decrypt_action).pack(pady=5)

tk.Label(app, text="© LK - ProDigy Infotech Internship Project", font=("Arial", 8)).pack(pady=10)

app.mainloop()
