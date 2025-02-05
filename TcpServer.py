# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 13:14:47 2018

TCP Uppercase Echo server
"""

import sys
from socket import *
import threading

# ARRAY FOR USERS AND PASSWORDS
users = ['user1','user2','user3']
passwords = ['abcdef','123456','chatroom']

#ARRAY TO KEEP TRACK OF CURRENT USERS
signedIn = []
nickname = []

# ARRAY FOR BANNED NICKNAMES
bannedName = ['Styer']

#ARRAY TO STORE CLIENTS SOCKETS AND CHATROOMS
sockets = []

styerFanClub = []
ianHateClub = []
csc460 = []
csit = []
general = []

# variable to tell server to exit
keepRunning = True

# define a function to handle a single client
def client(clientSocket):
        chatRoom = ''   # variable to keep track of which chatroom user is in
        chatting = True # variable to keep track of whether user is in chatroom
        legitUser = False       # variable to decide if client has signed in
        duplication = False     # variable to test if username is duplicate
        currentName = ''        # var to keep track of nickname
        user = clientSocket.recv(4096).decode() # username entered by client

        # for loop to check if user is already signed in
        for i in range(len(signedIn)):
                if user == signedIn[i]:
                        duplication = True

        # for loop for login
        if not duplication:
                for i in range(len(users)):
                        if user == users[i]:
                                approval = "CONTINUE"
                                clientSocket.send( approval.encode() )
                                pws = clientSocket.recv(4096).decode()
                                if pws == passwords[i]:
                                        legitUser = True
                                        signedIn.append(users[i])
                                        break

        # while loop for main functions
        while legitUser:
                # nickname, checks if nickname is already taken
                currentName = clientSocket.recv(4096).decode()
                for i in range(len(nickname)):
                        if currentName == nickname[i]:
                                chatting = False

                chatRoom = clientSocket.recv(4096).decode()

                # Python doesn't have a switch command
                if (chatRoom.upper() == "CSC460"):
                        csc460.append(clientSocket)
                        chatRoom = csc460
                elif (chatRoom.upper() == "GENERAL"):
                        general.append(clientSocket)
                        chatRoom = general
                elif (chatRoom.upper() == "CSIT"):
                        csit.append(clientSocket)
                        chatRoom = csit
                elif (chatRoom.upper() == "STYERFANCLUB"):
                        styerFanClub.append(clientSocket)
                        chatRoom = styerFanClub
                elif (chatRoom.upper() == "IANHATECLUB"):
                        ianHateClub.append(clientSocket)
                        chatRoom = ianHateClub
                else:
                        print("you failed, L")

                # there should be a way to enter chatroom, but this would be the chatting
                while chatting:
                        # get a message from the client
                        sentance = currentName + ": " + clientSocket.recv(4096).decode()

                        # empty - Assume the client has disconnected
                        if len( sentance ) == 0:
                                return
                                
                        # send it back
                        for clientSocket in chatRoom:
                                clientSocket.send( sentance.encode() )

        clientSocket.close
# end function client()

# function to handle the main server socket accept loop
def listenLoop(serverPort):	
	# create the socket
	serverSocket = socket( AF_INET, SOCK_STREAM )
	serverSocket.bind( ('',serverPort) )

	# start the keyboard input thread
	# be ready for clients
	serverSocket.listen(1)

	print('The server is ready to receive')
	while keepRunning:
		# get a connection from a client
		connectionSocket, addr = serverSocket.accept()

		sockets.append(connectionSocket)
		
		# start up a thread for that client
		cl = threading.Thread( target=client, args=(connectionSocket,), daemon=True )
		cl.start()
	
# get the port for the server if not on the command line
if len(sys.argv) == 1:
	serverPort = int(input('Enter port number of server: ' ))
else:
	serverPort = int(sys.argv[1])

# get my Internet-ready IP address
s = socket(AF_INET, SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()

# create the main socket listener thread with the port number
sthread = threading.Thread( target=listenLoop, args=(serverPort,), daemon=True )
sthread.start()

# wait for input (this includes control-C)
input('Type anything to exit\n')

# exit (other threads stop since they are daemon threads)
