from tkinter import *

root = Tk()
# create label
myLabel1 = Label(root, text="Hello GSG",font=("Times",50))
myLabel2 = Label(root, text="Welcome to programming",font=("Times",50))
# show label in screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

root.mainloop()
