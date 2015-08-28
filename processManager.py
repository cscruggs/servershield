import psutil,datetime,time

class processManager():
    def update(self):
        threadCount = 0
        processCount = 0
        processInfo = []
        for proc in psutil.process_iter():
            procInfo = {}
            procInfo["id"] = proc.pid
            procInfo["name"] = proc.name()
            p = psutil.Process(proc.pid)
            procInfo["user"] = proc.username()
            delta = datetime.timedelta(seconds=(time.time() - p.create_time()))
            procInfo["time"] = str(delta).split('.')[0]
            procInfo["cpu"] = p.cpu_percent()
            procInfo["memory"] = round(p.memory_percent(),2)
            procInfo["command"] = ' '.join(p.cmdline())
            threadCount += p.num_threads()
            processCount += 1
            processInfo.append(procInfo)
        self.table = processInfo

    def getChild(self,pid):
        try:
            p = psutil.Process(pid)
        except:
            return []
        l = []
        child_pid = p.children()
        for pid in child_pid:
            l.append(pid.pid)
        return l

    def info(self,pid):
        p = psutil.Process(pid)
        delta = datetime.timedelta(seconds=(time.time() - p.create_time()))
        procInfo = [] 
        procInfo.append(str( p.pid))
        procInfo.append(str( p.username()))
        procInfo.append(str( p.num_threads()))
        procInfo.append(str( p.cpu_percent()))
        procInfo.append(str( round(p.memory_percent(),2)))
        procInfo.append(str( str(delta).split('.')[0]))
        procInfo.append(str( p.name()))
        procInfo.append(str( ' '.join(p.cmdline())))
        return procInfo

