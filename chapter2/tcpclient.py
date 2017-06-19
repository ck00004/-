import socket
target_host = "www.baidu.com"
target_port = 80
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target_host,target_port))
aaa = "GET / HTTP/1.1\r\nHost:baidu.com\r\n\r\n"
client.send(str.encode(aaa))  #这里只需要注意 send在python3中 接收的是 bytes 只需要做一个转换就好
response = client.recv(4096)
print (bytes.decode(response))