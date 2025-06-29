
from tkinter import *
window =Tk()


def dosomething(event):
  label.config(text=event.keysym)


window.bind("<Key>",dosomething)

label = Label(window,font=('Arial',100))
label.pack()

window.mainloop()
