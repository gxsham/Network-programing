from socket import * 
import time, sys, io, random , linecache
from time import gmtime, strftime
from thread import start_new_thread
HOST = "127.0.0.1"
PORT = 1045
listeningSocket = socket()
#bind the socket to an interface
listeningSocket.bind( (HOST, PORT) )
print "bind = OK"
#make it listen
listeningSocket.listen(5) 
def client_thread(newAllocatedSocket):   
    while newAllocatedSocket:
        try:
            data = newAllocatedSocket.recv(100)
            sys.stdout.write(data)
        except:
            return
        if data == "hastalavista\n":
            newAllocatedSocket.close()
            listeningSocket.close()
        elif data =="pic\n":
            file = open('Terminator.jpg','rb') 
            newAllocatedSocket.send(file.read())
            file.close()
        elif data.startswith('reverse'):
            rever = data[8:]
            newAllocatedSocket.send(rever[::-1]+'\n') 
        elif data =="joke\n":
            newAllocatedSocket.send(linecache.getline('jokes.txt',random.randint(1,12)))
        elif data =="host\n":
            newAllocatedSocket.send(HOST+ "\n")
        elif data =="close\n":
            newAllocatedSocket.close()
        elif data =="time\n":
            newAllocatedSocket.send(strftime("%a, %d %b %Y %H:%M:%S\n", gmtime()))    
        else:
            if data.endswith('?\n'):
                newAllocatedSocket.send('42\n')
            else:
                newAllocatedSocket.send("Can you elaborate on that?\n")
while 1:
    newAllocatedSocket, address = listeningSocket.accept()   
    start_new_thread(client_thread,(newAllocatedSocket,))
    print address, newAllocatedSocket
