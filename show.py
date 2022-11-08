# start of module import
from tkinter import *
from tkinter import messagebox
import re
import random
import os
from tkinter import font
from tkinter import ttk
import mysql.connector as mysql
from mysql.connector.errors import Error
import time

# end of module import
# ......................................

apc_count = 1


def apc_counting():
    global apc_count
    voting = messagebox.askyesno('title', 'Do You Want to Vote for All Progressive Party')
    if voting:
        ballot_apc_vote.configure(image=thumb_image)
        apc_count = apc_count + 1
        apc_erad_voting['value'] += 4
        if apc_erad_voting['value'] == apc_count:
            return

    else:
        pass
        ballot_apc_vote.configure(image='')


pdp_count = 1


def pdp_counting():
    global pdp_count
    voting = messagebox.askyesno('title', 'Do You Want to Vote for People Democratic Party')
    if voting:
        ballot_apc_vote.configure(image=thumb_image)
        pdp_count = pdp_count + 1
        pdp_erad_voting['value'] += 4
        if pdp_erad_voting['value'] == pdp_count:
            return

    else:
        pass
        ballot_apc_vote.configure(image='')


lab_count = 1


def lab_counting():
    global lab_count
    voting = messagebox.askyesno('title', 'Do You Want to Vote for Labour Party')
    if voting:
        ballot_lab_vote.configure(image=thumb_image)
        lab_count = lab_count + 1
        lab_erad_voting['value'] += 4
        if lab_erad_voting['value'] == lab_count:
            return

    else:
        pass
        ballot_apc_vote.configure(image='')


adc_count = 1


def adc_counting():
    global adc_count
    voting = messagebox.askyesno('title', 'Do You Want to Vote for African Democratic Congress')
    if voting:
        ballot_adc_vote.configure(image=thumb_image)
        adc_count = adc_count + 1
        adc_erad_voting['value'] += 4
        if adc_erad_voting['value'] == adc_count:
            return

    else:
        pass
        ballot_adc_vote.configure(image='')


sdp_count = 1


def sdp_counting():
    global sdp_count
    voting = messagebox.askyesno('title', 'Do You Want to Vote for Social Democratic Party')
    if voting:
        ballot_sdp_vote.configure(image=thumb_image)
        sdp_count = sdp_count + 1
        sdp_erad_voting['value'] += 4
        if sdp_erad_voting['value'] == sdp_count:
            return

    else:
        pass
        ballot_adc_vote.configure(image='')


def yng():
    voting = messagebox.askyesno('Voting', 'Did u want to vote for Young Progressive Party')
    if voting:
        ballot_yng_vote.configure(image=thumb_image)
    else:
        ballot_yng_vote.configure(image='')


def fetch():
    messagebox.showinfo('Fetching', 'Thank You for fetching information from database')


def validate():
    referencing = reference_number.get()
    if(referencing) == 'tosin'.lower():
        messagebox.showinfo('Validation Parse', 'U can now cast your vote for ur favourite candidate of your choice by clicking on the button at the left side but remember u are suppose to click once and once u click on the button u vote has already be casted to the candidate of your choice \n\n Vote Wisely, and dont sell your future')

        ballot_apc.configure(state='normal')
        ballot_pdp.configure(state='normal')
        ballot_lab.configure(state='normal')
        ballot_adc.configure(state='normal')
        ballot_sdp.configure(state='normal')
        ballot_yng.configure(state='normal')

    else:
        messagebox.showerror('er', 'error')


frame = Tk()
frame.title('The Main Voting Application')
frame.geometry('300x300')

