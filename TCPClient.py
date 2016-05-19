from socket import *
servername = '127.0.0.1'
serverPort = 12001
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((servername,serverPort))
print("Welcome!")
print("Enter your priority: -")

print("1: Security, 2: Region, 3: Memory, 4: Compute, 5: Load Balancing")
msg = input("Enter order of priority seperated by a '-'\n")

clientSocket.send(msg.encode('ascii'))
modifiedSentence = clientSocket.recv(1024)
cloud_service = modifiedSentence.decode('ascii')
#print("From server: ",cloud_service)
clientSocket.close()

cloud_ip = cloud_service.split(":")[0]
cloud_name = cloud_service.split(":")[1]

print("From server: ",cloud_ip,cloud_name)

if (cloud_name == "openstack"):
    image_list = ["cirros-0.3.4-x86_64-uec", "cirros-0.3.4-x86_64-uec-kernel", "cirros-0.3.4-x86_64-uec-ramdisk"]
    flavor_list = ["m1.tiny", "m1.small", "m1.medium"]
else:
    image_list = ["CentOS-6.2-x64-v5.8.8.1", "Oracle-Linux-6-12-2014", "Windows-8.1-Enterprise-N-x64-en.us-201507.20"]
    flavor_list = ["ExtraSmall", "Small", "Medium"]

def select_image():
    print("Select one image - ")
    #print("a: cirros-0.3.4-x86_64-uec \nb: cirros-0.3.4-x86_64-uec-kernel \nc: cirros-0.3.4-x86_64-uec-ramdisk")
    for i in image_list:
        print(str(image_list.index(i)+1),':',i)
    
    def switch_image(x):
        return {
            '1': image_list[0],
            '2': image_list[1],
            '3': image_list[2]
        }[x]
        
    return switch_image(input("Enter choice - "))
    
#print(select_image())


def select_flavor():
    print("Select one flavor - ")
    #print("a: m1.tiny \nb: m1.small \nc: m1.medium")
    for i in flavor_list:
        print(str(flavor_list.index(i)+1),':',i)
    
    def switch_flavor(x):
        return {
            '1': flavor_list[0],
            '2': flavor_list[1],
            '3': flavor_list[2]
        }[x]
        
    return switch_flavor(input("Enter choice - "))
    
#print(select_flavor())


servername = cloud_ip
serverPort = 12005
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((servername,serverPort))
msg = select_image() + ":" + select_flavor() + ":" + input("Enter instance name - ")

clientSocket.send(msg.encode('ascii'))
modifiedSentence = clientSocket.recv(1024)
cloud_service = modifiedSentence.decode('ascii')
print("From ",cloud_name,cloud_service)
clientSocket.close()