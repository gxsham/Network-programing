import socket, sys
import time
s_client = socket.socket()
s_client.connect( ('127.0.0.1', 1045) )
while 1:
    mess = sys.stdin.readline()
    if mess!="":
        s_client.send(mess)
    answer = s_client.recv(25000)
    if answer!="":        
        if answer.startswith(b'\xff\xd8'):
            file = open("newTerminator.jpg", "wb")
            file.write(answer)
            file.close()
            sys.stdout.write("Picture recieved")
        else:
            sys.stdout.write(answer)
