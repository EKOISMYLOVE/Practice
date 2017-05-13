#!/usr/bin/python
import sys
from Tkinter import *

root=Tk()
root.title("AI Move")
root.minsize(400,400)
root.resizable(width=False,height=False)

x1 = 10
y1 = 10
x2 = 380
y2 = 380

def keyleft(event):
    global x1,y1,x2,y2
    x1 = x1 - 5
    AI_MOVE()

    window.delete("all")
    window.create_rectangle(0,0,400,400,fill='black')
    window.create_oval(x1,y1,x1+10,y1+10,fill="#ff0000")
    window.create_oval(x2,y2,x2+10,y2+10,fill="#0000ff")
    window.pack(expand=YES , fill=BOTH)
def keyright(event):
    global x1,y1,x2,y2
    x1 = x1 + 5
    AI_MOVE()

    window.delete("all")
    window.create_rectangle(0,0,400,400,fill='black')
    window.create_oval(x1,y1,x1+10,y1+10,fill="#ff0000")
    window.create_oval(x2,y2,x2+10,y2+10,fill="#0000ff")
    window.pack(expand=YES , fill=BOTH)
def keyup(event):
    global x1,y1,x2,y2
    y1 = y1 - 5
    AI_MOVE()

    window.delete("all")
    window.create_rectangle(0,0,400,400,fill='black')
    window.create_oval(x1,y1,x1+10,y1+10,fill="#ff0000")
    AI_MOVE()
    window.create_oval(x2,y2,x2+10,y2+10,fill="#0000ff")
    window.pack(expand=YES , fill=BOTH)
def keydown(event):
    global x1,y1,x2,y2
    y1 = y1 + 5
    AI_MOVE()

    window.delete("all")
    window.create_rectangle(0,0,400,400,fill='black')
    window.create_oval(x1,y1,x1+10,y1+10,fill="#ff0000")
    window.create_oval(x2,y2,x2+10,y2+10,fill="#0000ff")
    window.pack(expand=YES , fill=BOTH)

def AI_MOVE():
    global x1,y1,x2,y2
    if x1+5 < x2+5:
        x2 = x2-2
    if x1+5 > x2+5:
        x2 = x2+2
    if y1+5 < y2+5:
        y2 = y2-2
    if y1+5 > y2+5:
        y2 = y2+2

root.bind('<Left>' , keyleft)
root.bind('<Right>' , keyright)
root.bind('<Up>' , keyup)
root.bind('<Down>' , keydown)

window=Canvas(width=400, height=400,bg="#000")
oval1=window.create_oval(10,10,20,20,fill="#ff0000")
oval2=window.create_oval(380,380,390,390,fill="#0000ff")

window.pack()
root.mainloop()
