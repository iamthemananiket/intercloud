# Intercloud
1) TCPClient.py - Maneesh's PC

2) TCPServer.py - Sharvel's PC

3) openstack_cli.py - Shreyash's Virtualbox VM

4) azure_cli.py - Aniket's PC

# Flow of events
1) TCPServer.py, openstack_cli.py and azure_cli.py are launched on Sharvel's, Shreyash's and Aniket's PCs

2) Once the 3 are ready, TCPClient.py is launcehd on Maneesh's PC. 

3) Preferred priority is input.

4) TCPClient.py builds a connection with TCPServe.py and sends the priority order sting to it.

5) TCPServer.py makes a decision based on the hardcoded dictionary.

6) TCPServer responds with the name and IP address of the most suited cloud service (Openstack/Azure) to TCPClient.py

7) TCPClient.py recieves the name and IP address of the service.

8) TCPClient.py displays a list of images and flavors for the respective cloud service and ask the user to select on from each.

9) TCPClient.py then builds a socket connection with the cloud service (Shreyash PC/Aniket PC) and sends the image and flavor name to either of the two PCs.

10) One of the two Cloud service PCs (Openstack - Shreyash PC/ Azure - Aniket PC) recieve the data sent by TCPClient.py. They run a command to create a new VM based on the image and flavor selected by the user.

11) The command is run as a subprocess and is specific to the cloud service (i.e Openstack has a command of its own and Azure has a command of its own to create the VM)

12) Once created, either of the two cloud services responds to TCPClient.py with a "vm created" message.

# Todos
- Ensure that the respective files run properly with python3 on the respective PCs

- Understand the code and add as much comments as possible to make the code look large.
