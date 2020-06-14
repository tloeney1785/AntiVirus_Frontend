from tkinter import messagebox
from tkinter import *

def startup():
    global dictionary
    root = Tk() 
    root.geometry("400x220")
    root.title('Gmail Virus Detector') 
 
    top = Label(root, text='Manually enter \path for database.txt \nor hit enter to wait while the program finds it: ',font="times 12 bold") 
    top.place(x=60,y=0)

    nameL = Label(root, text='File Path:',font="times 12") 
    nameL.place(x=10,y=80)

    nameEL = Entry(root,font="times 12",width=35)
    nameEL.place(x=100,y=80)
    dictionary = nameEL.get()

    loginB = Button(root, text='Enter',  command=lambda:[searching(dictionary),root.destroy(),Login()],font = "time 14 italic bold",padx=50) 
    loginB.place(x=120,y=170)
    root.mainloop()

def Login():
 
    rootA = Tk() 
    rootA.geometry("400x220")
    rootA.title('Gmail Virus Detector') 
 
    top = Label(rootA, text='Gmail Virus Detector',font="times 20 bold") 
    top.place(x=60,y=0)
    header = Label(rootA, text='Please login with your Gmail Account',font="times 10 italic") 
    header.place(x=90,y=40)

    nameL = Label(rootA, text='Username:',font="times 14") 
    pwordL = Label(rootA, text='Password:',font = "times 14") 
    nameL.place(x=10,y=80)
    pwordL.place(x=10,y=120)

    nameEL = Entry(rootA,font="times 14")
    pwordEL = Entry(rootA, show='*', font ="times 14")
    nameEL.place(x=150,y=80)
    pwordEL.place(x=150,y=120)
    loginB = Button(rootA, text='Login & Scan',  command=lambda:[display("imap.gmail.com", nameEL.get(), pwordEL.get()),rootA.destroy()],font = "time 14 italic bold",padx=60) 
    loginB.place(x=100,y=170)
    rootA.mainloop()

def display(server,uname,pwd):

#display window
    root = Tk()
    root.geometry("600x450")
    root.title('Gmail Virus Detector') 

    top = Label(root, text='Scanning Emails...',font="times 20 bold") 
    top.place(x=60,y=0)
    listbox = Listbox(root, width = 85,height=25)
    listbox.place(x = 40, y = 40)

startup()
