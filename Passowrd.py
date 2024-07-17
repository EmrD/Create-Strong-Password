import random
import tkinter as tk

def generate_password():
    copy_button.config(state=tk.ACTIVE, text="Copy")
    password_len = int(entry.get())
    password = ""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"

    for _ in range(password_len):
        password_char = random.choice(chars)
        password += password_char

    password_label.config(text=password)
    adjust_window_width()

def copy_password():
    window.clipboard_clear()
    window.clipboard_append(password_label.cget("text"))
    copy_button.config(state=tk.DISABLED, text="Copied")

def adjust_window_width():
    password_len = len(password_label.cget("text"))
    if 10 <= password_len <= 15:
        window_width = 400
    elif 16 <= password_len <= 20:
        window_width = 500
    elif password_len > 20:
        window_width = 900
    else:
        window_width = 400
    window.geometry(f"{window_width}x170")

window = tk.Tk()
window.title("")
window.geometry("400x170")
window.resizable(width=False, height=False)

Chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"

password_frame = tk.Frame(window)
password_frame.pack(pady=10)

label12 = tk.Label(password_frame, text="The password is:", font="20")
label12.pack(side=tk.LEFT)

password_label = tk.Label(password_frame, text="", font="Verdana 14")
password_label.pack(side=tk.LEFT)

length_frame = tk.Frame(window)
length_frame.pack()

length_label = tk.Label(length_frame, text="Password Length:", font="Verdana 12")
length_label.pack(side=tk.LEFT)

entry = tk.Entry(length_frame, font="Verdana 12", width=10, justify="center")
entry.pack(side=tk.LEFT)

generate_button = tk.Button(window, text="Generate", font="Verdana 12", command=generate_password)
generate_button.pack()

copy_button = tk.Button(window, text="Copy", font="Verdana 12", command=copy_password, state=tk.DISABLED)
copy_button.pack(pady=5)

window.mainloop()
