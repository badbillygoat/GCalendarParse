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
# this is a function to get the user input from the text input box
import requests

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

# This is the section of code which creates a button to trigger the collection and parsing of data
submitbutton = tk.Button(text="Press to Parse Calendar!")
submitbutton.pack(fill=tk.BOTH, side=tk.TOP)


def open_calendar(filename):
    return open(filename, "rb")


###DATA PARSING SECTION###
##########################
##########################
#function that will be called to run the calendar sorting part of the program
def sort_calendars(event):
    #userinput = URL_input.get()
    #userinput = "https://weber.instructure.com/feeds/calendars/user_3tv3cVJzAq5N0HlijsgPx7p3ysN49elcM6G3XuFA.ics"


    userinput1 = course1input.get()
    if userinput1 != "":
        course_cal_1 = Calendar()
        course_cal_1.add("prodid", "-//{} Calendar//mxm.dk//".format(userinput1))
    else:
        print("User input 1 empty!")

    userinput2 = course2input.get()
    course_cal_2 = Calendar()

    userinput3 = course3input.get()
    userinput4 = course4input.get()
    userinput5 = course5input.get()
    userinput6 = course6input.get()
    userinput7 = course7input.get()

    #set the variable "gcal" to read the calendar file opened from Canvas:
    gcal = Calendar.from_ical(open_calendar("olivercalendar.ics").read())

    #for loops that says "For each calendar event, if the title includes [course name], add it to this calendar:
    for component in gcal.walk():
        print(str(component.get('summary')))
        if userinput1.lower() in str(component.get('summary')).lower():
            course_cal_1.add_component(component)

            # f = open('{}.ics'.format(userinput1), 'wb')
            # f.write(cal.to_ical())
            # f.close()
        else:
            continue

    # for component in gcal.walk():
    #     if str(course2) in str(component.get('summary')):
    #         cal.add_component(component)
    #
    #         f = open('Course2.ics', 'wb')
    #         f.write(cal.to_ical())
    #         f.close()
    #     else:
    #         continue
    #
    # for component in gcal.walk():
    #     if str(course3) in str(component.get('summary')):
    #         cal.add_component(component)
    #
    #         f = open('Course3.ics', 'wb')
    #         f.write(cal.to_ical())
    #         f.close()
    #     else:
    #         continue
    #
    # for component in gcal.walk():
    #     if str(course4) in str(component.get('summary')):
    #         cal.add_component(component)
    #
    #         f = open('Course4.ics', 'wb')
    #         f.write(cal.to_ical())
    #         f.close()
    #     else:
    #         continue
    #
    # for component in gcal.walk():
    #     if str(course5) in str(component.get('summary')):
    #         cal.add_component(component)
    #
    #         f = open('Course5.ics', 'wb')
    #         f.write(cal.to_ical())
    #         f.close()
    #     else:
    #         continue
    #
    # for component in gcal.walk():
    #     if str(course6) in str(component.get('summary')):
    #         cal.add_component(component)
    #
    #         f = open('Course6.ics', 'wb')
    #         f.write(cal.to_ical())
    #         f.close()
    #     else:
    #         continue
    #
    # for component in gcal.walk():
    #     if str(course7) in str(component.get('summary')):
    #         cal.add_component(component)
    #
    #         f = open('Course7.ics', 'wb')
    #         f.write(cal.to_ical())
    #         f.close()
    #     else:
    #         continue
    return

#This function binds the "right clieck" key to running the "sort calendars" function when the button is pressed
submitbutton.bind("<Button-1>", sort_calendars)

root.mainloop()