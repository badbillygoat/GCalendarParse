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
from tkinter import filedialog
import requests

root = Tk()
global initial_calendar
###GUI SECTION###
#################
#################

# This is the section of code which creates the main window
root.geometry('616x424') # Dimensions of GUI (in pixels) that opens
root.configure(background='#D7D5D2') #background color of window
root.title('Jordan\'s Canvas Calendar Builder!') #title that appears on top bar of window

def UploadAction(event=None): #this function assigns the .ics file uploaded to the "initial_calendar" variable
    global initial_calendar #declares that the "initia_calendar" var referenced below is the same variable as outside the function
    initial_calendar = filedialog.askopenfilename() #intiates the file explorer for the user to choose a file
    print('Selected:', initial_calendar) #verifies that the file was succesfully uploaded by printing the name of it

# This is the section of code which creates a text input box and label for it for the URL, and each course name
canvas_label = tk.Label(text="Please upload the .ics file downloaded from Canvas:")
canvas_label.pack(fill=tk.BOTH, side=tk.TOP)
button = tk.Button(root, text='Select File', command=UploadAction)
button.pack()


course_instructions = tk.Label(text="Please provide the names of your courses EXACTLY as they appear in \n the Canvas calendar- yes, capitalization matters (ex: PS 3903)")
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
submitbutton = tk.Button(root, text="Press to Parse Calendar!")
submitbutton.pack()


def open_calendar(filename):
    return open(filename, "rb")


###DATA PARSING SECTION###
##########################
##########################

#function that will be called to run the calendar sorting part of the program
def sort_calendars(event):
    #declares that the "initia_calendar" var referenced below is the same variable as outside the function
    global initial_calendar

    userinput1 = course1input.get() #reads the text input by the user from the first course...
    userinput2 = course2input.get()
    userinput3 = course3input.get()
    userinput4 = course4input.get()
    userinput5 = course5input.get()
    userinput6 = course6input.get()
    userinput7 = course7input.get()

    if userinput1 != "": #if NOT nothing is input into the 1st course input, then open a calendar and assign it to "course_cal_1", and name it "[Course Name] Calendar"...
        course_cal_1 = Calendar()
        course_cal_1.add('prodid', "-//{} Calendar//mxm.dk//".format(userinput1))
    if userinput2 != "":
        course_cal_2 = Calendar()
        course_cal_2.add("prodid", "-//{} Calendar//mxm.dk//".format(userinput2))
    if userinput3 != "":
        course_cal_3 = Calendar()
        course_cal_3.add("prodid", "-//{} Calendar//mxm.dk//".format(userinput3))
    if userinput4 != "":
        course_cal_4 = Calendar()
        course_cal_4.add("prodid", "-//{} Calendar//mxm.dk//".format(userinput4))
    if userinput5 != "":
        course_cal_5 = Calendar()
        course_cal_5.add("prodid", "-//{} Calendar//mxm.dk//".format(userinput5))
    if userinput6 != "":
        course_cal_6 = Calendar()
        course_cal_6.add("prodid", "-//{} Calendar//mxm.dk//".format(userinput6))
    if userinput7 != "":
        course_cal_7 = Calendar()
        course_cal_7.add("prodid", "-//{} Calendar//mxm.dk//".format(userinput7))
        
    else:
        print("User input empty!")
    

    #set the variable "gcal" to read the calendar file opened from Canvas:
    gcal = Calendar.from_ical(open_calendar(initial_calendar).read())

    #several for loops that say "For each calendar event, if the title includes [course name], add it to this calendar:
    for component in gcal.walk():
        if userinput1.lower() in str(component.get('summary')).lower():
            course_cal_1.add_component(component)
            a = open(str(userinput1)+".ics", 'wb')
            a.write(course_cal_1.to_ical())
            a.close()
        else:
            continue
        
    for component in gcal.walk():
        if userinput2 != "":
            if userinput2.lower() in str(component.get('summary')).lower():
                course_cal_2.add_component(component)
                b = open(str(userinput2)+".ics", 'wb')
                b.write(course_cal_2.to_ical())
                b.close()
        else:
            continue
    
    for component in gcal.walk():
        if userinput3 != "":
            if userinput3.lower() in str(component.get('summary')).lower():
                course_cal_3.add_component(component)
                c = open(str(userinput3)+".ics", 'wb')
                c.write(course_cal_3.to_ical())
                c.close()
        else:
            continue

    for component in gcal.walk():
        if userinput4 != "":
            if userinput4.lower() in str(component.get('summary')).lower():
                course_cal_4.add_component(component)
                d = open(str(userinput4)+".ics", 'wb')
                d.write(course_cal_4.to_ical())
                d.close()
        else:
            continue

    for component in gcal.walk():
        if userinput5 != "":
            if userinput5.lower() in str(component.get('summary')).lower():
                course_cal_5.add_component(component)
                e = open(str(userinput5)+".ics", 'wb')
                e.write(course_cal_5.to_ical())
                e.close()
        else:
            continue

    for component in gcal.walk():
        if userinput6 != "":
            if userinput6.lower() in str(component.get('summary')).lower():
                course_cal_6.add_component(component)
                f = open(str(userinput6)+".ics", 'wb')
                f.write(course_cal_6.to_ical())
                f.close()
        else:
            continue

    for component in gcal.walk():
        if userinput7 != "":
            if userinput7.lower() in str(component.get('summary')).lower():
                course_cal_7.add_component(component)
                g = open(str(userinput7)+".ics", 'wb')
                g.write(course_cal_7.to_ical())
                g.close()
        else:
            continue
    
    return

#This function binds the "right clieck" key to running the "sort calendars" function when the button is pressed
submitbutton.bind("<Button-1>", sort_calendars)

root.mainloop()