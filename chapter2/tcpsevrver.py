import socket
import threading
bing_ip = '0.0.0.0'
bing_port = 12138
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bing_ip,bing_port))
server.listen(5)    #最大连接数 
print ("[*] listen on %s:%d" % (bing_ip,bing_port))
def handle_client(client_socket):   #客户端处理进程
    request = client_socket.recv(1024)    
    print ("[*] Received: %s" % request)   #接受类型并打印
    client_socket.send(str.encode('ACK!'))
    client_socket.close()
while True:
    client,addr = server.accept()
    print ("[*] Accepted connection from: %s:%d" % (addr[0],addr[1]))
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()