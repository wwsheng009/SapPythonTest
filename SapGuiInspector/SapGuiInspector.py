# -*- coding: utf-8 -*- 
#作者：王卫生
#时间：2013-3-30

import sys
import clr
import System


#添加VB DLL的目录
from System.IO import Directory,Path
directory = Directory.GetCurrentDirectory()
#binpath = Path.Combine(directory,'bin\\')

sys.path.append(r'D:\wangws\sap_interface_project\SAPAutomation\SAPGuiInspector\bin\Debug')
#sys.path.append(System.AppDomain.CurrentDomain.BaseDirectory)
#sys.path.append(binpath)
clr.AddReferenceToFile("SapGuiApplicationVB.dll")


from SapGuiApplicationVB import SapGuiConnector
sapgui =  SapGuiConnector()

Session = sapgui.getSessionByTcode("MB03")
