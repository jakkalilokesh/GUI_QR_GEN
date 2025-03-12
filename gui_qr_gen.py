import pyqrcode
import os
import tkinter as tk
from tkinter import messagebox

def generate_qr():
    data = data_entry.get()
    file_name = file_name_entry.get().strip() or "qr_code.png"

    if not data:
        messagebox.showwarning("Input Error", "Please enter data or URL to generate QR Code.")
        return

    try:
        qr = pyqrcode.create(data)
        qr.png(file_name, scale=5)

        if os.path.exists(file_name):
            messagebox.showinfo("Success", f"QR Code saved successfully as '{file_name}'!")
        else:
            messagebox.showerror("Error", "Failed to save QR Code. Please try again.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Setting up the GUI window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x250")
root.resizable(0, 0)

# Labels
tk.Label(root, text="QR Code Generator", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter Data or URL:", font=("Arial", 10)).pack(anchor="w", padx=10)
data_entry = tk.Entry(root, width=50)
data_entry.pack(pady=5)

tk.Label(root, text="File Name (Optional):", font=("Arial", 10)).pack(anchor="w", padx=10)
file_name_entry = tk.Entry(root, width=50)
file_name_entry.pack(pady=5)

# Generate Button
generate_button = tk.Button(root, text="Generate QR Code", font=("Arial", 12, "bold"), command=generate_qr)
generate_button.pack(pady=20)

# Run the application
root.mainloop()
