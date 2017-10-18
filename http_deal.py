#!/usr/bin/python
#coding:utf-8

import os
import sys
import urllib
import urllib2
import json

from common_data import *

#构造http请求函数
def Get_Data_ByHttp(url,postData,postType,headers):

  if(postData == ""):
    #get请求
    req = urllib2.Request(url)

    resp = urllib2.urlopen(req)
    respData = resp.read()

    return respData

  else:
    #post 请求
    headers = {}

    if(postType == POST_BYJSON):
      headers = { 'Content-Type': 'application/json','Accept': 'application/json'}
      req = urllib2.Request(url,json.dumps(postData),headers)
      resp = urllib2.urlopen(req)
      respData = resp.read()

      #print 'respDataByJson',respData
      return respData

    else:
      strPostData = str(postData)
      print 'PostData:',strPostData
      print 'Header:',headers

      req = urllib2.Request(url,urllib.urlencode(postData),headers)
      resp = urllib2.urlopen(req)
      respData = resp.read()

      print 'respDataByNOJson',respData
      return respData

