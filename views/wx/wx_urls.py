# encoding: utf-8
from emailUtil import emailSender

__author__ = 'lianggao'
__date__ = '2018/6/1 上午11:08'

import datetime
from werobot import WeRoBot
from werobot.contrib.tornado import make_handler
import re

robot = WeRoBot(token="你的token")

urls = [
    (r'reply', make_handler(robot))
]
debug_list = []
exception_list = []
info_message = []


@robot.filter('kindle')
def replyKindle(message, session):
    count = session.get("kindle_count", 0)
    email = session.get("kindle_auth_email", "")
    if email is "":
        session["kindle_count"] = count + 1
        return "输入Kindle邮箱："
    else:
        return "请输入要找的书名："

@robot.filter("重新绑定")
def printSeesino(message, session):
    session['kindle_count'] = 1
    session['kindle_email'] = ""
    session['kindle_auth_email'] = ""
    session['kindle_auth_pwd'] = ""
    return "解绑成功！\n请重新输入Kindle邮箱："


@robot.filter("session")
def printSeesino(message, session):
    return "session: " + str(session)

@robot.filter(re.compile('找书：'))
def replayHuitie(message, session):
    return findBook(message, session)


def findBook(message, session):
    if session['kindle_count'] != 4:
        return "请绑定Kindle账号，再来找书。"
    book_name = message.content[3:]
    if book_name is "":
        return "老铁你输入的书名有误，请重新输入。"
    else:
        ### 找书的过程
        # find_result = find_book()
        find_result = True
        if find_result is True:
            ### 发送书籍的函数方法
            # send_result = send_book()
            # send_result = send_book()
            send_result = emailSender().sendEmailWithAttr(session['kindle_email'], session['kindle_auth_email'],
                                                          session['kindle_auth_pwd'])
            if send_result is True:
                return "老铁你找书的内容：《" + book_name + "》\n后台已经成功给您发送，请您10分钟之内注意查收。感谢使用。"
            else:
                return "抱歉，老铁要的书发送失败，请重新试试。"
        else:
            return "抱歉，老铁要的书未能找到，请试试其他的书籍？"


@robot.handler
def restReply(message, session):
    count = session.get("kindle_count", 0)
    print(message.content + " count: " + str(count))
    if count == 1:
        session["kindle_count"] = count + 1
        session["kindle_email"] = message.content
        return "请输入Kindle认证邮箱："
    if count == 2:
        session["kindle_count"] = count + 1
        session["kindle_auth_email"] = message.content
        return "请输入认证邮箱的密码："
    if count == 3:
        session["kindle_count"] = count + 1
        session["kindle_auth_pwd"] = message.content
        return "绑定成功！\n你的Kindle邮箱地址：" + session['kindle_email'] \
               + "\nKindle认证邮箱地址：" + session['kindle_auth_email'] + "\n认证邮箱密码：" \
               + session['kindle_auth_pwd'] + "\n如果需要重新绑定，回复『重新绑定』即可。\n现在你可以找书啦，回复『找书： + 书名』即可，例如『找书：金鳞岂是池中物』"
    if count == 4:
        if "找书：" in message.content:
            findBook(message, session)
        else:
            reply = """『皮克啪的铲屎官』这么牛逼的公众号，还不关注一波啊？"""
        return reply
