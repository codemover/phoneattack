#!/usr/bin/python
#coding:utf-8
#codemover-gx

import os
import logging
import logging.handlers

LOG_MAXBYTES = 1024*1024
LOG_BACKUPCOUNT = 5
LOG_PATH = '../log/analyzelog/'

def create_log(fileName,logMsg):
  global LOG_MAXBYTES

  if(os.path.exists(LOG_PATH) == False):
    command = 'mkdir -p ' + LOG_PATH
    os.system(command)

  logFileName = LOG_PATH + fileName
  handler = logging.handlers.RotatingFileHandler(logFileName, maxBytes = LOG_MAXBYTES, backupCount = 5) # 实例化handler
  #fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
  #formatter = logging.Formatter(fmt)          # 实例化formatter

  logger = logging.getLogger('analezelog')    # 获取名为tst的logger
  logger.addHandler(handler)                  # 为logger添加handler
  logger.setLevel(logging.INFO)

  logger.info(logMsg)
  #logger.debug(logMsg)
