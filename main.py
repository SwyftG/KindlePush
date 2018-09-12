# encoding: utf-8
__author__ = 'PeekPaCodeWorld'
__date__ = '2018/6/10 上午11:40'

import tornado.ioloop
import tornado.web
import os
from tornado.options import define, options
from common.url_router import include, url_wrapper


class Application(tornado.web.Application):
    def __init__(self):
        # initdb()
        handlers = url_wrapper([
            (r"/json/", include('views.json.json_urls')),
            (r"/web/", include('views.web.web_urls')),
            (r"/wx/", include('views.wx.wx_urls')),
        ])
        # 定义tornado服务器的配置项，如static/templates目录位置，debug级别等
        settings = dict(
            debug=True,
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "templates")
        )
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    print("Tornado server is ready for service\r")
    tornado.options.parse_command_line()
    Application().listen(8000, xheaders=True)
    tornado.ioloop.IOLoop.current().start()