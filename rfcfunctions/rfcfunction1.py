# -*- coding: utf-8 -*-
#作者：王卫生
#时间：2013-3-31
#使用SAPINT 文件
#测试python 与SAP NCO之间的调用
#import sys
#sys.path.append(r'D:\wangws\sap_interface_project\SapPythonTest\sapnco')
#import BackUpCconfig

import sapncopy
from sapncopy import * 
#from SAP.Middleware.Connector import *
#from BackUpCconfig import *



##初始化配置文件
#config = BackupDestinationConfiguration()
##注册配置
#RfcDestinationManager.RegisterDestinationConfiguration(config)

#返回目标系统
destination = sapnco.GetDestination('LH205')

rfcFunctionSearch = destination.Repository.CreateFunction("DDIF_FIELDINFO_GET")
rfcFunctionSearch.SetValue("TABNAME", 'MARA')
rfcFunctionSearch.Invoke(destination)
fieldtab = rfcFunctionSearch.GetTable("DFIES_TAB")
fieldtab.ElementCount
fieldtab.RowCount
range(fieldtab.ElementCount)
for i in range(fieldtab.RowCount):
    print i