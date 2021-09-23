
#importing all the modules
#only need to import tkinter and tkinter.colorchooser 
# for the color pallete

from tkinter import *
import tkinter.ttk as ttk
import tkinter.colorchooser as cc
from tkinter import messagebox



#defining the mian root of the GUI
# and a few properties
root = Tk()
root.geometry('600x200')
root.title('ColorGen')




#Frame where the color is displayed
colorframe = Frame(root, bg='white')
colorframe.place(relheight=0.6, relwidth=0.9, relx=0.05, rely=0.05)



#frame with the hex code entry amd color chooser
frame = Frame(root)
frame.place(relheight=0.3, relwidth=0.8, relx=0.1, rely=0.7)



#functions


# this function lets u choose the color from a color palette to
#  change the color of the main color frame.
def choosecolor(e=None):
    color = cc.askcolor(title='Choose Color')
    colorentry.delete(0, END)
    colorentry.insert(END, color[1])
    enter()




#This function uses the hex code in the entry field to change the 
#color of the main color frame where the color is displayed
def enter(e=None):
    try:
        colorframe.config(bg=str(colorentry.get()))
    except:
        messagebox.showerror('ColorGen', 'There has been an error. Try checking if the hex code exists or not!')




#This function removes the current color from the color frame
def remove(e=None):
    colorframe.config(bg='white')



#frame widgets
Label(frame, text='Hex Code').grid(row=0, column=0, pady=5, padx=2)
colorentry = Entry(frame, bd=1, width=20)
colorentry.grid(row=1, column=0, pady=2, padx=5)

Button(frame, bg='white', bd=0, text='Enter', cursor='hand2',height=3, width=5, command=enter).grid(row=0, rowspan=2, column=1)

colorbtn = Button(frame, bg='#0398fc', fg='white', bd=0, text='Choose Color', height=3, width=15, cursor='hand2', command=choosecolor)
colorbtn.grid(row=0, column=2, padx=20, rowspan=2)

Button(frame, bg='white', bd=0, text='Remove Color', cursor='hand2',height=3, width=13, command=remove).grid(row=0, rowspan=2, column=3)


#bindings: to bind the keyboard and GUI

root.bind('<Return>', enter)  #press enter button to use hex code on the color frame
root.bind('<Delete>', remove) # press delete button to remove current color from color frame
root.bind('<Control-c>', choosecolor) # Press control+c to use colorchooser




mainloop()