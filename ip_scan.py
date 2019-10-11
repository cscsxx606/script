#-*-coding:UTF-8-*-
import  nmap
import  os
import  smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
DIR="/opt/scripts"
ip_list=open("iplist.txt",'r')
nm=nmap.PortScanner()
open_port=open('open_port.txt','w')
for  i in ip_list.readlines():
    ip=i.strip()
    nm.scan(ip,'0-65535')
    for  host in nm.all_hosts():
        open_port.write('##############################################\n')
        open_port.write("Host:%s\n" %(host))
        #print ('State:%s'% nm[host].state())
        for  proto  in nm[host].all_protocols():
            open_port.write('Protocol:%s\n' % proto)
            iport=nm[host][proto].keys()
            #print (iport)
            #iport.sort()
            for port  in iport:
                #print (port)
                open_port.write('port:%s\tstate:%s\n' % (port, nm[host][proto][port]['state']))
open_port.close()
#发送邮件
port_file=open('open_port.txt','r').read()
mail_namelist = ["xxx@xxx.com"]
mail_user = ""
mail_pass = ""
mail_subject = "IDC外网IP端口扫描"
mail_context = port_file
def send_main():
        msg = MIMEMultipart()
