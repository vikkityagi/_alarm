#import requirements file
import datetime
from playsound import playsound
from tkinter import *
from tkinter import messagebox
import webbrowser
import time

#print programmer name
print("This alarm made by vikki")

#print current time
print("the alarm has started from : "
      +str(datetime.datetime.now().hour),str(datetime.datetime.now().minute),str(datetime.datetime.now().second),
      datetime.datetime.now().strftime("%p"))

#alarm time
alarmHour=str(input("Enter hour to wake up?:"))
alarmMinute=str(input("Enter minute to wake up?:"))
alarmSecond=str(input("Enter second to wake up?:"))
ampm=str(input("Time Format AM/PM?:"))

#assignment
ah=alarmHour
aM=alarmMinute
aS=alarmSecond

#print time format
tf=datetime.datetime.now().strftime("%p")

#diffrenece between current time from alarm time
rhour = int(alarmHour) - datetime.datetime.now().hour
rminute = int(alarmMinute) - datetime.datetime.now().minute
rsecond = int(alarmSecond) - datetime.datetime.now().second

#calculate net time in second
remainingtime = rhour * 3600 + rminute * 60 + rsecond

#assignment
remainingtime1 = remainingtime

#convert net time into minute,second format
alarmMinute = 0
while remainingtime > 59:
    alarmMinute += 1
    remainingtime -= 60
print("the alarm has started on after :" + str(alarmMinute) + " Minute " + str(remainingtime) + " Second")

#count time between current time to alarm time
while alarmMinute>=0:
    while remainingtime!=0:
        time.sleep(1)
        remainingtime-=1
        print(f"{alarmMinute}:{remainingtime}")
    alarmMinute-=1

    remainingtime=60


#alarm process
if ampm == tf:
    while True:
        if ah == str(datetime.datetime.now().hour) and \
                aM == str(datetime.datetime.now().minute) and \
                aS == str(datetime.datetime.now().second) and \
                ampm == str(datetime.datetime.now().strftime("%p")):
            playsound('Midnight-chimes-sound-effect.mp3')
            opinion = input("if you want to close this alarm(Yes/No): ")
            if opinion=='Yes':
                break
            else:
                while True:
                    playsound('Midnight-chimes-sound-effect.mp3')


