import hashlib
from tkinter import *
from tkinter import ttk, messagebox

from register_players import connect_to_db


def enter_to_game():

    window = Tk()
    window.title("игровое меню")
    window.geometry("250x200")
    Label(window, text="Вход в систему").pack(pady=10)

    username_label = Label(window, text="Имя пользователя:")
    username_entry = Entry(window)
    username_label.pack()
    username_entry.pack()

    password_label = Label(window, text="Пароль:")
    password_entry = Entry(window, show="*")
    password_label.pack()
    password_entry.pack()

    email_label = Label(window, text="Email:")
    email_entry = Entry(window)
    email_label.pack()
    email_entry.pack()


    login_button = Button(window, text="Войти",
                          command=lambda: check_credentials(window, username_entry, password_entry, email_entry))
    login_button.pack(pady=10)

    return window


def check_credentials(root, username_entry, password_entry, email_entry):
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()

    conn, cursor = connect_to_db()

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute("SELECT * FROM users WHERE username = ? AND email = ?", (username, email))
    user = cursor.fetchone()

    if user:
        stored_hash = user[3]  # Индекс 3 соответствует столбцу password_hash
        if hashed_password == stored_hash:
            messagebox.showinfo("Успех", "Вход успешен!")
            root.destroy()
            # Здесь можно добавить код для перехода к основному интерфейсу приложения
        else:
            messagebox.showerror("Ошибка", "Неверный пароль!")
    else:
        messagebox.showerror("Ошибка", "Пользователь не найден!")

    conn.close()
