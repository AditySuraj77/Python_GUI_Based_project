import tkinter

import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from tkinter import *
from tkinter import messagebox

root = Tk()


def check_detail():
    number = number_enter.get()
    phone = phonenumbers.parse(number)
    time = timezone.time_zones_for_number(phone)
    car = carrier.name_for_number(phone, 'en')
    reg = geocoder.description_for_number(phone, 'en')
    result_label = Label(root, text=f"Detail : \n{phone} \n{time} \n{car} \n{reg}", font=('Roboto', 10, 'normal'))
    result_label.place(x=5, y=300, height=190, width=290)
    number_enter.delete(first=0,last=END)




root.geometry('300x500')
root.title('PhoneNumber Detail')
root.configure(background='navajo white')

title = Label(root, text='Identify Phone \nNumber', font=('Roboto', 30, 'normal'))
title.place(x=15, y=20)

number_label = Label(root, text='Enter Number', font=('Roboto', 15, 'normal'))
number_label.place(x=80, y=150)

number_enter = Entry(root, width=20, )
number_enter.place(x=80, y=190)

sign_label = Label(root, text='+__', font=('Roboto', 11, 'normal'), height=1)
sign_label.place(x=45, y=190)

button = Button(root, text='CHECK', font=('Roboto', 11, 'normal'), command=check_detail)
button.place(x=110, y=230)

root.mainloop()
