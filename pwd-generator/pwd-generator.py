import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip

def generate_password():
    length = int(length_var.get())
    charset = string.ascii_letters + string.digits 
    
    password = ''.join(random.choice(charset) for _ in range(length))
    generated_password_label.config(text="Generiertes Passwort:\n" + password)
    pyperclip.copy(password)
    print(password)

# Tkinter-Setup
root = tk.Tk()
root.title("Passwort Generator")

# Stil definieren
style = ttk.Style()
style.theme_use("clam")

# Hauptframe für das gesamte Layout
main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Titel
title_label = ttk.Label(main_frame, text="Passwort Generator", font=("Arial", 24, "bold"), foreground="black")
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

# Formularframe
form_frame = ttk.Frame(main_frame)
form_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Passwortlänge Label und Eingabefeld
length_label = ttk.Label(form_frame, text="Passwortlänge:", font=("Arial", 12))
length_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

length_var = tk.StringVar()
length_entry = ttk.Entry(form_frame, textvariable=length_var, width=5, font=("Arial", 12))
length_entry.insert(0, "12")  # Standardlänge
length_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Button zum Generieren des Passworts
generate_button = ttk.Button(form_frame, text="Generieren", command=generate_password, style="Accent.TButton")
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Label für das generierte Passwort
generated_password_label = ttk.Label(form_frame, text="Generiertes Passwort:", font=("Arial", 12))
generated_password_label.grid(row=2, column=0, columnspan=2, pady=(20, 5))

# Flexibles Layout
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

# Stil anpassen
style.configure("Accent.TButton", background="#1DA1F2", foreground="white", padding=(5, 10), font=("Arial", 12), borderwidth=0)
style.map("Accent.TButton", background=[("active", "#6E91F6")])

# Start der Anwendung
root.mainloop()
