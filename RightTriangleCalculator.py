
import tkinter
from math import sqrt

master=tkinter.Tk()
master.title("Right Triangle Calculator")
master.geometry("300x150")

Label1=tkinter.Label(master, text="Side A:")
Label1.grid(row=1,column=0)

Entry1=tkinter.Entry(master)
Entry1.grid(row=1,column=1)

Label2=tkinter.Label(master, text="Side B:")
Label2.grid(row=2,column=0)

Entry2=tkinter.Entry(master)
Entry2.grid(row=2,column=1)

Label3=tkinter.Label(master, text="Side C:")
Label3.grid(row=3,column=0)

entryText=tkinter.StringVar()
Entry3=tkinter.Entry(master,state='readonly',textvariable=entryText)
Entry3.grid(row=3,column=1)


def calculate():
    average = round(sqrt(float(Entry1.get())**2 + float(Entry2.get())**2),3)
    entryText.set(average)
button3=tkinter.Button(master, text="Calculate",command=lambda:calculate())
button3.grid(row=4,column=1,padx=(40,10))

def close():
    master.destroy()

button4=tkinter.Button(master, text="Exit",command=lambda:close())
button4.grid(row=4,column=1,padx=(160, 10))

master.mainloop()
