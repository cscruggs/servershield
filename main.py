from processManager import *
from displayManager import *
from displayTable import *
import time

DE = displayManager()
PM = processManager()
depth = 0
def addEntry(box,pid,childIndex,last):
    global depth
    if(depth == 0):
        return
    pidInfo = PM.info(pid)
    if(childIndex != 0):
        if(last):
            pidInfo[7] = (" "*childIndex*5)+chr(9492)+(chr(9472)*4)+pidInfo[7]
        else:
            pidInfo[7] = (" "*childIndex*5)+chr(9474)+(chr(9472)*4)+pidInfo[7]
    box.append(pidInfo)
    depth = depth - 1
    children = PM.getChild(pid)
    for child in children:
        if(child == children[len(children)-1]):
            addEntry(box,child,childIndex+1,True)
        else:
            addEntry(box,child,childIndex+1,False)

def start():
    DE.clear()
    DE.wireframe()
    dimentions = DE.dim()
    leftUpper = {}
    rightLower = {}
    leftUpper["x"] = 2
    leftUpper["y"] = 3
    rightLower["x"] = dimentions[1] -2
    rightLower["y"] = dimentions[0] -3
    box = table(DE,leftUpper,rightLower)
    columns = [7,15,8,5,8,23,20,70]
    if(not box.addColumn(columns)):
        print("some error here")
        DE.destroy()
        exit()
    global depth
    depth = rightLower["y"] - leftUpper["y"] - 2
    title = ["ID","USER","THREADS","CPU","MEMORY","TIME","NAME","COMMAND"]
    box.append(title)
    title = [" "," "," "," "," "," "," "," ",]
    box.append(title)
    addEntry(box,1,0,False)
    DE.paint()
    time.sleep(2)
    userInput = DE.getch()
    if(userInput == 113):
        DE.destroy()
        quit()
    start()

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

start()
DE.destroy()
