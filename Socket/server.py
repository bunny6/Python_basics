import socket
s=socket.socket()
print("Socket createted")
s.bind(('localhost',9998))
s.listen(3)                               # deciding how many request want to have or how many clients we want
print("waiting for connections")
while True:                                # to accept request from client and work simultaneously.
    c, addr = s.accept()    
    name = c.recv(1024).decode()            
    print("Connected with:",addr,name)
    
    c.send(bytes("Welcome",'utf-8')) 
    c.close()
    
    
