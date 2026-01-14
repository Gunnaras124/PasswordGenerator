from tkinter import*
import tkinter as tk
import datetime
from ttkthemes import ThemedTk
from tkinter.ttk import*
import random
x=datetime.datetime.now()
window=ThemedTk(theme="ubuntu")
window.title("https://PasswordEncrypter.com")
window.geometry("800x600")
Password=StringVar()
EncryptedPassword=StringVar()
password2=""
password=""
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
day=x.day
month=x.month
key=(int(day)+int(month))*2
def copy_to_clipboard(entry_widget):
    window.clipboard_clear()
    window.clipboard_append(entry_widget.get())
def gen(*args):
    global power, combo, password
    password=""
    print(int(combo.get()))
    if power.get()==1:
        for i in range(int(combo.get())):
            password=password+(random.choice(lower))
            print(password)
        Password.set(password)
    elif power.get() == 2:
        for i in range(int(combo.get())):
            password = password + (random.choice(upper))
            print(password)
        Password.set(password)
    elif power.get() == 3:
        for i in range(int(combo.get())):
            password = password + (random.choice(digits))
            print(password)
        Password.set(password)


def encrypt():
    global password,password2
    for grammata in password:
        thesi = digits.index(grammata)
        password2 = password2 + digits[(thesi + key) % 72]
    EncryptedPassword.set(password2)
def decrypt():
    global password
    EncryptedPassword.set(password)



lbl=Label(window,text="Password:")
lbl.place(x=10,y=8)
txt=Entry(window,text=Password,state='disabled')
txt.place(x=100,y=10)
btn=Button(window,text="Copy",command=copy_to_clipboard)
btn.place(x=230,y=4)
btn1=Button(window,text="Generate",command=gen)
btn1.place(x=360,y=4)
lbl1=Label(window,text="Length:")
lbl1.place(x=10,y=36)
combo=Combobox(window)
combo['values']=(6,7,8,9,10)
combo.place(x=100,y=35)
power=IntVar()
power.set(1)
radio=Radiobutton(window,text="Low",value=1,variable=power)
radio.place(x=250,y=35)
radio1=Radiobutton(window,text="Medium",value=2,variable=power)
radio1.place(x=315,y=35)
radio2=Radiobutton(window,text="Strong",value=3,variable=power)
radio2.place(x=400,y=35)
lbl2=Label(window,text="Encrypt:")
lbl2.place(x=10,y=62)
txt1=Entry(window,text=EncryptedPassword,state='disabled')
txt1.place(x=100,y=64)
btn2=Button(window,text="Encrypt",command=encrypt)
btn2.place(x=230,y=59)
btn3=Button(window,text="Decrypt",command=decrypt)
btn3.place(x=360,y=59)

window.mainloop()