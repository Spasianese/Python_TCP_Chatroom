import tkinter as tk
from tkinter import *

chattingRoot = tk.Tk()
chattingRoot.geometry("500x500")
chattingRoot.title("Chatting")
textBox = tk.Text(chattingRoot, state='normal')
textBox.place(x=0,y=0)
sendMsg = tk.Entry(chattingRoot)
sendMsg.place(x=90,y=390,width=310, height=90)
sendMsgBtn = tk.Button(chattingRoot,text="send")
sendMsgBtn.place(x=405,y=400,height=90,width=90)
chatLeaveBtn = tk.Button(chattingRoot,text="Leave Room")
chatLeaveBtn.place(x=10,y=400,width=75,height=45)
quitBtn = tk.Button(chattingRoot,text="Log Out")
quitBtn.place(x=10,y=445,width=75,height=45)
    
chattingRoot.resizable(False,False)
chattingRoot.mainloop()
