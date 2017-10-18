#!/usr/bin/python
#coding:utf-8

import os
import sys

#POST形式
POST_BYJSON = 0
POST_BYNOJSON = 1 

#网站标识
WEIPINHUI = 0
ZHUBAJIE = 1

#网站标识数组
g_web_pool = [ZHUBAJIE]

#URL池
g_url_pool = {}
g_url_pool[WEIPINHUI] = 'https://passport.vip.com/register/send_phone_verify'
g_url_pool[ZHUBAJIE] = 'https://login.zbj.com/register/sendRegisterCode'

#公共请求头
g_common_headers = {}
g_common_headers['Accept'] = 'application/json, text/javascript, */*; q=0.01'
#headers['Accept-Encoding'] = 'text'
g_common_headers['Accept-Language'] = 'zh-CN,zh;q=0.8'
g_common_headers['Connection'] = 'keep-alive'
g_common_headers['Content-Type'] = 'application/x-www-form-urlencoded'
g_common_headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'

#不同网站的POST数据
g_post_data = {}
##唯品会
g_post_data[WEIPINHUI] = {}
g_post_data[WEIPINHUI]['phone'] = '18704250528'

##猪八戒
g_post_data[ZHUBAJIE] = {}
#g_post_data[ZHUBAJIE]['sacc'] = '18704250528'
g_post_data[ZHUBAJIE]['captcha'] = '' #验证码
g_post_data[ZHUBAJIE]['seed'] = '1508227858984'
