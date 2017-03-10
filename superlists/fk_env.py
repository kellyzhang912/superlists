#!/usr/bin/python
#-*- coding: utf-8 -*-
import paramiko
import sys,os,time

#把打好包的风控后台的包放到服务器上，并且部署好
host = '192.168.11.199'
port = 22
username = 'MG01720'
password = 'Wss123456'

t = paramiko.Transport((host,22))
t.connect(username=username,password=password)      #连接方式也可以用key，这里只需要将password=password改为pkey=key，其余的key代码与前面的一样

sftp = paramiko.SFTPClient.from_transport(t)         #使用t的设置方式连接远程主机
#sftp.get('/Linux_SZJRDEV03_10.223 sftp (192.168.10.223)/root/opt/fkconfig','D:\\fkconfig')
#下载文件
#sftp.put('D:\\2.txt','/Linux_SZJRDEV03_10.223 sftp (192.168.10.223)/root/opt/3.txt')            #上传文件
#风控后台放包
# if os.path.isfile('C:\Users\MG01720\Downloads\project.zip'):
#     os.remove('C:\Users\MG01720\Downloads\project.zip')

sftp.put('C:\\Users\\MG01720\Downloads\project.zip','/Linux_SZJRDEV03_10.223 sftp (192.168.10.223)/root/opt/fk3/project.zip')



passinfo='password: ' #输入服务器密码的前标志串

paramiko.util.log_to_file('syslogin.log')

ssh=paramiko.SSHClient() #ssh登录堡垒机

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname=host,username=username,password=password)
channel=ssh.invoke_shell(term='xterm')  #创建会话,开启命令调用
channel.settimeout(10)      #会话命令执行超时时间,单位为秒
buff = ''
resp = ''
#channel.send('ssh '+username+'@'+hostname+'\n') #执行ssh登录业务主机
channel.send('1 '+'\n') #执行ssh登录业务主机
channel.send('3 '+'\n') #执行ssh登录业务主机
time.sleep(3)
channel.send('cd /opt/fk3'+'\n')
#channel.send('rm -rf *'+'\n')
channel.send('unzip project.zip'+'\n')
time.sleep(8)
channel.send('rm -rf /opt/fk3/project/resources/config/jdbc.properties'+'\n')
channel.send('rm -rf /opt/fk3/project/resources/config/service-config.properties'+'\n')
channel.send('cp /opt/jdbc.properties /opt/fk3/project/resources/config/jdbc.properties -f'+'\n')
channel.send('cp /opt/service-config.properties /opt/fk3/project/resources/config/service-config.properties -f'+'\n')
channel.send('cd /opt/fk3/project/'+'\n')
channel.send('chmod 777 init.sh'+'\n')
channel.send('./init.sh restart'+'\n')
time.sleep(8)
channel.close()

#




