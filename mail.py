# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import json 	
import configparser

config = configparser.ConfigParser()
config.readfp(open('config.ini'))
#linux服务器 定时任务 需要用绝对路径
#config.readfp(open('/home/gdhelper/config.ini'))
mail_ssl = config.get("Mail","ssl")
mail_server = config.get("Mail","server")
mail_port = config.get("Mail","port")



#发送账号配置
sender = config.get("Mail","sender")
senderAccount = config.get("Mail","senderAccount")
senderPassword = config.get("Mail","senderPassword")
#接收方账号配置
receivers = config.get("Mail","receivers").replace('[',"").replace(']',"").split(',')
#receivers = ['im@program.dog']
 
#邮件模板
MailTitleTpl = '不思议迷宫:每日密令'
MailContentTpl = '今天的每日密令是 {0}'
#测试模式 只显示log 不发送
DEBUG_MODE = False


	
#发信
def SemdMail( _json):
	server = smtplib.SMTP() 
	server.connect('smtp.163.com',25)  
	server.login(senderAccount,senderPassword)
	for recv in receivers:
		print(recv)
		try:
			message = MIMEText(MailContentTpl.format(_json['message']), 'plain', 'utf-8')
			message['From'] = sender
			message['To'] =  recv
			message['Subject'] = MailTitleTpl;
			if DEBUG_MODE == False:
				server.sendmail(sender,recv,message.as_string()) 
			print("send success") 
		except smtplib.SMTPException:
			print("send fail")
			
	server.quit()
	return