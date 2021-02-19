from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newfile():
    global file
    root.title("Untitled-Notepad")
    file=None
    textarea.delete(1.0,END)    # delete all from 1 line 0 char to end
def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetype=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad")  # title change and path to open other file
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()
def savefile():
    global file
    if file==None:    # mean if file is none that mean save as the file as new file
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetype=[("All Files","*.*"),("Text Document","*.txt")])
        if file=="":
            file=None
        else:
            #save as new  file
            f=open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()
    else:
        # save the new  file
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()
def quitapp():
    root.destroy()
def cut():
    textarea.event_generate(("<<Cut>>"))     # this event_generate automatic handle cut commandsame for other
def copy():
    textarea.event_generate(("<<Copy>>"))
def paste():
    textarea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad","notepad made by ravi pratap singh")

if __name__ =="__main__":
    # basic tkinter setup
    root=Tk()
    root.title("Untitled - Notepad")
    root.geometry("644x788")

    # add text area
    textarea=Text(root,font="sunken 12")
    file=None
    textarea.pack(fill=BOTH,expand=True)

    #create menubar
    Menubar=Menu(root)
    # filemenu start
    Filemenu=Menu(Menubar,tearoff=0)
    # to open new file
    Filemenu.add_command(label="New",command=newfile)

    #to open already exist file
    Filemenu.add_command(label="Open",command=openfile)

    #to save a current file
    Filemenu.add_command(label="Save",command=savefile)
    Filemenu.add_separator()
    Filemenu.add_command(label="Exit",command=quitapp)
    Menubar.add_cascade(label="File",menu=Filemenu)    # to bind all label in filemanu
    # file menu ends

    # edit menu starts
    editmenu=Menu(Menubar,tearoff=0)
    # to give feature of cut,copy,paste
    editmenu.add_command(label="Cut",command=cut)
    editmenu.add_command(label="Copy",command=copy)
    editmenu.add_command(label="Paste",command=paste)
    Menubar.add_cascade(label="Edit",menu=editmenu)
    #edit menu ends

    #help menu starts
    helpmenu=Menu(Menubar,tearoff=0)
    helpmenu.add_command(label="About Notepad",command=about)
    Menubar.add_cascade(label="Help",menu=helpmenu)

    #helpmenu ends
    root.config(menu=Menubar)

    # adding scroolband
    scroll=Scrollbar(textarea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=scroll.set)

root.mainloop()