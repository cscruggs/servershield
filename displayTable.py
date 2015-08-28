class table():
    def __init__(self,D,start,end):
        self.screen = D
        self.leftUpper = start
        self.rightLower = end
        self.top = start["y"]
    def addColumn(self,c):
        delta = self.rightLower["x"] - self.leftUpper["x"]
        for x in c:
            delta -= x
        if (delta >= 0):
            self.columnArch = c
            return True
        else:
            return False
    def append(self,data):
        if(self.top > self.rightLower["y"]):
            return False
        if(len(data) != len(self.columnArch)):
            return False
        iterator = 0
        marginLeft=0
        for block in data:
            blockLength = len(block)
            if(blockLength > self.columnArch[iterator]):
                self.screen.write(self.leftUpper["x"] + marginLeft,self.top,block[0:self.columnArch[iterator]])
            else:
                self.screen.write(self.leftUpper["x"] + marginLeft,self.top,block)
            marginLeft += self.columnArch[iterator]
            iterator += 1
        self.top += 1
