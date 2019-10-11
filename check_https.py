# -*- coding:utf-8 -*-
from urllib3.contrib import pyopenssl as req
from datetime import datetime
import  yagmail
def get_domain_list():
    objlist=[]
    with open('domain.txt','r') as f:
        for  i in  f:
            objlist.append({'domain':i.split()[0],'tag':i.split()[1]})
    return  objlist
def get_expire_time(url):
    sslc=req.OpenSSL.crypto.load_certificate(req.OpenSSL.crypto.FILETYPE_PEM,req.ssl.get_server_certificate((url,443)))
    ca_date=sslc.get_notAfter().decode()[0:-1] #取出证书有效日期
    return datetime.strptime(ca_date,'%Y%m%d%H%M%S')


def send_mail(expire_list):
    user = ''
    password = ''
    # 126邮箱
    host = 'smtp.126.com'
    to = 'xxx@xxx.com'
    subject = 'ssl 证书过期告警'
    d = ''
    for i in expire_list:
        d += '''\
  <tr>
    <td align="center">''' + str(i['domain']) + '''</td>
    <td align="center">''' + str(i['remain']) + '''</td>
    <td align="center">''' + str(i['tag']) + '''</td>
  </tr>
'''
    html = '''\
<table width="70%" border="1" bordercolor="black" cellspacing="0" cellpadding="0">
  <tr>
    <td width="140" align="center" ><strong>域名</strong></td>
    <td width="110" align="center" ><strong>剩余天数</strong></td>
    <td width="110" align="center" ><strong>所属项目</strong></td>
  </tr>
'''+ d +'''</table>'''

    html = html.replace("\n", "")
    yag = yagmail.SMTP(user = user, password = password, host = host)
    yag.send(to = to, subject = subject, contents = html)
if __name__=='__main__':
    check_days=30
    domail_list=get_domain_list()
    for i in domail_list:
        remain_days=(get_expire_time(i['domain']) - datetime.now()).days
        i['remain'] = remain_days
    expire_domain_list=[i for i in domail_list if i['remain'] <= check_days]
    if (len(expire_domain_list) !=0):
        send_mail(expire_domain_list)
