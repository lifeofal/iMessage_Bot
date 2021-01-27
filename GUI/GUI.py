import tkinter
import time
import random
from iMessage_Lyric_App import iMessage_Bot as iMB
import emoji

numberBool = False

def onPressNumber():
    number = numInput.get()
    fullName = firstName.get()
    print(fullName)
    numberBool = True

    if bool(number):

        iMB.get_lyrics_and_send_messages(number, numberBool)
        message = iMB.getMessage()


        num.config(text=message, justify=tkinter.CENTER, anchor=tkinter.W,  wraplength=300)

    else:
        numberBool = False
        iMB.get_lyrics_and_send_messages(fullName, numberBool)
        message = iMB.getMessage()

        num.config(text=message, justify=tkinter.CENTER, anchor=tkinter.W, wraplength=300)
        #num.config(text='Invalid number')


window = tkinter.Tk()

window.iconbitmap('gear.ico')

window.title('iMessage Bot')
window.geometry('600x500')
window.resizable(width=False, height=False)
window.config(background='gray')


title = tkinter.Label(text='iMessage Bot')
title.place(x=100, y=20)
title.config(font=('Times New Roman', 30, 'bold'), background='gray')

numTxt = tkinter.Label(text='Phone Number')
numTxt.place(x=260, y=100)
numTxt.config(font=('Times New Roman', 23, 'bold'), background='gray')

numTxt2 = tkinter.Label(text='Full Name')
numTxt2.place(x=260, y=200)
numTxt2.config(font=('Times New Roman', 23, 'bold'), background='gray')

numInput = tkinter.Entry()
numInput.place(x=255, y=145)
numInput.config(font=('Times New Roman', 10, 'bold'))

firstName = tkinter.Entry()
firstName.place(x=255, y=245)
firstName.config(font=('Times New Roman', 10, 'bold'))

#LastName = tkinter.Entry()
#LastName.place(x=255, y=345)
#LastName.config(font=('Times New Roman', 10, 'bold'))


button = tkinter.Button(text='Confirm', command=onPressNumber)
button.place(x=280, y=425)
button.config(font=100, height=2, width=10)

num = tkinter.Label(text='No message has been sent')
num.place(x=330, y=550, anchor='center')
num.config(font=('Times New Roman', 20, 'bold'), background='gray')

window.mainloop()
