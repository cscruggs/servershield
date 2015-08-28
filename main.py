import glob
def list_processes():
    for pid_path in glob.glob('/proc/[0-9]*/'):

        # cmdline represents the command whith which the process was started
        f = open("%s/cmdline" % pid_path)
        pid = pid_path.split("/")[2] # get the PID
        # we replace the \x00 to spaces to make a prettier output from kernel
        cmdline = f.read().replace("\x00", " ").rstrip()
        f.close()

        yield (pid, cmdline)

for procs in list_processes():
    print(procs)
