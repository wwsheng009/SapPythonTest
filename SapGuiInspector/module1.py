
import sys
import clr
import System
import string

sys.path.append(r'D:\wangws\sap_interface_project\SAPAutomation\SAPGuiInspector\bin\Debug')
#sys.path.append(r'C:\Program Files (x86)\SAP\FrontEnd\SAPgui')
#clr.AddReferenceToFile("Interop.SAPFEWSELib.dll")
clr.AddReferenceToFile("SapGuiApplicationVB.dll")

clr.AddReference('Microsoft.VisualBasic')
from SapGuiApplicationVB import *
from System import Array, Type, Activator

from Microsoft.VisualBasic.CompilerServices import LateBinding

sapApplication =  sapApp()
session = sapApplication.getSessionByTcode("MB03")
#ty = System.Reflection.Assembly.Load("Interop.SAPFEWSELib.dll").GetType('GuiSession')
#a = Activator.CreateInstance(ty)
#session =  sapApplication.sapApp
#session.FindById("wnd[0]")
##session.findById("wnd[0]").resizeWorkingPane (126,27,false)
#session.findById("wnd[0]")
#o = session.findById("wnd[0]")
#session.sendVKey (4)
#session.findById("wnd[1]").sendVKey (0)
#session.findById("wnd[1]/usr/lbl[1,24]").setFocus()
#session.findById("wnd[1]/usr/lbl[1,24]").caretPosition = 8
#session.findById("wnd[1]").sendVKey (2)
guiComponent = sapApplication.getControlById("wnd[0]/usr/ctxtRM07M-MBLNR")


#LateBinding.LateCall(session,None,"CreateSession",None,None ,None)
strarr = Array[System.String](["123124"])
LateBinding.LateCall(guiComponent,None,"text",strarr,None,None)

#wrapper = Activator.CreateInstance(Type.GetTypeFromProgID('SapROTWr.SapROTWrapper'))
#RotSAPGUI = wrapper.GetROTEntry("SAPGUI")
#aa = RotSAPGUI.GetScriptingEngine()