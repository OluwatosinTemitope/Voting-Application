# start to import the neccessary module
from tkinter import *
from tkinter import messagebox
import re
import random
import os
from tkinter import filedialog as f
from tkinter import ttk
import mysql.connector as mysql
from mysql.connector.errors import Error
from tkinter import filedialog as f
from PIL import ImageTk, Image


filename = ''

# end of module import

def reg():
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
        newimage.save(currentPath + '/' + email_address.get() + '.jpg')

    def show_hide_password():
        if password_entry['show'] == '.':
            password_entry.configure(show='')
            btn_show.configure(image=show_image)

        else:
            password_entry.configure(show='.')
            btn_show.configure(image=hide_image)

    # end of variable for hide ans show password

    def code_generating():

        generating_codes = "0123456789"
        length = 5
        ac_number = "".join(random.sample(generating_codes, length))
        user_code.set(ac_number)

    def saved():
        try:
            db_username = 'root'
            pwd = ''
            dbname = 'voting'
            host = 'localhost'

            con = mysql.connect(host=host, database=dbname, user=db_username, password=pwd)
            cursor = con.cursor()

            sql = "INSERT INTO users(`username`, `email`, `password`, `reference_code`, `gender`) VALUES (%s, %s,%s,%s, %s)"
            value = (username.get(), email_address.get(), password.get(), user_code.get(), user_gender.get())
            cursor.execute(sql, value)
            con.commit()
            username.set('')
            email_address.set('')
            password.set('')
            user_code.set('')
            message = 'Your record has been saved successfully!'
            messagebox.showinfo('Saving Record', message)

        except Error as err:
            messagebox.showerror('Database Error', 'The email used is already exist.')
        finally:
            con.close()

    window = Tk()
    window.title('Voting Application')
    window.geometry('790x400+100+100')

    # declaring variable for images upload
    user_image = PhotoImage(file='icons/person_30px.png')
    email_image = PhotoImage(file='icons/gmail_logo_30px.png')
    password_image = PhotoImage(file='icons/password_30px.png')
    hide_image = PhotoImage(file='icons/hide_30px.png')
    show_image = PhotoImage(file='icons/eye_30px.png')
    save_image = PhotoImage(file='icons/save_30px.png')
    code_image = PhotoImage(file='icons/elections_30px.png')
    generated_code = PhotoImage(file='icons/code_30px.png')
    # end of images declaration upload

    # declaration of string var
    username = StringVar()
    email_address = StringVar()
    password = StringVar()
    user_code = StringVar()
    user_gender = StringVar()

    # label Frame Display
    label_caption = ttk.LabelFrame(window, width=580, height=350, text='Voter(s) Registration Page')
    label_caption.place(x=200, y=10)
    user_upload_image = ttk.LabelFrame(window, width=185, height=350, text='Upload User Picture')
    user_upload_image.place(x=10, y=10)

    lbl = Label(user_upload_image, relief=GROOVE, border=1, height=13, width=22)
    lbl.place(x=10, y=10)
    Button(user_upload_image, text='Select User Image', cursor='hand2',
    bg='white', fg='black', relief=GROOVE, font=('Impact', 10),compound=LEFT).place(x=10, y=220, width=158, height=35)
    # end of label Frame Display
    username_lable = Label(label_caption, text='Create User Voting Account'.upper(), font='impact')
    username_lable.place(x=150, y=15)
    # ..............username label and entry design....................................
    username_label = ttk.Label(label_caption, text='Username')
    username_label.place(x=10, y=55)
    username_entry = ttk.Entry(label_caption, width=75, textvariable=username)
    username_entry.place(y=50, x=100, height=30, )
    # ................ end of username and entry design

    # ..............Email Address label and entry design...............................
    email_label = ttk.Label(label_caption, text='E-mail Address')
    email_label.place(x=10, y=95)
    email_entry = ttk.Entry(label_caption, width=75, textvariable=email_address)
    email_entry.place(y=90, x=100, height=30)
    # ................ end of email address label and entry design.....................

    # ..............Password label and entry design....................................
    password_label = ttk.Label(label_caption, text='Password')
    password_label.place(x=10, y=135)
    password_entry = ttk.Entry(label_caption, width=75, textvariable=password)
    password_entry.place(y=130, x=100, height=37)
    btn_show = Button(password_entry, image=show_image, bg='white', border=0, command=show_hide_password)
    btn_show.place(x=420, y=3)
    # ................ end of password and entry design................................

    # ..............Generated Code label and entry design..............................
    code_label = ttk.Label(label_caption, text='Ref Code')
    code_label.place(x=10, y=183)
    code_entry = ttk.Entry(label_caption, width=75, textvariable=user_code)
    code_entry.place(y=175, x=100, height=37)
    gen_code = Button(code_entry, image=generated_code, bg='white', border=0, command=code_generating, )
    gen_code.place(x=420, y=3)
    # ................ end of password and entry design................................
    # start of module combo
    gender_label = ttk.Label(label_caption, text='Gender')
    gender_label.place(x=10, y=225)
    gender = ttk.Combobox(label_caption, values=('Woman'.upper(), 'Man'.upper()), state='readonly',
                          textvariable=user_gender)
    gender.place(x=100, y=220, width=455, height=30)

    # submit button
    save_btn = Button(label_caption, text='create account '.upper(), relief=GROOVE, bd=2, background='white',
                      command=saved,
                      image=save_image, compound=LEFT, font='impact')
    save_btn.place(x=100, y=260, height=40, width=200)

    vot_app = Button(label_caption, text='Launch Voting Application'.upper(), relief=GROOVE, background='white',
                     image=code_image, compound=LEFT)
    vot_app.place(x=320, y=260, height=40, width=220)
    # end of module

    # end of window display
    window.mainloop()


reg()
