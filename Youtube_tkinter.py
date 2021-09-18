from tkinter import *
from tkinter import messagebox
import pytube
from pytube import YouTube

root=Tk()
root.title("Youtube downloader")
root.geometry("600x300")

lbl_title=Label(root,text="Youtube downloader",font=("times new roman",25,"bold"))
lbl_title.place(x=95,y=2)

url=Label(root,text="URL:-",font=("times new roman",20,"bold"))
url.place(x=10,y=50)

link=Entry(root,bd=6,font=("times new roman",15,"bold"))
link.place(x=95,y=50,width=300)

#1080
var=IntVar()
check=Checkbutton(root,text="1080p",font=("times new roman",15,"bold"),variable=var)
check.place(x=95,y=100)

#720
var1=IntVar()
check1=Checkbutton(root,text="720p",font=("times new roman",15,"bold"),variable=var1)
check1.place(x=180,y=100)

#only mp3
var2=IntVar()
check2=Checkbutton(root,text="webm",font=("times new roman",15,"bold"),variable=var2)
check2.place(x=265,y=100)

btn_submit=Button(root,text=">",font=("times new roman",20,"bold"),command=lambda:submitdata(),bg="black",fg="white")
btn_submit.place(x=400,y=50,height=35,width=100)

def submitdata():
    yturl=link.get()
    yt=YouTube(yturl)
    resolutions=yt.streams#.filter().order_by('resolution').desc()                  ....this will sort list descending order
    print(*resolutions,sep='\n')
    if var.get()==1:
        itag1080=yt.streams.get_by_itag("399")
        print("downloading...")
        itag1080.download()
        print("download complete")
    elif var1.get()==1:
        itag720=yt.streams.get_by_itag("398")
        print("downloading...")
        itag720.download()
        print("download complete")
    elif var2.get()==1:
        itagmp3=yt.streams.get_by_itag("251")
        print("downloading...")
        itagmp3.download()
        print("download complete")
    else:
        itag=yt.streams.get_highest_resolution()
        print("downloading...")
        itag.download()
        print("download complete")
   
root.mainloop()
