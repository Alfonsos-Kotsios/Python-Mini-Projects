from tkinter import *

def drag_start(event):
  widget = event.widget
  widget.startX = event.x
  widget.startY = event.y
def drag_motion(event):
  widget = event.widget
  x = widget.winfo_x()-widget.startX + event.x
  y = widget.winfo_y() -widget.startY + event.y
  widget.place(x=x,y=y)

window =Tk()


label = Label(window,bg="red",height=5,width=10)
label.place(x=0,y=0)
label.bind("<Button-1>",drag_start)
label.bind("<B1-Motion>",drag_motion)


label2 = Label(window,bg="blue",height=5,width=10)
label2.place(x=10,y=10)
label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)

window.mainloop()
