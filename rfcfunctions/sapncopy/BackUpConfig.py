# -*- coding: utf-8 -*-
#作者：王卫生
#时间：2013-3-31
#使用SAPINT 文件
#测试python 与SAP NCO之间的调用

#定义SAP的连接配置
import LoadSapDll
from SAP.Middleware.Connector import *


class BackupDestinationConfiguration (IDestinationConfiguration):
    def GetParameters(self,name):
        if name == 'LH205':
            parms = RfcConfigParameters()
            parms.Add(RfcConfigParameters.Name, "LH205")
            parms.Add(RfcConfigParameters.AppServerHost, "192.168.0.205")
            parms.Add(RfcConfigParameters.SAPRouter, "/H/183.62.136.248/H/")
            parms.Add(RfcConfigParameters.SystemNumber, "00")
            parms.Add(RfcConfigParameters.SystemID, "RET")
            parms.Add(RfcConfigParameters.User, "wwsheng")
            parms.Add(RfcConfigParameters.Password, "wwsheng")
            parms.Add(RfcConfigParameters.Client, "500")
            parms.Add(RfcConfigParameters.Language, "ZH")
            return parms
    def ChangeEventsSupported(self):
        return 0