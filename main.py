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
        for x in processInfo:
            v = x["user"]
            print(str(v))
a = processManager()
a.update()
            
