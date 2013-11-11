import sys
import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Reflection')
clr.AddReference('System.IO')

from System.Windows.Forms import *
from System import Activator
from System.IO import File
from System.Reflection import Assembly

Application.EnableVisualStyles()
Application.SetCompatibleTextRenderingDefault(False)

formName = sys.argv[1] # Format should include namespace.form_name

bytes = File.ReadAllBytes(r'C:\some project\bin\debug\someProject.exe')
asm = Assembly.Load(bytes)
t = asm.GetType(formName) 
ins = Activator.CreateInstance(t)
frm = clr.Convert(ins, Form)
Application.Run(frm)

