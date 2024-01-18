from tkinter import *
from tkinter import messagebox
import tkinter as tk
import time
import threading
from pygame import mixer
from PIL import Image, ImageTk

def set_alarm():
    alarm_time = user_input.get()
    if not alarm_time:
        messagebox.showerror("Error", "Please enter a valid time")
    else:
        alarm_thread = threading.Thread(target=alarm, args=(alarm_time,))
        alarm_thread.start()

def alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            play_music()
            break
        time.sleep(1)

def play_music():
    mixer.init()
    mixer.music.load('clock.mp3')
    mixer.music.play()
    root.after(30000, stop_music)

def stop_music():
    mixer.music.stop()

# GUI setup
root = tk.Tk()
root.title("Alarm Clock")

# Load and display an image
img = Image.open("clock_image .png")  
photo = ImageTk.PhotoImage(img)
image_label = Label(root, image=photo)
image_label.image = photo 
image_label.pack() # Keep a reference to avoid garbage collection


label = Label(root, text="Enter alarm time (HH:MM):")
label.pack()

user_input = Entry(root)
user_input.pack()

alarm_button = Button(root, text="Set Alarm", command=set_alarm)
alarm_button.pack()

root.mainloop()
