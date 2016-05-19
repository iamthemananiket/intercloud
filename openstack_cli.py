from socket import *
serverPort = 12005
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
import sys 
import subprocess
import argparse
import os

print("OP1 ready")
while 1:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024)
        parms=sentence.decode('ascii')
	image_name =parms.split(":")[0]
	flavor_name=parms.split(":")[1]
	instance_name=parms.split(":")[2] 
	print("wait running command")       
	#f.close()
	#run cmd
	print(image_name)
	print(flavor_name)
	cod="nova boot --image "+image_name+" --flavor "+flavor_name+" "+instance_name
	os.system(cod)
        connectionSocket.send(b"has been created")
        connectionSocket.close()
