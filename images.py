# importing the necessary module
from tkinter import *
import mysql.connector.errors as error
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
import os
from tkinter import filedialog as f
from PIL import ImageTk, Image

filename = ''


def show_image():
    global filename
    filename = f.askopenfilename(initialdir=os.getcwd(), defaultextension='.jpg', title='Open file for Upload',
                                 filetypes=[('Jpeg File (.jpg)', '*.jpg'), ('Png File (*.png', '*.png')])
    # using PIL
    myimage = Image.open(filename)
    newimage = myimage.resize((200, 200))
    img = ImageTk.PhotoImage(image=newimage)
    lbl.config(image=img, width=150, height=200)
    lbl.image = img

    # getting the current working path from os Module
    currentPath = os.getcwd() + '/images'
    # saving the image folder
    newimage.save(currentPath + '/' + emailvar.get() + '.jpg')


window = Tk()
window.title('Sign Up Form')
window.geometry('900x500+200+100')
# window.configure(bg='#fff')
window.resizable(False, False)
emailvar = StringVar()
lbl = Label(window, relief=GROOVE, border=1, height=13, width=22)
lbl.place(x=10, y=10)
em = ttk.Entry(window, textvariable=emailvar)
em.place(x=10, y=220, width=300, height=30)
Button(window, text='Select User Image', command=show_image, cursor='hand2',
       bg='white', fg='black', relief=GROOVE, font=('Impact', 10),
       compound=LEFT).place(x=10, y=260, width=158, height=35)
mainloop()
