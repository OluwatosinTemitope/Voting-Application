# the first display of the application module importing
from tkinter import ttk
import tkinter
from tkinter import *
import registration


# end of module import
def user_reg():
    root.destroy()
    registration.reg()


root = Tk()
root.title('The Voting Application as Designed by Oluwatosin')
root.geometry('500x400+400+200')
root.resizable(0, 0)
root.overrideredirect(1)

style = ttk.Style()
style.theme_use('vista')
style.configure('title.TLabel', font=('bold'), foreground='tomato')
# start to configure the application
display_frame = Frame(root, width=500, height=400, background='white', relief=FLAT, border=8)
display_frame.place(x=0, y=0)

# settig the images
reg_images = PhotoImage(file='icons/Users_80px.png')
ballot_box_image = PhotoImage(file='icons/ballot_box_with_ballot_80px.png')

caption = Label(display_frame, text='Electronic'.upper(), background='white', font=('Segoe UI Black', 45, 'bold'))
caption.place(x=10, y=10)
caption_two = Label(display_frame, text='Voting Application'.upper(), background='white',
                    font=('Segoe UI Black', 32, 'bold'))
caption_two.place(x=10, y=90)

# plcaing the buttons
reg_button = Button(display_frame, text='Create User Profile', image=reg_images, compound=TOP, cursor='hand2',
                    relief=GROOVE, background='white', activebackground='white', font=('Segoe UI Black', 15, 'bold'),
                    command=user_reg)
reg_button.place(x=10, y=200, height=130, width=230)

vote_button = Button(display_frame, text='Start Voting App', image=ballot_box_image, compound=TOP, cursor='hand2',
                     relief=GROOVE, background='white', activebackground='white', font=('Segoe UI Black', 15, 'bold'))
vote_button.place(x=250, y=200, height=130, width=230)

root.mainloop()
