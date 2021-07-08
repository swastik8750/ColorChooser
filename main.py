from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("COLOUR CHOOSER :)")
root.geometry("400x400")

def color():
    my_color = colorchooser.askcolor()[1]
    my_label =Label(root, text = my_color).pack()
    mp_label2 = Label(root,text= "You Picked A color!!",font = ("Helvetica",32), bg= my_color).pack()
my_button=Button(root,text='Pick A Color', command= color).pack()

root.mainloop()