import threading
import paramiko
import subprocess
def ssh_command(ip, user, passwd, command):
    client = paramiko.SSHClient()
    #clien.load_host_keys('') 使用秘钥来进行验证 单引号中间是秘钥存放位置
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #自动添加和保存服务器秘钥
    client.connect(ip, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        print (ssh_session.recv(1024))
    return
ssh_command('192.168.6.6','root','roothake','id')