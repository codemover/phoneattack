#!/usr/bin/python
#coding:utf-8

import os
import sys

from common_data import *

#机房信息类
class CBizHostInfo:
  def __init__(self):
    self.twsIpList_LF = []
    self.twsIpList_MJQ = []
    self.appIpList_LF = []
    self.appIpList_MJQ = []

    self.appIpList_Write = [] #商品特殊拥有


  #设置廊坊机房tws docker IP列表
  def Set_TwsIpList_LF(self,iplist):
    self.twsIpList_LF = iplist

  def Set_TwsIpList_MJQ(self,iplist):
    self.twsIpList_MJQ = iplist

  def Set_APPIpList_LF(self,iplist):
    self.appIpList_LF = iplist

  def Set_APPIpList_MJQ(self,iplist):
    self.appIpList_MJQ = iplist


  #商品和金手指特殊拥有
  def Set_APPIpList_Write(self,iplist):
    self.twsIpList_Write = iplist


  #获取廊坊机房tws docker IP列表
  def Get_TwsIpList_LF(self):
    return self.twsIpList_LF

  def Get_TwsIpList_MJQ(self):
    return self.twsIpList_MJQ

  def Get_APPIpList_LF(self):
    return self.appIpList_LF

  def Get_APPIpList_MJQ(self):
    return self.appIpList_MJQ

  #商品和金手指业务特殊拥有
  def Get_APPIpList_Write(self):
    return self.appIpList_Write

#分机房宿主机列表负载信息类 -- 该类一次获取一个机房的一个服务的所有宿主机负载信息
#防止多次请求影响性能
class CMotherLoadInfo:

  def __init__(self):
    self.ipList = []
    self.cpuInfoList = []   #CPU负载信息
    self.diskInfoList = []  #磁盘负载信息
    self.timeList = [] #时间

    self.mcType = MACHINE_LF
    self.svcType = SERVICE_TWS

  def Set_IpList(self,iplist):
    self.ipList = iplist

  def Set_CpuInfoList(self,cpuInfoList):
    self.cpuInfoList = cpuInfoList

  def Set_DiskInfoList(self,diskInfoList):
    self.diskInfoList = diskInfoList

  def Set_TimeList(self,timeList):
    self.timeList = timeList

  def Set_McType(self,mcType):
    self.mcType = mcType

  def Set_SvcType(self,svcType):
    self.svcType = svcType


  def Get_IpList(self):
    return self.ipList

  def Get_CpuInfoList(self):
    return self.cpuInfoList

  def Get_DiskInfoList(self):
    return self.diskInfoList

  def Get_TimeList(self):
    return self.timeList

  def Get_McType(self):
    return self.mcType

  def Get_SvcType(self):
    return self.svcType

#分机房Docker容器负载信息类
class CDockerLoadInfo:

  def __init__(self):
    self.motherIp = ""
    self.dockerIp = ""
    self.mcType = MACHINE_LF
    self.svcType = SERVICE_TWS
    self.loadList = []   #容器负载二维数组
    self.motherCpuLoad = 0 #宿主机负载

  def Set_MotherIp(self,motherIp):
    self.motherIp = motherIp

  def Set_DockerIp(self,dockerIp):
    self.dockerIp = dockerIp

  def Set_McType(self,mcType):
    self.mcType = mcType

  def Set_SvcType(self,svcType):
    self.svcType = svcType

  def Set_LoadList(self,loadList):
    self.loadList = loadList

  def Set_MotherCpuLoad(self,motherLoad):
    self.motherCpuLoad = motherLoad

  def Get_MotherIp(self):
    return self.motherIp

  def Get_DockerIp(self):
    return self.dockerIp

  def Get_McType(self):
    return self.mcType

  def Get_SvcType(self):
    return self.svcType

  def Get_LoadList(self):
    return self.loadList

  def Get_MotherCpuLoad(self):
    return self.motherCpuLoad