# styling the ttk style
style = ttk.Style()
style.configure('title.TLabel', font=('Segoe UI Black', 35, 'bold'), foreground='black')
style.configure('reference.TButton', font=('Segoe UI Black', 10, 'bold'), foreground='black')
# image uploads and import
apc_voting_image = PhotoImage(file='images/vote_apc.png')
pdp_voting_image = PhotoImage(file='images/pdp_vote.png')
lab_voting_image = PhotoImage(file='images/lab_vote.png')
adc_voting_image = PhotoImage(file='images/vote_adc.png')
sdp_voting_image = PhotoImage(file='images/vote_sdp.png')
yng_voting_image = PhotoImage(file='images/yng_vote.png')
apc_image = PhotoImage(file='images/new_apc.png')
pdp_image = PhotoImage(file='images/new_pdp.png')
lab_image = PhotoImage(file='images/new_lab.png')
adc_image = PhotoImage(file='images/new_adc.png')
sdp_image = PhotoImage(file='images/new_sdp.png')
nigeria = PhotoImage(file='images/new_nigeria_flag.png')
side_apc_image = PhotoImage(file='images/apc_new.png')
side_pdp_image = PhotoImage(file='images/pdp_new.png')
side_lab_image = PhotoImage(file='images/lab_new.png')
side_adc_image = PhotoImage(file='images/adc_new.png')
apc_erad_image = PhotoImage(file='images/erad_asiwaju.png')
pdp_erad_image = PhotoImage(file='images/erad_atiku.png')
lab_erad_image = PhotoImage(file='images/obi_erad.png')
adc_erad_image = PhotoImage(file='images/erad_dumebi.png')
sdp_erad_image = PhotoImage(file='images/erad_adebayo.png')
apc_count_image = PhotoImage(file='images/count_apc.png')
pdp_count_image = PhotoImage(file='images/count_pdp.png')
lab_count_image = PhotoImage(file='images/count_lab.png')
adc_count_image = PhotoImage(file='images/count_adc.png')
sdp_count_image = PhotoImage(file='images/count_sdp.png')
thumb_image = PhotoImage(file='images/thumb_second-removebg-preview.png')

# declaration of string variables constant
reference_number = StringVar()

caption_label = ttk.Label(text='The Presidential Election Portal'.upper(), style='title.TLabel')
caption_label.pack(pady=10)
# reference display

# end of reference display on voter's reference code

# start of validation display

# end of validation display

# start of ballot paper and boxes
ballot_display = ttk.LabelFrame(width=205, height=680, text="Ballot Voting Page")
ballot_display.place(x=10, y=10)
# apc segment
ballot_apc = Button(ballot_display, image=apc_voting_image, relief=GROOVE, border=2,
                    command=apc_counting, state='disabled')
ballot_apc.place(x=9, y=10)
ballot_apc_vote = Label(ballot_display, text='voting apc', background='white', relief=GROOVE, border=1)
ballot_apc_vote.place(x=104, y=10, height=96, width=90)
# end of apc segment

# pdp segment
ballot_pdp = Button(ballot_display, image=pdp_voting_image, relief=GROOVE, border=2,
                    command=pdp_counting, state='disabled')
ballot_pdp.place(x=9, y=107)
ballot_pdp_vote = Label(ballot_display, text='voting pdp', background='white', relief=GROOVE, border=1)
ballot_pdp_vote.place(x=104, y=107, height=96, width=90)
# end of pdp segment

# lab party segment
ballot_lab = Button(ballot_display, image=lab_voting_image, relief=GROOVE, border=2,
                    command=lab_counting, state='disabled')
ballot_lab.place(x=9, y=204)
ballot_lab_vote = Label(ballot_display, text='voting lab', background='white', relief=GROOVE, border=1)
ballot_lab_vote.place(x=104, y=204, height=96, width=90)
# end of labour party segment


# adc segment
ballot_adc = Button(ballot_display, image=adc_voting_image, relief=GROOVE, border=2,
                    command=adc_counting, state='disabled')
ballot_adc.place(x=9, y=302)
ballot_adc_vote = Label(ballot_display, text='voting adc', background='white', relief=GROOVE, border=1)
ballot_adc_vote.place(x=104, y=302, height=96, width=90)
# end of adc segment

