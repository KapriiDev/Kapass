import random
import string
import customtkinter as ctk
from tkinter import messagebox

# ----- CODE -----
def update_slider_label(value):
    slider_value_label.configure(text=f"{int(float(value))} caractères")

def generate_password():
    try:
        length = int(password_length_slider.get())
        if length < 4:
            messagebox.showwarning("Attention", "La longueur doit être au moins 4.")
            return

        characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+<>?"
        password = ''.join(random.choices(characters, k=length))
        password_entry.delete(0, ctk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez choisir une longueur valide.")

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Succès", "Mot de passe copié dans le presse-papier !")
    else:
        messagebox.showwarning("Attention", "Aucun mot de passe à copier.")

# ----- APPARENCE -----
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Kapass - Générateur de mots de passe")
root.geometry("400x350")
root.resizable(False, False)


title_label = ctk.CTkLabel(root, text="Générateur de mots de passe", font=("Helvetica", 18, "bold"), text_color="white")
title_label.pack(pady=20)


length_label = ctk.CTkLabel(root, text="Choisissez la longueur :", font=("Helvetica", 14), text_color="white")
length_label.pack(pady=5)

password_length_slider = ctk.CTkSlider(root, from_=4, to=50, number_of_steps=46, width=300, command=update_slider_label)
password_length_slider.pack(pady=5)
password_length_slider.set(12)

slider_value_label = ctk.CTkLabel(root, text="12 caractères", font=("Helvetica", 12), text_color="white")
slider_value_label.pack(pady=5)

frame = ctk.CTkFrame(root)
frame.pack(pady=10)

password_entry = ctk.CTkEntry(frame, width=260, font=("Helvetica", 14), fg_color="white", text_color="black")
password_entry.grid(row=0, column=0, padx=5)

copy_button = ctk.CTkButton(
    frame, 
    width=30, 
    height=30, 
    text="📋", 
    fg_color="#05b2dc",  
    hover_color="#0392a6", 
    command=copy_to_clipboard
)
copy_button.grid(row=0, column=1, padx=5)


generate_button = ctk.CTkButton(root, text="Générer", fg_color="#05b2dc", hover_color="#0392a6", font=("Helvetica", 14), command=generate_password)
generate_button.pack(pady=10)


root.mainloop()
