# encoding: utf-8
__author__ = 'lianggao'
__date__ = '2018/7/25 上午11:27'

import smtplib
import datetime
import logging
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class emailSender(object):
    def __init__(self):
        self.smtp_host = "smtp.126.com"      # 发送邮件的smtp服务器（从QQ邮箱中取得）
        self.smtp_port = 465                # smtp服务器SSL端口号，默认是465


    def sendEmailWithAttr(self, kindleEmail, kindleAuthEmail, kindleAuthPwd):
        '''
        发送邮件
        '''
        logging("sendEmailWithAttr:::\nkindleEmail: " + kindleEmail + "\nkindleAuthEmail: " + kindleAuthEmail + "\nkindleAuthPwd: " + kindleAuthPwd)
        message = MIMEMultipart()  # 邮件内容，格式，编码
        message['From'] = kindleAuthEmail             # 发件人
        message['To'] = kindleEmail             # 收件人列表
        message['Subject'] = "Convert"                # 邮件标题
        filename = './txt/哲学的慰藉-阿兰德波顿.mobi'
        with open(filename, 'rb') as f:
            attachfile = MIMEApplication(f.read())
        filename = "哲学的慰藉-阿兰德波顿.mobi"
        attachfile.add_header('Content-Disposition', 'attachment', filename=filename)
        encoders.encode_base64(attachfile)
        message.attach(attachfile)
        try:
            smtpSSLClient = smtplib.SMTP_SSL(self.smtp_host, self.smtp_port)   # 实例化一个SMTP_SSL对象
            loginRes = smtpSSLClient.login(kindleAuthEmail, kindleAuthPwd)      # 登录smtp服务器
            logging(f"登录结果：loginRes = {loginRes}")    # loginRes = (235, b'Authentication successful')
            if loginRes and loginRes[0] == 235:
                logging(f"登录成功，code = {loginRes[0]}")
                smtpSSLClient.sendmail(kindleAuthEmail, kindleEmail, message.as_string())
                logging(f"mail has been send successfully. message:{message.as_string()}")
                return True
            else:
                logging(f"登陆失败，code = {loginRes[0]}")
                return False
        except Exception as e:
            logging(f"发送失败，Exception: e={e}")
            return False
