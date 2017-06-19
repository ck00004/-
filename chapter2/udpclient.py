import socket
target_host = '127.0.0.1'
terget_post =  12138
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto(str.encode('sdsdsdsdsdsd'),(target_host,terget_post)) #和tcp一样在这里做一个转换
data, addr = client.recvfrom(4096)
print (data)