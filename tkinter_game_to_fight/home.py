from tkinter import Tk
from tkinter import ttk

from function_to_game import enter_to_game
from register_players import register_players
from windows_info import windows_info

root = Tk()
root.title('game to fight')
root.geometry("300x250")

btn_enter = ttk.Button(text="вход", command=enter_to_game)
btn_register = ttk.Button(text="регистрация", command=register_players)
btn_info = ttk.Button(text="информация", command=windows_info)

btn_enter.pack()
btn_enter.place(relx=0.5, rely=0.3, anchor="c")

btn_register.pack()
btn_register.place(relx=0.5, rely=0.4, anchor="c")

btn_info.pack()
btn_info.place(relx=0.5, rely=0.5, anchor="c")

root.mainloop()
