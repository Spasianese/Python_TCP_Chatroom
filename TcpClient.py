# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 13:00:56 2018

TCP Client Program
"""

import sys
from socket import *
import tkinter as tk
from tkinter import *
import threading

clientSocket = socket( AF_INET, SOCK_STREAM )

def chattingReq():
    # if statement that takes care of the logging in request and errors, errors aren't implemented yet
    if(ipEntry.get()!=""):
        # takes ip and port and connects
        serverName = ipEntry.get()
        serverPort = int(portEntry.get()) 
        clientSocket.connect( (serverName, serverPort) )
        # takes username
        message = userEntry.get()
        clientSocket.send( message.encode() )
        # tests if username is deemed valid
        if(clientSocket.recv(2048).decode()=='CONTINUE'):
            message = pwsEntry.get()
            clientSocket.send( message.encode() )
            # AT THIS POINT WE NEED TO OPEN ANOTHER THREAD FOR CLIENT SIDE THAT LISTENS AND RECIEVES MSGS FROM THE REST
            # ACTUALLY, MAYBE WE COULD START THE THREAD WHENEVER WE HAVE THE USER JOIN A CHATROOM
            # detroys log in screen and opens chatting section
            root.destroy()
            openChatting()
    else:
        welcomeLabel.config(text="dummy")

def openChatting():
    # func that sets username 
    def nickName():
        if(enterName.get()!=''):
            message = enterName.get()
            # Send it to the server
            clientSocket.send( message.encode() )
    # func that sends actual msg and recieves own msg
    def serverSend():
        if(sendMsg.get()!=''):
            message = sendMsg.get()
            # Send it to the server
            clientSocket.send( message.encode() )
        
            # get the uppercase response from the server
            modifiedMessage = clientSocket.recv(2048)
        
            # display the response
            textBox.insert("1.0", '\n' + modifiedMessage.decode())
    def quitChat():
        clientSocket.close()
        root2.destroy()
    root2 = tk.Tk()
    root2.geometry("500x500")
    root2.title("Attempt 1.1")
    textBox = tk.Text(root2, state='normal')
    textBox.pack()
    sendMsg = tk.Entry(root2)
    sendMsg.pack()
    sendMsgBtn = tk.Button(root2,text="send",command=serverSend)
    sendMsgBtn.pack()
    quitBtn = tk.Button(root2,text="quit",command=quitChat)
    quitBtn.pack()
    enterName = tk.Entry(root2)
    enterName.pack()
    sendName = tk.Button(root2,text="send",command=nickName)
    sendName.pack()
    
    root2.mainloop()


root = tk.Tk()
root.geometry("500x500")
root.title("Attempt 1.0")

welcomeLabel = tk.Label(root, text="autumn sucks")
welcomeLabel.pack()

ipEntry = tk.Entry(root)
portEntry = tk.Entry(root)
ipEntry.pack()
portEntry.pack()

userLabel = tk.Label(root,text="userName")
userLabel.pack()
userEntry = tk.Entry(root)
userEntry.pack()
pwsLabel = tk.Label(root,text="password")
pwsLabel.pack()
pwsEntry = tk.Entry(root)
pwsEntry.pack()

newWindowBtn = tk.Button(root,text="attempt3",command=chattingReq)
newWindowBtn.pack()



root.mainloop()
