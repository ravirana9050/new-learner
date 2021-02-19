from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text")        # event.widget give button that is click and cget take text of button
    print(text)
    if text == "=":                       # mean scvalue contain string of digit like 546
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:                     # mean scvalue contain expression like 22*5 then perform operation
            try:
                value=eval(scvalue.get())
            except Exception as e:
                print(e)
                value="Error"
        scvalue.set(value)
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root=Tk()
root.geometry("644x700")
root.title("GUI Calculator")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 30 bold",bg="grey",fg="white")
screen.pack(fill="x",padx=30,pady=15)

f1=Frame(root,bg="blue")
b=Button(f1,text="9",font="lucida 50 bold",padx=15,pady=6)
b.bind("<Button-1>",click)                               # to bind the button with function
b.pack(side=LEFT,padx=8,pady=4)
b=Button(f1,text="8",font="lucida 50 bold",padx=15,pady=6)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=8,pady=4)
b=Button(f1,text="7",font="lucida 50 bold",padx=15,pady=6)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=8,pady=4)
b=Button(f1,text="%",font="lucida 50 bold",padx=20,pady=6)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=8,pady=4)
f1.pack(fill="x",padx=30)

f2=Frame(root,bg="blue")
b=Button(f2,text="6",font="lucida 50 bold",padx=15,pady=6)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=8,pady=4)
b=Button(f2,text="5",font="lucida 50 bold",padx=15,pady=6)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=8,pady=4)
b=Button(f2,text="4",font="lucida 50 bold",padx=15,pady=6)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=8,pady=4)
b=Button(f2,text="*",font="lucida 50 bold",padx=30,pady=6)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=8,pady=4)
f2.pack(fill="x",padx=30)

f3=Frame(root,bg="blue")
b=Button(f3,text="3",font="lucida 50 bold",padx=15,pady=6)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=8,pady=4)
b=Button(f3,text="2",font="lucida 50 bold",padx=15,pady=6)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=8,pady=4)
b=Button(f3,text="1",font="lucida 50 bold",padx=15,pady=6)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=8,pady=4)
b=Button(f3,text="/",font="lucida 50 bold",padx=33,pady=6)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=8,pady=4)
f3.pack(fill="x",padx=30)

f4=Frame(root,bg="blue")
b=Button(f4,text="0",font="lucida 50 bold",padx=15,pady=6)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=8,pady=4)
b=Button(f4,text="-",font="lucida 50 bold",padx=22,pady=6)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=8,pady=4)
b=Button(f4,text="+",font="lucida 50 bold",padx=14,pady=6)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=8,pady=4)
b=Button(f4,text="=",font="lucida 50 bold",padx=24,pady=6)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=8,pady=4)
f4.pack(fill="x",padx=30)


root.mainloop()