import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("500x500")
root.title("Sign In Screen")

welcomeLabel = tk.Label(root, text="Server IP:")
portLabel = tk.Label(root, text="Port:")
ipEntry = tk.Entry(root)
portEntry = tk.Entry(root)
welcomeLabel.place(x=20,y=0)
ipEntry.place(x=90, y=0)
portLabel.place(x=270,y=0)
portEntry.place(x=315,y=0)

userLabel = tk.Label(root, text="Username:")
userEntry = tk.Entry(root)
userLabel.place(x=210,y=50)
userEntry.place(x=180,y=70)

pwsLabel = tk.Label(root, text="Password:")
pwsEntry = tk.Entry(root)
pwsLabel.place(x=210,y=90)
pwsEntry.place(x=180,y=110)

signIn = tk.Button(root,text="Sign In")
signIn.place(x=220,y=150)

root.resizable(False,False)
root.mainloop()
