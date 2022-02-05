###This script takes a .ics calendar file with a bunch of events, and parses the events depending on the
###contents of the title of each calendar events to seperate calendar files. The original use was to parse 
###an academic assignment schedule exported from the Canvas learning system to have each course's work
###displayed as a seperate calendar file.

#import several libraries of code that help this program run:
from ast import Global
from cgitb import text
from struct import pack
from icalendar import Calendar, Event, vCalAddress, vText
from datetime import datetime
from pytz import UTC # timezone
import os
from pathlib import Path
import time

import tkinter as tk
from tkinter import ttk
from tkinter import * 

root = Tk()

###GUI SECTION###
#################
#################
# This is the section of code which creates the main window
root.geometry('616x424')
root.configure(background='#FFD39B')
root.title('Jordan\'s Canvas Calendar Builder!')


# This is the section of code which creates a text input box and label for it for the URL, and each course name
URL_label = tk.Label(text="Please Paste the Google Calendar URL \n from Canvas here:")
URL_label.pack(fill=tk.BOTH, side=tk.TOP)
URL_input=Entry(root)
URL_input.pack(fill=tk.BOTH, side=tk.TOP)

course_instructions = tk.Label(text="Please provide the names of your courses EXACTLY as they appear in \n the Canvas calendar (ex: PS 3903)")
course_instructions.pack(fill=tk.BOTH, side=tk.TOP)
course1label = tk.Label(text="Course #1 Name:")
course1label.pack(fill=tk.BOTH, side=tk.TOP)
course1input=Entry(root)
course1input.pack(fill=tk.BOTH, side=tk.TOP)

course2label = tk.Label(text="Course #2 Name:")
course2label.pack(fill=tk.BOTH, side=tk.TOP)
course2input=Entry(root)
course2input.pack(fill=tk.BOTH, side=tk.TOP)

course3label = tk.Label(text="Course #3 Name:")
course3label.pack(fill=tk.BOTH, side=tk.TOP)
course3input=Entry(root)
course3input.pack(fill=tk.BOTH, side=tk.TOP)

course4label = tk.Label(text="Course #4 Name:")
course4label.pack(fill=tk.BOTH, side=tk.TOP)
course4input=Entry(root)
course4input.pack(fill=tk.BOTH, side=tk.TOP)

course5label = tk.Label(text="Course #5 Name:")
course5label.pack(fill=tk.BOTH, side=tk.TOP)
course5input=Entry(root)
course5input.pack(fill=tk.BOTH, side=tk.TOP)

course6label = tk.Label(text="Course #6 Name:")
course6label.pack(fill=tk.BOTH, side=tk.TOP)
course6input=Entry(root)
course6input.pack(fill=tk.BOTH, side=tk.TOP)

course7label = tk.Label(text="Course #7 Name:")
course7label.pack(fill=tk.BOTH, side=tk.TOP)
course7input=Entry(root)
course7input.pack(fill=tk.BOTH, side=tk.TOP)

# This is the section of code which creates a button to trigger the collegction and parsing of data
submitbutton = tk.Button(text="Press to Parse Calendar!")
submitbutton.pack(fill=tk.BOTH, side=tk.TOP)

# this is a function to get the user input from the text input box
import requests


###DATA PARSING SECTION###
##########################
##########################
#function that will be called to run the calendar sorting part of the program
def sort_calendars(course1,course2,course3,course4,course5,course6,course7):
    global userinput
    global userinput1
    global userinput2
    global userinput3
    global userinput4
    global userinput5
    global userinput6
    global userinput7

    userinput = URL_input.get()
    requests.get(userinput).text

    userinput1 = course1input.get()
    #requests.get(userinput1).text

    userinput2 = course2input.get()
    #requests.get(userinput2).text

    userinput3 = course3input.get()
    #requests.get(userinput3).text

    userinput4 = course4input.get()
    #requests.get(userinput4).text

    userinput5 = course5input.get()
    #requests.get(userinput5).text

    userinput6 = course6input.get()
    #requests.get(userinput6).text

    userinput7 = course7input.get()
    #requests.get(userinput7).text

    time.sleep(.002)

    #create a new google calendar
    cal = Calendar()
    cal.add('prodid', '-//PS 3903 Calendar//mxm.dk//')
    cal.add('version', '2.0')

    #set the variable "g" to open the input calendar file from Canvas:
    g = open(userinput,'rb')
    #set the variable "gcal" to read the calendar file opened from Canvas:
    gcal = Calendar.from_ical(g.read())

    #for loops that says "For each calendar event, if the title includes [course name], add it to this calendar:
    for component in gcal.walk():
        if str(course1) in str(component.get('summary')):
            cal.add_component(component)

            f = open('PS 3903.ics', 'wb')
            f.write(cal.to_ical())
            f.close()
        else:
            continue

    for component in gcal.walk():
        if str(course2) in str(component.get('summary')):
            cal.add_component(component)

            f = open('PS 3803.ics', 'wb')
            f.write(cal.to_ical())
            f.close()
        else:
            continue

    for component in gcal.walk():
        if str(course3) in str(component.get('summary')):
            cal.add_component(component)

            f = open('PS 4993.ics', 'wb')
            f.write(cal.to_ical())
            f.close()
        else:
            continue

    for component in gcal.walk():
        if str(course4) in str(component.get('summary')):
            cal.add_component(component)

            f = open('PS 1303.ics', 'wb')
            f.write(cal.to_ical())
            f.close()
        else:
            continue

    for component in gcal.walk():
        if str(course5) in str(component.get('summary')):
            cal.add_component(component)

            f = open('PS 1303.ics', 'wb')
            f.write(cal.to_ical())
            f.close()
        else:
            continue

    for component in gcal.walk():
        if str(course6) in str(component.get('summary')):
            cal.add_component(component)

            f = open('PS 1303.ics', 'wb')
            f.write(cal.to_ical())
            f.close()
        else:
            continue

    for component in gcal.walk():
        if str(course7) in str(component.get('summary')):
            cal.add_component(component)

            f = open('PS 1303.ics', 'wb')
            f.write(cal.to_ical())
            f.close()
        else:
            continue    

#This function binds the "right clieck" key to running the "sort calendars" function when the button is pressed
submitbutton.bind("<Button-1>", sort_calendars(
    userinput1,
    userinput2,
    userinput3,
    userinput4,
    userinput5,
    userinput6,
    userinput7
))

root.mainloop()