#告警信息类
class CWarnMsgInfo:

  def __init__(self):
    self.time = ""
    self.timestamp = 0
    self.status = STATUS_RECOVER
    self.bizId = BIZID_NONE
    self.troubleId = 0
    self.reasonList = []
    self.bNeedAnalyze = True

  def Set_Time(self,time):
    self.time = time

  def Set_Timestamp(self,timestamp):
    self.timestamp = timestamp

  def Set_Status(self,status):
    self.status = status

  def Set_BizId(self,bizId):
    self.bizId = bizId

  def Set_TroubleId(self,troubleId):
    self.troubleId = troubleId

  def Set_ReasonList(self,reasonList):
    self.reasonList = reasonList

  def Set_NeedAnalyze(self,bNeedAnalyze):
    self.bNeedAnalyze = bNeedAnalyze


  def Get_Time(self):
      return self.time

  def Get_Timestamp(self):
      return self.timestamp

  def Get_Status(self):
    return self.status

  def Get_BizId(self):
    return self.bizId

  def Get_TroubleId(self):
    return self.troubleId

  def Get_ReasonList(self):
    return self.reasonList

  def Get_NeedAnalyze(self):
    return self.bNeedAnalyze

#告警项reason层
class CWarnReason:
  def __init__(self):
    self.groupId = 0
    self.groupName = ""
    self.rules = []

  def Set_GroupId(self,groupId):
    self.groupId = groupId

  def Set_GroupName(self,groupName):
    self.groupName = groupName

  def Set_Rules(self,rules):
    self.rules = rules

  def Get_GroupId(self):
    return self.groupId

  def Get_GroupName(self):
    return self.groupName

  def Get_Rules(self):
    return self.rules

#告警项rules层
class CWarnRule:
  def __init__(self):
    self.ruleId = 0
    self.ruleName = ""
    self.umpKey = ""
    self.item = ""        #告警项，有映射表
    self.value = 0
    self.oper = ""
    self.targetValue = 0  #规则阈值
    self.limit = 0        #连续发生次数上限阈值
    self.conTimes = 0     #连续发生次数
    self.curKeytotal = 0  #key关联项当前值
    self.hisKeytotal = 0 #key关联历史值

  def Set_RuleId(self,ruleId):
    self.ruleId = ruleId

  def Set_RuleName(self,ruleName):
    self.ruleName = ruleName

  def Set_UmpKey(self,umpKey):
    self.umpKey = umpKey

  def Set_Item(self,item):
    self.item = item

  def Set_Value(self,value):
    self.value = value

  def Set_Oper(self,oper):
    self.oper = oper

  def Set_TargetValue(self,targetValue):
    self.targetValue = targetValue

  def Set_Limit(self,limit):
    self.limit = limit

  def Set_ConTimes(self,conTimes):
    self.conTimes = conTimes

  def Set_CurKeytotal(self,curKeytotal):
    self.curKeytotal = curKeytotal

  def Set_HisKeytotal(self,hisKeytotal):
    self.hisKeytotal = hisKeytotal

  def Get_RuleId(self):
    return self.ruleId

  def Get_RuleName(self):
    return self.ruleName

  def Get_UmpKey(self):
    return self.umpKey

  def Get_Item(self):
    return self.item

  def Get_Value(self):
    return self.value

  def Get_Oper(self):
    return self.oper

  def Get_TargetValue(self):
    return self.targetValue

  def Get_Limit(self):
    return self.limit

  def Get_ConTimes(self):
    return self.conTimes

  def Get_CurKeytotal(self):
    return self.curKeytotal

  def Get_HisKeytotal(self):
    return self.hisKeytotal


#推送告警消息类 -- 根据此类来判断发送哪个负载的消息和消息备份使用
class CRgySendMsg:
  def __init__(self):
    self.typeList = []   #消息的类型 -- 0无问题，1抖动已恢复，2持续增长未恢复
    self.msgList = []    #消息列表

  def Add_MsgType(self,msgType):
    self.typeList.append(msgType)

  def Get_TypeList(self):
    return self.typeList

  def Add_MsgList(self,warnMsg):
    self.msgList.append(warnMsg)

  def Get_MsgList(self):
    return self.msgList
