# importing the necessary module
from tkinter import ttk
import tkinter
import re
import os
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
from tkinter import *
from mysql.connector.errors import Error as errors
import random


def code_generating():
    generating_codes = "0123456789"
    length = 5
    ac_number = "".join(random.sample(generating_codes, length))
    coonfirmpassord.set(ac_number)


def show_hide_password():
    if comPassword['show'] == '.':
        comPassword.configure(show='')
        btn_show.configure(image=show_image)

    else:
        comPassword.configure(show='.')
        btn_show.configure(image=hide_image)


# coding for sumbit button to database


def submit():
    if username.get().lower() == 'username'.strip():
        messagebox.showwarning('Warning', 'Please Fill The Field Username')
    elif email_address.get().lower() == 'e-mail address'.strip():
        messagebox.showwarning('Warning', 'Please Fill The Field E-Mail Address')
    elif user_password.get().lower() == 'password':
        messagebox.showwarning('Warning', 'Please Fill the Field Password')
    else:
        try:
            # declaring the constant variable for database
            db_username = 'root'
            pwd = ''
            dbname = 'voting'
            host = 'localhost'
            # end of the constant variable for database
            con = mysql.connector.connect(host=host, database=dbname, user=db_username, password=pwd)
            cursor = con.cursor()

            sql = "INSERT INTO users (`username`, `email`, `password`, `reference_code`) VALUES (%s, %s,%s,%s) "
            value = (username.get(), email_address.get(), user_password, coonfirmpassord.get())

            cursor.execute(sql, value)
            con.commit()

        except errors:
            messagebox.showerror('Database Error', 'The email used is already exist.')
        finally:
            con.close()


window = Tk()
window.title('Sign Up Form')
window.geometry('900x500+200+100')
window.configure(bg='#fff')
window.resizable(False, False)

# declaration of entry variable constant

username = StringVar()
email_address = StringVar()
user_password = StringVar()
coonfirmpassord = StringVar()

# end of entry variable declaration


img = PhotoImage(file='images/values-1.png')
Label(window, image=img, border=0, bg='white').place(x=50, y=90)
# declaring variables
user_image = PhotoImage(file='icons/person_30px.png')
email_image = PhotoImage(file='icons/gmail_logo_30px.png')
password_image = PhotoImage(file='icons/password_30px.png')
hide_image = PhotoImage(file='icons/hide_30px.png')
show_image = PhotoImage(file='icons/eye_30px.png')
save_image = PhotoImage(file='icons/save_30px.png')
code_image = PhotoImage(file='icons/elections_30px.png')
generated_code = PhotoImage(file='icons/code_30px.png')

frame = Frame(window, width=350, height=390, bg='white')
frame.place(x=480, y=50)

heading = Label(frame, text='Account Creation Page', fg='#57a1f8', bg='white', font=('arial black', 15, 'bold'))
heading.place(x=60, y=5)


# ..................................................
def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    if user.get() == '':
        user.insert(0, 'Username')


user = Entry(frame, width=45, fg='black', border=0, bg='white', font=('Microsoft, Yahei, UILight', 11),
             textvariable=username)
user.place(x=60, y=85)
username_image = Label(frame, image=user_image, background='white')
username_image.place(x=25, y=75)
user.insert(0, 'Username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)
Frame(frame, width=305, height=2, bg='green').place(x=25, y=110)


# ..................................................
def on_enter(e):
    password1.delete(0, 'end')


def on_leave(e):
    if password1.get() == '':
        password1.insert(0, 'E-mail Address')


password1 = Entry(frame, width=45, fg='black', border=0, bg='white', font=('Microsoft, Yauheni, UILight', 11),
                  textvariable=email_address)
password1.place(x=60, y=150)
email_add_image = Label(frame, image=email_image, background='white')
email_add_image.place(x=25, y=145)
password1.insert(0, 'E-mail Address')
password1.bind("<FocusIn>", on_enter)
password1.bind("<FocusOut>", on_leave)
Frame(frame, width=305, height=2, bg='green').place(x=25, y=177)


# ..................................................
def on_enter(e):
    comPassword.delete(0, 'end')


def on_leave(e):
    if comPassword.get() == '':
        comPassword.insert(0, 'Password')


comPassword = Entry(frame, width=29, fg='black', border=0, bg='white', font=('Microsoft, Yahei, UILight', 11),
                    textvariable=user_password)
comPassword.place(x=60, y=220)
password_ima = Label(frame, image=password_image, background='white')
password_ima.place(x=25, y=210)
comPassword.insert(0, 'Password')
comPassword.bind("<FocusIn>", on_enter)
comPassword.bind("<FocusOut>", on_leave)
Frame(frame, width=305, height=2, bg='green', ).place(x=25, y=247)

btn_show = Button(frame, image=show_image, bg='white', border=0, command=show_hide_password)
btn_show.place(x=300, y=210)


# the generated voting codes
def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    if code.get() == '':
        code.insert(0, 'Generated Voting Code')


code = Entry(frame, width=29, fg='black', border=0, bg='white', font=('Microsoft, Yauheni, UILight', 11),
             textvariable=coonfirmpassord)
code.place(x=60, y=270)
generate_ima = Label(frame, image=code_image, background='white')
generate_ima.place(x=25, y=260)
code.insert(0, 'Generated Voting Code')
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)
Frame(frame, width=305, height=2, bg='green', ).place(x=25, y=300)

generated_btn = Button(frame, image=generated_code, bg='white', border=0, command=code_generating)
generated_btn.place(x=300, y=260)

# ...........................................

Button(frame, pady=7, text='Create Voting Account', bg='white', fg='black', cursor='hand2', border=2, relief=GROOVE,
       image=save_image, command=submit,
       compound=LEFT, font=('calibre', 10, 'bold')).place(x=35, y=320, width=290, height=40)
label = Label(frame, text='I have an account', fg='black', bg='white', font=('arial', 9))
label.place(x=90, y=370)

signin = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8')
signin.place(x=200, y=370)

mainloop()
