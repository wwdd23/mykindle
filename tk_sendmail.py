#!/usr/bin/env python
#-*- coding:utf-8 -*-
############################
#File Name: tk_sendmail.py
#Author: wudi
#Mail: programmerwudi@gmail.com
#Created Time: 2015-06-22 10:38:18
############################



from Tkinter import *

from tkMessageBox import *

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


msg = MIMEMultipart()

def send_click():
    msg['from'] = text.get()
    msg['to'] = text_to.get()
    from_mail=msg['from']
    to_mail =msg['to']
    label_from['text'] = text.get()
    label_to['text'] = text_to.get()
    
    print msg['from']
    #print text.get()
    print msg['to']
    #print text_to.get()
    showinfo('OK','Mail send OK!')



def send_conf():
    conf=['$from_mail','$to_mail']
    f=file('sendmail.conf','w')
    f.write(conf)
    f.close()
    msg['subject'] = text_subject.get()


       

##创建一个带附件的实例
#msg = MIMEMultipart()
#
##构造附件1
#att1 = MIMEText(open('/Users/wudi/github/mykindle/51cce9cd0120c.jpg', 'rb').read(), 'base64', 'gb2312')
#att1["Content-Type"] = 'application/octet-stream'
#att1["Content-Disposition"] = 'attachment; filename="picture.jpg"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
#msg.attach(att1)
##
###构造附件2
##att2 = MIMEText(open('d:\\123.txt', 'rb').read(), 'base64', 'gb2312')
##att2["Content-Type"] = 'application/octet-stream'
##att2["Content-Disposition"] = 'attachment; filename="123.txt"'
##msg.attach(att2)
#
##加邮件头
#msg['from'] = 'wwdd.23@163.com'
#msg['to'] = 'di.wu@i-soft.com.cn'
#msg['subject'] = 'hello world'
##发送邮件
#try:
#    server = smtplib.SMTP()
#    server.connect('smtp.163.com')
#    server.login('wwdd.23','xxxxx')#XXX为用户名，XXXXX为密码
#    server.sendmail(msg['from'], msg['to'],msg.as_string())
#    server.quit()
#    print '发送成功'
#
#except Exception, e:  
#    print str(e) 
#
#

root=Tk(className='send mail to amzon')

##发件方

label_from = Label(root)
label_from['text']='change from'
label_from.pack()

text=StringVar()
text.set('From')
entry=Entry(root)
entry['textvariable'] = text
entry.pack()
entry.focus_set()




##收件方


label_to = Label(root)
label_to['text']='change to'
label_to.pack()

text_to=StringVar()
text_to.set('To')
entry_to=Entry(root)
entry_to['textvariable'] = text_to
entry_to.pack()
entry_to.focus_set()


#send_subject 


text_subject=StringVar()
text_subject.set('subject')
entry_subject=Entry(root)
entry_subject['textvariable'] = text_subject

entry_subject.pack()

##button send mail
button_send=Button(root)
button_send['text'] = 'Send'
button_send['command'] = send_click
button_send.pack()

button_exit=Button(root,text='exit',command=root.quit)
button_exit.pack()

Label(root,text="send mail to amzon").pack()



root.mainloop()
