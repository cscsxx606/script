# -*- coding:utf-8 -*-
import os,time,datetime
DB_HOST='127.0.0.1'
DB_USER='root'
DB_USER_PASSWD=' '
DB_NAME='/opt/dbname.txt'
BACKUP_PATH='/data/backup/'
DATETIME=time.strftime('%Y%m%d_%H%M%S')
TOBACKUPPATH=BACKUP_PATH + DATETIME
print ('创建备份目录')
if not os.path.exists(TOBACKUPPATH):
    os.makedirs(TOBACKUPPATH)
print ('检查数据库名文件')
def backup():
    in_file=open(DB_NAME,"r")
    for dbname in in_file.readlines():
        dbname=dbname.strip()
        print ("现在开始备份数据库 %s" %dbname)
        dumpcmd="mysqldump -h"+" " +DB_HOST +" "+ "-u" +" "+DB_USER + " " + "-p"+DB_USER_PASSWD+" " + dbname + " "+">" + " "+ TOBACKUPPATH +"/"+dbname+".sql"
        print (dumpcmd)
        os.system(dumpcmd)
    in_file.close()
def compress():
    compress_file=TOBACKUPPATH+".tar.gz"
    compress_cmd="tar -czvf " + compress_file +" " + DATETIME
    os.chdir(BACKUP_PATH)
    os.system("pwd")
    os.system(compress_cmd)
    print("压缩完成")
    remove_cmd="rm -rf" + " " +TOBACKUPPATH
    os.system(remove_cmd)
if os.path.exists(DB_NAME):
    file1=open(DB_NAME)
    print ("启动备份所有数据库备份文件列出的库" +DB_NAME)
    backup()
    compress()
