import tkinter as tk
from tkinter import messagebox
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_login"
)

cursor = db.cursor()

def login():
    user = entry_user.get()
    pw = entry_pass.get()

    cursor.execute(
        "SELECT * FROM user WHERE username=%s AND password=%s",
        (user, pw)
    )

    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Login Berhasil", "Login sukses!")
        halaman_index(user)
    else:
        messagebox.showerror("Login Gagal", "Username atau password salah")

def logout(window):
    jawab = messagebox.askyesno("Logout", "Apakah Anda yakin ingin logout?")
    if jawab:
        window.destroy()
        root.deiconify()

def halaman_index(username):
    root.withdraw()

    index = tk.Toplevel()
    index.title("Halaman Index")
    index.geometry("300x200")

    lbl = tk.Label(index, text=f"Selamat Datang, {username}", font=("Arial", 12))
    lbl.pack(pady=20)

    btn_logout = tk.Button(index, text="Logout", command=lambda: logout(index))
    btn_logout.pack()

root = tk.Tk()
root.title("Login")
root.geometry("300x200")

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()