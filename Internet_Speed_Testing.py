from tkinter import *
import speedtest


def checkspeed():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / (10 ** 6), 3)) + 'Mbps'
    upl = str(round(sp.upload() / (10 ** 6), 3)) + 'Mbps'
    checking_download.config(text=down)
    Checking_upload.config(text=upl)


root = Tk()

root.title('Internet Speed Testing')
root.geometry('400x500')
root.configure(background='cyan')

title_lable = Label(root, text='Internet Speed Test', font=('Roboto', 30, 'bold'))
title_lable.place(x=15, y=20)

Downloading_lable = Label(root, text='Downloading', font=('Roboto', 20, 'bold'))
Downloading_lable.place(x=100, y=100,width=200)

checking_download = Label(root, text='00', font=('Roboto', 15, 'bold'))
checking_download.place(x=100, y=150,width=200)

Uploading_lable = Label(root, text='Uploading', font=('Roboto', 20, 'bold'))
Uploading_lable.place(x=100, y=200,width=200)

Checking_upload = Label(root, text='00', font=('Roboto', 15, 'bold'))
Checking_upload.place(x=100, y=250,width=200)

button = Button(root, text='Check', font=('Product Sans', 15, 'normal'),command=checkspeed)
button.place(x=150, y=300)

root.mainloop()
