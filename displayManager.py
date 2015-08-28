import curses

class displayManager():
    def __init__(self):
        self.screen = curses.initscr()
        self.screen.clear()
        self.screen.border(0)
        self.screen.nodelay(1)
    def paint(self):
        self.screen.border(0)
        self.screen.refresh()
    def clear(self):
        self.screen.clear()
    def getch(self):
        return self.screen.getch()
    def write(self,x,y,strin):
        self.screen.addstr(y,x,str(strin))
    def destroy(self):
        curses.endwin()
    def dim(self):
        return self.screen.getmaxyx()
    def wireframe(self):
        a = self.dim()
        width = a[1]
        if((width%2)==0):
            w = width/2
            self.write(int(w),1,"Server Shield")
        else:
            w = (width-1)/2
            self.write(int(w),1,"Server Shield")

