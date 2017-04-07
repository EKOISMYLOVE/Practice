#!/usr/bin/python
"""
This is my practice.
I need change label text.
Cause mainloop() , I must use thread to finish it.
"""

from Tkinter import *
import time
import thread

def print_time (delay):
	while True:
		time.sleep(0.1)
		label.configure(text=time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime()))

root=Tk()
root.title("Date & Time")
root.minsize(300,25)
label=Label(root,text=time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime()))
label.pack()
try:
	thread.start_new_thread( print_time , (1,))
except:
	label.configure(text="Error: unable to start thread")

root.mainloop()