# sdp segment
ballot_sdp = Button(ballot_display, image=sdp_voting_image, relief=GROOVE, border=2,
                    command=sdp_counting, state='disabled')
ballot_sdp.place(x=9, y=400)
ballot_sdp_vote = Label(ballot_display, text='voting sdp', background='white', relief=GROOVE, border=1)
ballot_sdp_vote.place(x=104, y=400, height=96, width=90)

# end of sdp segment

# young progressive segement
ballot_yng = Button(ballot_display, image=yng_voting_image, relief=GROOVE, border=2,
                    command=yng, state='disabled')
ballot_yng.place(x=9, y=500)
ballot_yng_vote = Label(ballot_display, text='voting sdp', background='white', relief=GROOVE, border=1)
ballot_yng_vote.place(x=104, y=500, height=96, width=90)
# end of young progressive segment
castVotes = ttk.Button(ballot_display, text='New Vote')
castVotes.place(x=9, y=600, width=180, height=50)
# end of ballot paper and boxes

# president image frontier display
frontier_display = ttk.LabelFrame(frame, width=1020, height=300, text='Presidency Frontiers')
frontier_display.place(x=220, y=80)

apc_button_image = ttk.Button(frontier_display, image=apc_image, compound='top',
                              text='''



ASIWAJU AHMED BOLA TINUBU
        
APC PRESIDENTIAL CANDIDATE''')
apc_button_image.place(x=10, y=10)
apc_flag = ttk.Label(apc_button_image, image=nigeria)
apc_flag.place(x=10, y=120)
side_apc = ttk.Label(apc_button_image, image=side_apc_image)
side_apc.place(x=120, y=120)

pdp_button_image = ttk.Button(frontier_display, image=pdp_image, compound=TOP,
                              text='''
  
  
  
  ALAHJI ATIKU ABUBAKAR

PDP PRESIDENTIAL CANDIDATE''')

pdp_button_image.place(x=210, y=10)
pdp_flag = Label(pdp_button_image, image=nigeria)
pdp_flag.place(x=10, y=120)
side_pdp = ttk.Label(pdp_button_image, image=side_pdp_image)
side_pdp.place(x=120, y=120)

lab_button_image = ttk.Button(frontier_display, image=lab_image, compound='top',
                              text='''



                PETER OBI

LAB. PRESIDENTIAL CANDIDATE''')
lab_button_image.place(x=410, y=10)
lab_flag = Label(lab_button_image, image=nigeria)
lab_flag.place(x=10, y=120)
lab_pdp = ttk.Label(lab_button_image, image=side_lab_image)
lab_pdp.place(x=120, y=120)

adc_button_image = ttk.Button(frontier_display, image=adc_image, compound='top',
                              text='''



          DUMEBI KWACHIWI

ADC PRESIDENTIAL CANDIDATE''')
adc_button_image.place(x=610, y=10)
adc_flag = Label(adc_button_image, image=nigeria)
adc_flag.place(x=10, y=120)
adc_pdp = ttk.Label(adc_button_image, image=side_adc_image)
adc_pdp.place(x=120, y=120)

sdp_button_image = ttk.Button(frontier_display, image=sdp_image, compound='top',
                              text='''



        ADEWOLE ADEBAYO

SDP PRESIDENTIAL CANDIDATE''')
sdp_button_image.place(x=810, y=10)
sdp_flag = Label(sdp_button_image, image=nigeria)
sdp_flag.place(x=10, y=120)

summary_display = ttk.LabelFrame(frame, width=1142, height=300, text='Summary of Electioneering'.upper())
summary_display.place(x=220, y=390)

