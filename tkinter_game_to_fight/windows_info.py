from tkinter import *
from tkinter import ttk


def windows_info():
    window = Tk()
    window.title("окно информации")
    window.geometry("250x200")
    label = ttk.Label(window, text="Принципиально новое окно")
    label.pack(anchor=CENTER, expand=1)
    #root.destroy()