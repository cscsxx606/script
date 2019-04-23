# coding=utf-8
#!/usr/bin/python
import  paramiko
import os,datetime
today=datetime.date.today()
yesterday=today - datetime.timedelta(days=1)
Time=yesterday.strftime('%Y%m%d')
File='fee_2019011100001_%s.txt.OK' %Time
host='192.168.50.1'
port=20022
username='cccc'
password='bbbb'
locadir='/Users/admin/python/'
remotedir='./'
sf=paramiko.Transport((host,port))
sf.connect(username=username,password=password)
sftp=paramiko.SFTPClient.from_transport(sf)
for  i in sftp.listdir(remotedir):
    print i
    if  i in File:
         sftp.get(remotedir+i,locadir+i)
sf.close()