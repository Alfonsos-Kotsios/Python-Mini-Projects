from tkinter import *
window =Tk()

def dos(event):
  print("Mouse cordinate : " + str(event.x) + "," + str(event.y))

#window.bind("<Button-3>",dos)
#window.bind("<Button-2>",dos)
#window.bind("<Button-1>",dos)
#window.bind("<ButtonRelease>",dos)
#window.bind("<Enter>",dos)
window.bind("<Motion>",dos)
window.mainloop()
