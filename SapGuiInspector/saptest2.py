
import sys
import clr
import System

sys.path.append(r'D:\wangws\sap_interface_project\SAPAutomation\SAPGuiInspector\bin\Debug')
sys.path.append(r'C:\Program Files (x86)\SAP\FrontEnd\SAPgui')
clr.AddReferenceToFile("Interop.SAPFEWSELib.dll")

clr.AddReferenceToFile("Interop.SapROTWr.dll")

from SAPFEWSELib import *
from SapROTWr import *

wrapper = System.Activator.CreateInstance(System.Type.GetTypeFromProgID('SapROTWr.SapROTWrapper'))
RotSAPGUI = wrapper.GetROTEntry("SAPGUI")
aa = RotSAPGUI.GetScriptingEngine()


