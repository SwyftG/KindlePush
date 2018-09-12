这次文章为什么这么慢？是因为上周铲屎官独自撇下皮克啪，飞去日本给女朋友过18岁生日，浪了几天，啊哈哈哈哈。
![](https://mmbiz.qpic.cn/mmbiz_png/jA4Qc7C9IZSibpC8t2gpRnUYmDllyuZ92kv0QYkfezMYYr5tBpk8lHxWEnwMUp4RLdCOKTLCiaxsNBarJQdP3kcA/0?wx_fmt=png)

**这几天明显，北京的会开完了，空气质量，呵呵，呵呵呵呵。**

那么这期我们来聊一聊外快的事儿。有kindle的同学，肯定了解，如果想看kindle的电子书，一般来说有这么几个渠道：
1. **去kindle官网买，支持正版，但是书籍很贵，偶尔有打折的时候，打折也不便宜。土豪可以选择这条路。**
2. **去网上自己下载下来电子书，然后倒入到自己的kindle。这种方式一般对于不爱用电脑的同学来说，挺技术的，所以爱动手的同学可以选择这个。**
3. **最后一种就是去某宝或者去找一些公众号，他们那里提供书籍的下载，有偿的无偿的都有，而且，是推送的方式。这条路径几乎对所有人适用，而且很方便。**

当时买了Kindle，我也是通过第三种方式来找书的，记得当时找了一个公众号，搜了些书，推送到Kindle上，就觉得炒鸡方便，但是后来那个公众号暂停服务了，之后又换了几个公众号，都不是很稳定，但是他们都有一个共同的特点，就是需要自己手动绑定一下邮箱。个人感觉，这个步骤似乎对没有电子智商的人来说，非常不友好，于是有的公众号就开通了专属客服，教你怎么绑定。整体而言，大家的流程都差不多，但是由于自己是个码农，出于职业上的好奇心，很想知道他们这些人是怎么搞的。所以就在网上谷歌，发现，推送最多的文章就是用KindleEar来做，但是这个东西是和google app engine契合在一起的，对于国内的童鞋，很是不友好。记得我在搜索的过程中，还发现有那种大神，每天爬取知乎热文，公众号文章之类的热点行文，然后自己整合一下，每天固定5点推送到kindle上，下了班在地铁上自己阅读。这其实是个很牛叉的做法，利用碎片化的时间来摄取知识，很强。可惜这个文章没说怎么做的。由此两点，铲屎官决定，靠天靠地不如靠自己，自己潜心修炼，势要打通此脉。果然，通过自己对Python的不断深入学习，慢慢的打通了所有节点，可以很轻松的完成这个任务了，啊哈哈哈哈。

**那么今天，铲屎官就来和大家捯饬捯饬这上面说的第三种方法**，给大家提供一下思路，和具体实现方法。做的好了，可以有偿帮助别人找书啊，比如一块钱十本书，不求多赚，只求平衡个电费而已，毕竟，你只是搬运工。

**废话不多说，下面我们就来说说细节。**


### 整体思路

拿到一个问题，我们首先就得来分析一下，这个问题由那几部分组成，这几个部分怎样做比较好。

Kindle推送服务器，大致可以分为两部分：找书和推送。

找书的过程我这里先不过多说，关键的技术点可以参考这几篇文章：
[【Python实战】用代码来访问1024网站，送福利](https://mp.weixin.qq.com/s?__biz=MzI2ODYwNjE5NQ==&mid=2247483753&idx=1&sn=8df6c2a190201826f6f860659ad4af9e&chksm=eaec4ef5dd9bc7e39e8d48134795f6c0173c4614c615d0dcaaa38d937f4394aee77a978d70b1&token=607075502&lang=zh_CN#rd)   
[【Python实战】用代码在1024论坛实现自动回贴](https://mp.weixin.qq.com/s?__biz=MzI2ODYwNjE5NQ==&mid=2247483846&idx=1&sn=120fd8452e2e8c465b424296853d40c9&chksm=eaec4e5add9bc74c0690541530f68d5e993e4afeebd535ea66e597141f10dd3f2bef82468355&token=607075502&lang=zh_CN#rd)

接下来我们来详细的说一下服务器推送的问题。推送的流程应该大致是这样的：
- 首先通过微信公众号来绑定用户的推送Kindle信息：Kindle的账户邮箱，Kindle已经认可的发件人邮箱，Kindle认可的发件人邮箱的STMP密码。
- 通过微信公众号发送搜搜书名，然后可以查找到相关书籍。
- 服务器通过之前绑定的账号，来实现Kindle的电子书推送。
- 大约10分钟的时间，电子书被推送到了Kindle上面，就可以愉快的看书喽。

大概就是这么几点，其实，看到这里，如果你是铲屎官的忠实读者，那么我说的这几点，其实在我之前的系列文章里面，关键的知识点都陆陆续续的详细的说过了，铲屎官在这里结合代码再帮大家捋一捋。

>整套服务器代码我已经部署到了阿里云上，铲屎官手头有一些阿里云和腾讯云的优惠券，非常实惠，便宜力度很大，如果自己玩服务器的话，一年300多的服务器不到200就可以拿下来。可以通过下面的链接领取，数量有限，先到先得：
> 
>**阿里云（总价值千元代金券）：**  
>*https://promotion.aliyun.com/ntms/yunparter/invite.html?userCode=nrkmbo9q*  
>**腾讯云（总价值高达2775元代金券）：**  
>*https://cloud.tencent.com/redirect.php?redirect=1025&cps_key=b351b2fc50b15866ff9d19b58a5df0f5*


首先，我们来先说一下这个通过微信公众号来绑定用户信息的事儿。

#### WeRobot

微信公众号开发，我首先推荐使用WeRobot框架，这个框架是对微信公众号官方开发文档里面提到的东西进行了一次封装，非常的好用，具体想了解更多的同学且有一定编程开发基础的同学，可以去看WeRobot的官方文档：

*https://werobot.readthedocs.io/zh_CN/latest/*

我们在这里需要用户绑定账号的场景，就是用到了WeRobot里面的Session。官方文档在下面：

*https://werobot.readthedocs.io/zh_CN/latest/session.html*

WeRobot的Session其实就是讲每一个账号的信息保存到了一个数据库中，默认会在服务器本地文件夹下面创建一个`werobot_session.sqlite3`文件，里面通过`键值对`的形式来存储数据。下面的代码是在Kindle项目中运用到的session示例：

```
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

```

可以看到，我这里是通过一个count变量来控制文本信息的处理的。每一个用户，当输入特定的关键字`kinle`，就会进入指定的处理逻辑里面。然后通过count的变化，来控制不同的处理逻辑，同时，将用户输入的相关文本信息，再保存到session字典中。WeRobot会自动将信息更新到数据库中。

> 这里说几点可以发挥的地方：
> 1. 可以检测用户输入的信息是否合法，比如需要输入邮箱的时候，输入的文本结构是否是合法的邮箱。
> 2. 可以在自己Debug的时候，添加一些特殊的文字表示，用来打印自己需要的信息，比如添加`session`，用来打印自己的session信息，就如下：
> ![](https://mmbiz.qpic.cn/mmbiz_png/jA4Qc7C9IZSibpC8t2gpRnUYmDllyuZ92Zhnn5iaPVYmQdhM20JTGwibE64Ebe1sCBdtU8SL2KpBk1131Iy9FLghA/0?wx_fmt=png)

那么到这里，我们的第一步就完成了，最后大致效果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/jA4Qc7C9IZSibpC8t2gpRnUYmDllyuZ925aicqOyhbndnoTUpgvQkP1X7k5aHqCSES1TNHlHVd9cb90NGxtCtKrw/0?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/jA4Qc7C9IZSibpC8t2gpRnUYmDllyuZ92nFnh4CpWeKKXqd3SakOibMldwYZicT0O7StAaL4PvIyR5qSEQib9rIFZA/0?wx_fmt=png)

OK，这里我们就把微信公众号这块的代码逻辑捋清楚了。那么接下来我们得看，发送书籍的代码应该怎么搞。

#### 发送.mobi文件

这里需要通过Python来发送邮件。首先，我们得先了解一下如何通过发邮件的形式来把`mobi`文件发送到kindle上。这里，kindle的官方文档有很详细的说明：

![](https://mmbiz.qpic.cn/mmbiz_png/jA4Qc7C9IZSibpC8t2gpRnUYmDllyuZ92SvnUmr7NRFiaTDMHQHTwibCamX5XbgeKiaK20L0yiahHxvwVPtdNOvQZYw/0?wx_fmt=png)  
*https://www.amazon.cn/gp/help/customer/display.html/ref=kinw_myk_wl_ln?ie=UTF8&nodeId=200767340#pdocarchive*

![](https://mmbiz.qpic.cn/mmbiz_png/jA4Qc7C9IZSibpC8t2gpRnUYmDllyuZ92nWtmTAMgOBaotbkXvib4QeHtGicRsa1fkh7w8utxyOQZ2uwtXGZExRBQ/0?wx_fmt=png)  
*https://www.amazon.cn/gp/help/customer/display.html?nodeId=201974220*

这里需要注意的就是，如果想要成功发送mobi文件到Kindle上，有两点要求：
1. 发送文件的邮箱必须是在Kindle的认可电子邮件列表里的邮箱。
2. 邮件的主题必须是“Convert”

所以，我们这里只需要，把找到的书籍，把书籍文件作为邮件的附件，邮件的标题是“Convert”，通过Kindle认证的邮箱，发邮件到Kindle账户邮箱。这样就完成了书籍的推送。是不是超级简单？

所以，这里我们先略过找书的过程，相关技术点请参考文章[1](1)。我们就把现成的书籍通过邮件的形式发送到Kindle上。细心的同学看到我上面的微信公众号代码里面有一行`send_result = emailSender().sendEmailWithAttr(session['kindle_email'], session['kindle_auth_email'],session['kindle_auth_pwd'])`没错，这个就是发送邮件的方法调用。那么这个`emailSender()`的代码就是长这个样子：
```
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
        filename = './txt/哲学的慰藉-阿兰德波顿.mobi'    # 本地书籍
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
```

可以看到，上面的代码就是将Subject填写Convert，然后将mobi书籍当附件的形式发送出来，就可以了。这个发送邮件的过程，和“1024种子吞噬器V2.0”版本很像，参考文章： 
 [【Python实战】带你玩转Scrapy的高阶骚操作，带邮件功能的“1024种子吞噬器2.0”，更高更快更强！千元福利等你取](https://mp.weixin.qq.com/s?__biz=MzI2ODYwNjE5NQ==&mid=2247484026&idx=1&sn=ed3c40355f386ffb2692c3cf02da96a0&chksm=eaec4de6dd9bc4f0a08ece7292a30ba0e60d2cad72889c8b266fcb46667c85f0295cca6babaf&token=607075502&lang=zh_CN#rd)

下面铲屎官就给大家演示一下整个是流程：

首先是公众号绑定：

![](https://mmbiz.qpic.cn/mmbiz_png/jA4Qc7C9IZSibpC8t2gpRnUYmDllyuZ92z7LQR0YnibeFFe1Hp4QQAHicpFdclPy2QkrVTtRjdzTGYY7azcKqxOQw/0?wx_fmt=png)

接着就是绑定成功，开始而且显示的发书也成功：

![](https://mmbiz.qpic.cn/mmbiz_png/jA4Qc7C9IZSibpC8t2gpRnUYmDllyuZ92ZcmQlQdu2GjFBRcvdPh6FAorFjgEnJBBYqPVbBkfHDXtERNiaXPib1dA/0?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/jA4Qc7C9IZSibpC8t2gpRnUYmDllyuZ92eVIe4SuNThs8aicLRMsYnkH6ibQqdeN5JyYAiadAPiakgAIGrH3LvbsKXg/0?wx_fmt=png)
那么我们来看一下自己的Kindle：

![](https://mmbiz.qpic.cn/mmbiz_png/jA4Qc7C9IZSibpC8t2gpRnUYmDllyuZ92Tiaouv2AVXkTaK6kMWKABv2mLxkKkicQ2PVIFsvicfrFlDYianDpwtOMcA/0?wx_fmt=png)

欧耶，一切搞定。这套流程完美跑通。其实，这只是一半的过程，剩下还有一半，我们下回再说，但是你也可以自己先研究研究。这些小玩意儿其实都是可以带来小额收益的，不吹牛逼。

### 简单总结

这里就简单的总结一下，说几点比较关键的地方：
1. *发送邮箱的绑定过程，这里只是绑定了126的邮箱，其实不同的邮箱他的STMP端口是不一样的，而且STMP服务器地址也是不一样的，这里需要做一下判断。*
2. *这里只是发送书籍的过程，其实应该在书籍搜索，返回书籍的搜索结果，然后让用户选择下载哪本书。下载书籍我目前想到的方式就是先下载到服务器上，然后才能通过附件的格式发送出去，最后需要执行以下删除操作。*
3. *其实这个功能可以玩的花活很多，不光发送书籍这么简单，也可以指定订阅比如1024Daily页面啊，每天都发送到Kindle上，或者喜欢哪个系列的技术讨论区的帖子，可以每天发送到自己的Kindle上。可以玩的方向有很多，等待大家自己去挖掘。*

感谢你能够容忍铲屎官唠叨这么多碎碎的知识点，那么我也不会亏待你，这个服务器我是用tornado编写的，整套代码我已上传，获取源码方式只需要关注『***皮克啪的铲屎官***』，回复『***代码***』即可获得。回复内容保你满意。

**下一步的计划，我今天觉得Daily项目有可以改进的地方，所以，下一步可能会加入一个集合的功能，啊哈哈哈哈，这样就越来越方便了。啊哈哈哈哈**

#### 推荐阅读
[一篇文章就够打通python网络请求，scrapy爬虫，服务器，代理，各种骚操作，真的一篇就够](https://mp.weixin.qq.com/s?__biz=MzI2ODYwNjE5NQ==&mid=2247484047&idx=1&sn=80cedd762ee7a9d6f60e0e5007183a91&chksm=eaec4d13dd9bc40568d55c8b35450d125f815d116d93ef28717077cc4f64e941c36b21dd1e92&token=607075502&lang=zh_CN#rd)  
[手把手用阿里云服务器搭建袜子工具，从此不再求人，内有福利](http://mp.weixin.qq.com/s?__biz=MzI2ODYwNjE5NQ==&mid=2247483979&idx=1&sn=432a355963fddc93a85de3373f849758&chksm=eaec4dd7dd9bc4c1c78b9d7387c854ab1569eb2e6d9d6e5e8db5da9e32098d8a9546ded9795c#rd)  
[【Python实战】通过“酸酸”的骚操作，让Scrapy爬虫变得没有国界，真正的硬核为所欲为，想爬啥就爬啥](https://mp.weixin.qq.com/s?__biz=MzI2ODYwNjE5NQ==&mid=2247484038&idx=1&sn=768da89e6b95654148600741c000a567&chksm=eaec4d1add9bc40c58a7d7da9c33725d3eb152b7f6e3ff55d5f1915a8295b120cf92d037e5e6&token=607075502&lang=zh_CN#rd)


**粉一波自己的小程序**  
![](https://mmbiz.qpic.cn/mmbiz_jpg/jA4Qc7C9IZSibpC8t2gpRnUYmDllyuZ926xFlv0g1Kk0aib2Fuhtp6w2OgYyvOXlX10Oibz5ce3Da92gia0qSf8rYQ/0?wx_fmt=jpeg)

**这么硬核的公众号，还不关注一波啊？**  
![](https://mmbiz.qpic.cn/mmbiz_jpg/jA4Qc7C9IZSibpC8t2gpRnUYmDllyuZ928Y6LkjIOVAwgdKqRFzMQZYqc77c1qJev6ypR3HWJuLniaLPJK3pbrhQ/0?wx_fmt=jpeg)
