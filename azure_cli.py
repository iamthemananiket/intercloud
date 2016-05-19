from socket import *
serverPort = 12005
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
import sys 
import subprocess
import argparse
import os

print("Azure ready")
while 1:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024)
        parms=sentence.decode('ascii')
        image_name =parms.split(":")[0]
        flavor_name=parms.split(":")[1]
        instance_name=parms.split(":")[2]
        
        print("Running azure CLI")       
	
        print(image_name)
        
        def fetch_image(x):
                return {
                    "CentOS-6.2-x64-v5.8.8.1": '0b11de9248dd4d87b18621318e037d37__RightImage-CentOS-6.2-x64-v5.8.8.1',
                    "Oracle-Linux-6-12-2014": 'c290a6b031d841e09f2da759bbabe71f__Oracle-Linux-6-12-2014',
                    "Windows-8.1-Enterprise-N-x64-en.us-201507.20": '03f55de797f546a1b29d1b8d66be687a__Windows-8.1-Enterprise-N-x64-en.us-201507.20'
                }[x]
        
        cod='start /wait cmd /c azure vm create ' + instance_name + ' ' + fetch_image(image_name) + ' aniket --location "East US" --vm-size ' + flavor_name + " & timeout 5"
        
        os.system(cod) 
        #print(result)
        connectionSocket.send(b"Instance has been created")
        connectionSocket.close()
