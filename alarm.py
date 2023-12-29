
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import time, sys
from pygame import mixer
from PIL import Image, ImageTk

def alarm():
    alarm_time=user_input.get()
    if alarm_time=="":
        messagebox.askretrycancel("Error Message","Please Enter value")
    else:
        while True:
            time.sleep(1)
            if(alarm_time==time.strftime("%H:%M")):
                playmusic()
def playmusic():
    mixer.init()
    mixer.music.load(' clock.mp3')
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(30)
        mixer.music.stop()
        sys.exit()
                                          
root=Tk()
root.title(" Alarm clock")
canvas=Canvas(root, width=600,height=380)
image=ImageTk.PhotoImage(Image.open("clock image .png"))
canvas.create_image(0,0,anchor=NW, image=image)

canvas.pack()
header=Frame(root)

box1=Frame(root)
box1.place(x=250,y=180)
box2=Frame(root)
box2.place(x=250,y=180)
 #time taken by user
 #helv36 = tkFont.Font(family="Helvetica",size=36,weight="bold")
 

user_input=Entry(box1,font=('ArialNarrow', 20),width=8)
user_input.grid(row=0, column=2)

#set alarm button 
start_button = Button( )
root.mainloop()


#done

