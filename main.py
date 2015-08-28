from processManager import *
from displayManager import *
from displayTable import *
import time

def tableFormat(a,b):
    a.append(str(b["id"]))
    a.append(str(b["user"]))
    a.append(str(b["cpu"]))
    a.append(str(b["memory"]))
    a.append(str(b["time"]))
    a.append(str(b["name"]))
    a.append(str(b["command"]))
    return a

DE = displayManager()

def update():
    a = processManager()
    a.update()
    tab = a.table
    
    dim = DE.dim()
    DE.clear()
    DE.wireframe()
    leftUpper = {}
    rightLower = {}
    leftUpper["x"] = 2
    leftUpper["y"] = 2
    rightLower["x"] = dim[1] -2
    rightLower["y"] = dim[0] -2
    
    tabl = table(DE,leftUpper,rightLower)
    columnA = [7,15,5,8,23,30,70]
    
    bol = tabl.addColumn(columnA)

    tab = sorted(tab,key=lambda k:k["memory"],reverse=True)
    c = []
    for zeta in tab:
        c = tableFormat(c,zeta)
        tabl.append(c)
        c = []
    
    if(not bol):
        DE.destroy()
        print("error in tables")
    DE.paint()
    inp = DE.getch()
    if(inp == 113):
        exit()
        return
    time.sleep(1)
    update()

def exit():
    DE.destroy()


update()
