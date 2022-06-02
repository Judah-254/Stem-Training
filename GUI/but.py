from tkinter import *
root =Tk()
def MyClick():
    Mylabel=Label(root,text="Hey,you clicked!")
    Mylabel.pack()
MyB=Button(root,text="Click me!",command=MyClick)
MyB.pack()
root.mainloop()