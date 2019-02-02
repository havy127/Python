import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(s)
print("===========s==================")
server = 'google.com'
port =80

server_ip = socket.gethostbyname(server)
print(server_ip)
print("==========server_ip===================")
request = "GET / HTTP/1.1\nHost: "+server+"\n\n"

s.connect((server,port))
s.send(request.encode())
result_ = s.recv(4096)
while(len(result_) >0):
    print(result_)
    result_ = s.recv(1024)
print("===========result==================")