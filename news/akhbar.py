from tkinter import *
from PIL import ImageTk,Image
root=Tk()

def every_100(text):
    finale_text=""
    for i in range(0,len(text)):
        finale_text +=text[i]
        if i%100==0 and i!=0:
            finale_text += "\n"
    return finale_text

root.geometry("1000x1000")
root.title("aapka aapna akhabar")

Label(root,text="Apka Apna Akhbar",font="SUNKEN 20 bold").pack()
Label(root,text="2 february, 2021",font="SUNKEN 10 bold").pack()
photos=[]
texts=[]
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text=f.read()
        texts.append(every_100(text))

    image=Image.open(f"{i+1}.jpg")
        #TODO: Resize these images
    image=image.resize((200,200),Image.ANTIALIAS) # FUNCTION TO RESIZE THE IMAGE BIGGER TO SMALLER
    photos.append(ImageTk.PhotoImage(image))
f1=Frame(root,width=600,height=150)
Label(f1,text=texts[0],padx=22,pady=22).pack(side="left")
Label(f1,image=photos[0],anchor="e").pack(padx=10,pady=10)
f1.pack(anchor="w")

f2=Frame(root,width=600,height=150)
Label(f2,text=texts[1],padx=22,pady=22).pack(side="left")
Label(f2,image=photos[1],anchor="e").pack()
f2.pack(anchor="w")

f3=Frame(root,width=600,height=150)
Label(f3,text=texts[2],padx=22,pady=22).pack(side="left")
Label(f3,image=photos[2],anchor="e").pack()
f3.pack(anchor="w")
root.mainloop()