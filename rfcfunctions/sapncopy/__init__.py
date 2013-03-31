# -*- coding: utf-8 -*-
#作者：王卫生
#时间：2013-3-31
#使用SAPINT 文件
#测试python 与SAP NCO之间的调用

__version__ = '1.0.0'
__author__ = 'Vincent wang<vincentwwsheng@gmail.com>'

__all__ = ['BackUpConfig','LoadSapDll']

import BackUpConfig
from SAP.Middleware.Connector import RfcDestinationManager
from BackUpConfig import BackupDestinationConfiguration


#初始化配置文件
config = BackupDestinationConfiguration()
#注册配置
RfcDestinationManager.RegisterDestinationConfiguration(config)

#根据名称返回连接
def GetDestination(destinationName):
    return RfcDestinationManager.GetDestination(destinationName)
