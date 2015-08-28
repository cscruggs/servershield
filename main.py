from processManager import *
from displayManager import *
from displayTable import *

def tableFormat(a,b):
    a.append(str(b["id"]))
    a.append(str(b["user"]))
    a.append(str(b["cpu"]))
    a.append(str(b["memory"]))
    a.append(str(b["time"]))
    a.append(str(b["name"]))
    a.append(str(b["command"]))
    return a


a = processManager()
a.update()
tab = a.table

DE = displayManager()
dim = DE.dim()
DE.wireframe()

leftUpper = {}
rightLower = {}
leftUpper["x"] = 2
leftUpper["y"] = 2
rightLower["x"] = dim[1] -2
rightLower["y"] = dim[0] -2

tabl = table(DE,leftUpper,rightLower)
columnA = [11,15,15,5,20,30,70]

bol = tabl.addColumn(columnA)
c = []
tab.reverse()
for zeta in tab:
    c = tableFormat(c,zeta)
    tabl.append(c)
    c = []

if(not bol):
    DE.destroy()
    print("error in tables")
#DE.write(10,10,str(rightLower))
DE.paint()
DE.getch()
DE.clear()
DE.destroy()
