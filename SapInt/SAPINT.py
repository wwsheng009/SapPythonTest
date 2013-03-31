# -*- coding: utf-8 -*- 
#作者：王卫生
#时间：2013-3-31
#使用SAPINT 文件
#测试python 与SAP NCO之间的调用

import sys
import clr
import System


#添加VB DLL的目录
#from System.IO import Directory,Path
#directory = Directory.GetCurrentDirectory()
#binpath = Path.Combine(directory,'sap\\')

sys.path.append(r'E:\Github\sap_interface\SAPINTGUI\bin\Debug')
#sys.path.append(System.AppDomain.CurrentDomain.BaseDirectory)
#sys.path.append(binpath)
clr.AddReferenceToFile("SAPINT.dll")
clr.AddReferenceToFile("SAPINTGUI.exe")

#clr.AddReferenceToFile("ConfigFileTool.dll")
#clr.AddReferenceToFile("sapnco.dll")
#from SAPINT import *
#from SAPINTGUI import *
from SAPINT.SapConfig import *
SAPConfigFromFile.LoadSAPClientConfig();

from SAPINT.Function import *
list = SAPFunction.SearchRfcFunctions("LH205","Z*","")



