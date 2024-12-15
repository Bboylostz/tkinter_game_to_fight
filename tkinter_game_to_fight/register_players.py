from tkinter import ttk, messagebox
from tkinter import *
from tkinter import messagebox
import hashlib
import sqlite3




def register_players():

    window = Tk()
    window.title("окно регистрации")
    window.geometry("250x300")
    Label(window, text="Регистрация").pack(pady=10)

    username_label = Label(window, text="Имя пользователя:")
    username_entry = Entry(window)
    username_label.pack()
    username_entry.pack()

    email_label = Label(window, text="Email:")
    email_entry = Entry(window)
    email_label.pack()
    email_entry.pack()

    password_label = Label(window, text="Пароль:")
    password_entry = Entry(window, show="*")
    password_label.pack()
    password_entry.pack()

    confirm_password_label = Label(window, text="Подтвердите пароль:")
    confirm_password_entry = Entry(window, show="*")
    confirm_password_label.pack()
    confirm_password_entry.pack()

    register_button = Button(window, text="Зарегистрироваться",
                             command=lambda: register_user(window, username_entry, email_entry, password_entry,
                                                           confirm_password_entry))
    register_button.pack(pady=10)

    return window


def register_user(window, username_entry, email_entry, password_entry, confirm_password_entry):
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if password != confirm_password:
        messagebox.showerror("Ошибка", "Пароли не совпадают!")
        return

    if not username or not email or not password:
        messagebox.showerror("Ошибка", "Заполните все поля!")
        return

    conn, cursor = connect_to_db()

    try:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        cursor.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
                       (username, email, hashed_password))
        conn.commit()
        messagebox.showinfo("Успех", "Регистрация успешна!")
        window.destroy()
    except sqlite3.IntegrityError:
        messagebox.showerror("Ошибка", "Пользователь с таким именем или email уже существует!")
    finally:
        conn.close()


def connect_to_db():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, email TEXT UNIQUE, password_hash TEXT)''')
    return conn, cursor