validation_display = ttk.LabelFrame(summary_display, width=300, height=200, text='Validation Keys')
validation_display.place(x=10, y=10)
user_validation = ttk.Label(validation_display, text='Enter Voter Reference Code')
user_validation.place(x=10, y=10)
user_validation_entry = ttk.Entry(validation_display, width=45, textvariable=reference_number)
user_validation_entry.place(x=10, y=30, height=30)
user_validation_button = ttk.Button(validation_display, text='Validate Voter', command=validate)
user_validation_button.place(x=10, y=70, width=100, height=40)

erad_config = ttk.LabelFrame(summary_display, width=478, height=270, text='Erad Configuration Display')
erad_config.place(x=320, y=10)
apc_erad = Label(erad_config, image=apc_erad_image, relief=SUNKEN, border=1)
apc_erad.place(x=10, y=10)
apc_erad_voting = ttk.Progressbar(erad_config, mode='determinate', orient='horizontal',
                                  maximum=100, value=0, length=410)
apc_erad_voting.place(x=60, y=20)

pdp_erad = Label(erad_config, image=pdp_erad_image, relief=SUNKEN, border=1)
pdp_erad.place(x=10, y=54)
pdp_erad_voting = ttk.Progressbar(erad_config, mode='determinate', orient='horizontal',
                                  maximum=100, value=0, length=410)
pdp_erad_voting.place(x=60, y=65)

lab_erad = Label(erad_config, image=lab_erad_image, relief=SUNKEN, border=1)
lab_erad.place(x=10, y=97)
lab_erad_voting = ttk.Progressbar(erad_config, mode='determinate', orient='horizontal',
                                  maximum=100, value=0, length=410)
lab_erad_voting.place(x=60, y=110)

adc_erad = Label(erad_config, image=adc_erad_image, relief=SUNKEN, border=1)
adc_erad.place(x=10, y=140)
adc_erad_voting = ttk.Progressbar(erad_config, mode='determinate', orient='horizontal',
                                  maximum=100, value=0, length=410)
adc_erad_voting.place(x=60, y=150)

sdp_erad = Label(erad_config, image=sdp_erad_image, relief=SUNKEN, border=1)
sdp_erad.place(x=10, y=183)
sdp_erad_voting = ttk.Progressbar(erad_config, mode='determinate', orient='horizontal',
                                  maximum=100, value=0, length=410)
sdp_erad_voting.place(x=60, y=195)

# counting of votes segment
counting_config = ttk.LabelFrame(summary_display, width=335, height=270, text="Voting Counting Erad Configuration")
counting_config.place(x=800, y=10)

apc_counting_image = Label(counting_config, image=apc_count_image, relief=SUNKEN, border=1)
apc_counting_image.place(x=10, y=10)
apc_counting_label = Label(counting_config, text='The Total Vote Cast  : '.upper())
apc_counting_label.place(x=60, y=20)

pdp_counting_image = Label(counting_config, image=pdp_count_image, relief=SUNKEN, border=1)
pdp_counting_image.place(x=10, y=55)
pdp_counting_label = Label(counting_config, text='The Total Vote Cast  : '.upper())
pdp_counting_label.place(x=60, y=62)

lab_counting_image = Label(counting_config, image=lab_count_image, relief=SUNKEN, border=1)
lab_counting_image.place(x=10, y=100)
lab_counting_label = Label(counting_config, text='The Total Vote Cast  : '.upper())
lab_counting_label.place(x=60, y=110)

adc_counting_image = Label(counting_config, image=adc_count_image, relief=SUNKEN, border=1)
adc_counting_image.place(x=10, y=140)
adc_counting_label = Label(counting_config, text='The Total Vote Cast  : '.upper())
adc_counting_label.place(x=60, y=150)


sdp_counting_image = Label(counting_config, image=sdp_count_image, relief=SUNKEN, border=1)
sdp_counting_image.place(x=10, y=180)
sdp_counting_label = Label(counting_config, text='The Total Vote Cast  : '.upper())
sdp_counting_label.place(x=60, y=190)
frame.mainloop()
