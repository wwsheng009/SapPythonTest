# -*- coding: utf-8 -*-
#作者：王卫生
#时间：2013-3-31
#使用SAPINT 文件
#测试python 与SAP NCO之间的调用
import sys
sys.path.append(r'D:\wangws\sap_interface_project\SapPythonTest\rfcfunctions')
#import BackUpCconfig
import sapncopy
from sapncopy import *
#from sapnco import * 
#from SAP.Middleware.Connector import *
#from BackUpCconfig import *



##初始化配置文件
#config = BackupDestinationConfiguration()
##注册配置
#RfcDestinationManager.RegisterDestinationConfiguration(config)

#返回目标系统
destination = sapncopy.GetDestination('LH205')

#转换RFCTABLE为LIST
def rfcTableToList(fieldtab):
    rows = []
    for r in range(fieldtab.RowCount):
        fieldtab.CurrentIndex = r
        row = []
        for c in range(fieldtab.ElementCount):
            row.append(fieldtab.GetValue(c))
        rows.append(row)
    return rows

def DDIF_FIELDINFO_GET():
    rfcFunctionSearch = destination.Repository.CreateFunction("DDIF_FIELDINFO_GET")
    rfcFunctionSearch.SetValue("TABNAME", 'MARA')
    rfcFunctionSearch.Invoke(destination)
    fieldtab = rfcFunctionSearch.GetTable("DFIES_TAB")
    fieldtab.ElementCount
    fieldtab.RowCount
    range(fieldtab.ElementCount)
    rows = []
    for r in range(fieldtab.RowCount):
        fieldtab.CurrentIndex = r
        row = []
        for c in range(fieldtab.ElementCount):
            row.append(fieldtab.GetValue(c))
        rows.append(row)

def searchRfcFunction(_funame,functionGroup):
    RFC_FUNCTION_SEARCH = destination.Repository.CreateFunction("RFC_FUNCTION_SEARCH");
    RFC_FUNCTION_SEARCH.SetValue("FUNCNAME", _funame);
    RFC_FUNCTION_SEARCH.SetValue("GROUPNAME", functionGroup);
    RFC_FUNCTION_SEARCH.Invoke(destination);
    FUNCTIONS = RFC_FUNCTION_SEARCH.GetTable("FUNCTIONS");
    return rfcTableToList(FUNCTIONS)


result = searchRfcFunction('z*',"")


