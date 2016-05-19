from socket import *
serverPort = 12001
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

print("Server ready")
while 1:
        connectionSocket, addr = serverSocket.accept()
        msg = connectionSocket.recv(1024)
        param = msg.decode('ascii')
        options = ["Security","Region","Memory","Compute","Load Balancing"]
        param = param.split("-")
        opscore = 0
        azurescore = 0
        prefer = { 
                "Security":"azure",
                "Region":"openstack",
                "Memory":"azure",
                "Compute":"openstack",
                "Load Balancing":"azure"
                }
        count = 5
        for p in param:
                property = options[int(p)-1]
                if(prefer[property] == "openstack" ):
                        opscore = opscore + count
                else:
                        azurescore = azurescore + count
                count = count - 1
        
        print(opscore,azurescore)
        if(opscore > azurescore):
                cloud_ip = '127.0.0.1'
                cloud_name = 'openstack'
        else:
                cloud_ip = '127.0.0.1'
                cloud_name = "azure"
        #connectionSocket.send(b"Recieved Params")
        return_str = cloud_ip + ":" + cloud_name
        connectionSocket.send(bytes(return_str, encoding='utf-8'))
        connectionSocket.close()
