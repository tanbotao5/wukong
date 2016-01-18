#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import random
import hashlib
import requests
import json
import traceback



WUKONG_JSON_HEADER = {'content-type': 'application/json',"Authorization":""}
WUKONG_URL = '''https://sandbox-wkapi.laiwang.com/v1/'''
WUKONG_Authorization = '''Wukong nonce=%s, domain="reindeerSO", timestamp=%s, signature_method="sha1", version="1.0", signature=%s'''

domain = 'your dimain'       #网站自取
appToken  = 'your appToken'  #网站自取

class ChatHandler:
      def __init__(self):
            pass

      #生成nonce, timestamp,signature
      def getSignature(self):
            nonce  = repr( random.randint(1,10000))
            timestamp = repr(int(time.time()))
            signature  = reduce(lambda x,y :x + y,sorted( [appToken,nonce,timestamp]))   #对三个值排序 求和  sha1加密.
            return nonce, timestamp,hashlib.sha1(signature).hexdigest()


      #发送请求使用标准https协议。创建会话请求
      #data = {"openId": 18210919572, "type": 1, "icon":"","title":"test","members": [13691127476,],\
      #          "tag":122,"extension":{},"memberLimit":500,"superGroup":1,}

      def creatSessionRequest(self,data):              
	  try:
                WUKONG_JSON_HEADER['Authorization'] = WUKONG_Authorization % self.getSignature()
                url = WUKONG_URL + 'im/conversation/create'
                reponse = requests.post( url,data = json.dumps( data ), headers = WUKONG_JSON_HEADER, auth = '')
                if reponse.status_code == requests.codes.ok:
                       return json.loads(reponse.text)
                else:
                        return json.loads(reponse.text)

          except:
                  print traceback.format_exc()
                  pass


      #包括同步、更新用户profile、查询用户profile、批量查询用户profile
      #data = {"avatar":"","birthday":651337200000,"gender":1,"isActive":true,"nick":"tianpeng", \
      #          "nickPinyin":"testpinyin","openid":11111,"ver":1}

      def addOrUpdateUserInfo(self,data):               
	  try:
                  WUKONG_JSON_HEADER['Authorization'] = WUKONG_Authorization % self.getSignature()
                  url = WUKONG_URL + 'user/profile/update'
                  reponse = requests.post( url,data = json.dumps( data ), headers = WUKONG_JSON_HEADER, auth = '')
                  if reponse.status_code == requests.codes.ok:
                        return json.loads(reponse.text)
                  else:
                        return json.loads(reponse.text)

          except:
                  print traceback.format_exc()
                  pass

      #查询用户 profile
      #data = {"avatar":"","birthday":651337200000,"gender":1,"isActive":true,"nick":"tianpeng","nickPinyin":"testpinyin",\
      #         "openid":11111,"ver":1}
      def getUserInfo(self,openId):               
	  try:
                  WUKONG_JSON_HEADER['Authorization'] = WUKONG_Authorization % self.getSignature()
                  url = WUKONG_URL + "user/profile/get?openId=" + repr(openId)
                  reponse = requests.get( url, headers = WUKONG_JSON_HEADER, auth = '',verify=True)
                  if reponse.status_code == requests.codes.ok:
                        #return reponse.text
                        return json.loads(reponse.text)
                  else:
                        #return reponse.text
                        return json.loads(reponse.text)

          except:
                  print traceback.format_exc()
                  pass

      #批量查询会话信息
      #conversationIds=[]会话的id列表  data={"openId":18210919572，"conversationIds": ["13691127476:18210919572"]}
      def getSessionsInfo(self,data):               
	  try:
                  WUKONG_JSON_HEADER['Authorization'] = WUKONG_Authorization % self.getSignature()
                  url = WUKONG_URL + "im/conversations/get"
                  reponse = requests.post( url,data = json.dumps( data ), headers = WUKONG_JSON_HEADER, auth = '',verify=True)
                  if reponse.status_code == requests.codes.ok:
                        #return reponse.text
                        return json.loads(reponse.text)
                  else:
                        #return reponse.text
                        return json.loads(reponse.text)

          except:
                  print traceback.format_exc()
                  pass


      # 单个用户消息推送
      #data = {"notifyModel":{"alertContent":"push test message","badge":3,"params":{},"sound":"cat.wav","timeToLive":10}, \
      #          "pushModel":{"content":"","toWeb":false,"type":1},"receiverId":100071}
      def pushUserInfo(self,data):              
	  try:
                  WUKONG_JSON_HEADER['Authorization'] = WUKONG_Authorization % self.getSignature()
                  url = WUKONG_URL + "push/message/user"
                  reponse = requests.post( url,data = json.dumps( data ), headers = WUKONG_JSON_HEADER, auth = '',verify=True)
                  if reponse.status_code == requests.codes.ok:
                        #return reponse.text
                        return json.loads(reponse.text)
                  else:
                        #return reponse.text
                        return json.loads(reponse.text)

          except:
                  print traceback.format_exc()
                  pass

      #短信邮件发送消息
      #会话好友没有安装应用时，可以通过短信邮件发送聊天消息
      #'data = {"openId":18210919572,"openIds":[18210919572,13691127476],"contacts":["18210919572","13691127476"],\
      #          "conversationId":"13691127476:18210919572","type":1,"messageId":914541627}
      def pushUserCMSInfo(self,data):              
	  try:
                  WUKONG_JSON_HEADER['Authorization'] = WUKONG_Authorization % self.getSignature()
                  url = WUKONG_URL + "im/message/sms/notice"
                  reponse = requests.post( url,data = json.dumps( data ), headers = WUKONG_JSON_HEADER, auth = '',verify=True)
                  if reponse.status_code == requests.codes.ok:
                        #return reponse.text
                        return json.loads(reponse.text)
                  else:
                        #return reponse.text
                        return json.loads(reponse.text)

          except:
                  print traceback.format_exc()
                  pass

      #发送消息
      #data={"content":{"contentType":"TEXT","text":"Are you hello world"},"priority":0,"msgType":"SELF",\
	                "conversationId":"13691127476:18210919572","senderId":18210919572,"extension":{"foo" : "bar"},\
			"XpnParam":{"incrbadge" : 1,"alertContent":"alert content","XpnOff":0,\
			"params":{"key1":"value1","key2":"value2","key3":"value3"}},"tag":121}
      def sendUserMessage(self,data):              
      	  try:
                  WUKONG_JSON_HEADER['Authorization'] = WUKONG_Authorization % self.getSignature()
                  url = WUKONG_URL + "im/message/send"
                  reponse = requests.post( url,data = json.dumps( data ), headers = WUKONG_JSON_HEADER, auth = '',verify=True)
                  if reponse.status_code == requests.codes.ok:
                        #return reponse.text
                        return json.loads(reponse.text)
                  else:
                        #return reponse.text
                        return json.loads(reponse.text)

          except:
                  print traceback.format_exc()
                  pass





