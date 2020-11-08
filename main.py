import pyqrcode
import re
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("QR Code Generator By IMAN")

window.geometry('350x300')

lbl = Label(window, text="Enter URL Below !!")
lbl.grid(column=3, row=0)
lbl.config(font=("times", 20))

txt = Entry(window, width=30)
txt.grid(column=3, row=2)


def error():
    messagebox.showerror("URL Error", "Incorrect URL")


def clicked():
    if not re.match('w{3}(.)([a-z]{3,})(.)(.{2,4})', Entry.get(txt)):
        error()
    else:
        url_gen = pyqrcode.create(Entry.get(txt))
        url_gen.svg('url.svg', scale=8)
        print(url_gen.terminal(quiet_zone=1))


btn = Button(window, text="Generate", command=clicked)

btn.grid(column=8, row=0)

window.mainloop()
