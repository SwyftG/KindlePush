# encoding: utf-8
__author__ = 'PeekPaCodeWorld'
__date__ = '2018/6/10 上午11:43'
import tornado.web
import pymongo
import datetime
import json

class JsonHandle(tornado.web.RequestHandler):
    def get(self):
        self.client = pymongo.MongoClient("mongodb://39.11.12.123/", 27017)
        self.db = self.client["DailyProject"]
        self.table = self.db["table"]
        result = self.table.find()
        time = datetime.datetime.now()
        cur_time = str(time.year) + "-" + str(time.month) + "-" + str(time.day)
        temp_posts = []
        posts = []
        for item in result:
            temp_posts.append(item)
            temp_posts.sort(key=lambda k: (k['post_time'][-5:]), reverse=True)
        for item in temp_posts:
            if item['post_day_time'] == cur_time:
                posts.append(item)
        return_data = []
        for item in posts:
            temp_dic = {'postId': item['post_id'], 'postTitle': item['post_title'],
                        'postPartUrl': item['post_part_url']}
            return_data.append(temp_dic)
        self.write(json.dumps({"data": {"block": return_data, "curTime": cur_time}}))