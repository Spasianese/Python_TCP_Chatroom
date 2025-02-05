import tkinter as tk
from tkinter import *

chatroomRoot = tk.Tk()
chatroomRoot.geometry("500x500")
chatroomRoot.title("Chatroom")

welcomeLabel = tk.Label(chatroomRoot, text="Join a Chatroom:",font=("Arial",20))
welcomeLabel.place(x=150,y=0)

chatRoom1 = tk.Button(chatroomRoot,text="CSC460",font=("Arial",20))
chatRoom1.place(x=25,y=50, width=150, height=50)
chatRoom2 = tk.Button(chatroomRoot,text="CSIT",font=("Arial",20))
chatRoom2.place(x=25,y=110,width=150, height=50)
chatRoom3 = tk.Button(chatroomRoot,text="General",font=("Arial",20))
chatRoom3.place(x=25,y=170,width=150, height=50)
logoutButton = tk.Button(chatroomRoot,text="Logout",font=("Arial",15))
logoutButton.place(x=375,y=450,width=90, height=30)

chatroomRoot.resizable(False,False)
chatroomRoot.mainloop()
