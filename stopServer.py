import os
import sys



cmd_listpid = "ps -ef | grep '.jar -work' | grep -v grep"
cmd_killpid = "kill "
result = os.popen(cmd_listpid)


pid_line = result.read()
pid_str = pid_line.split()
if len(pid_str) > 1:
    os.system( cmd_killpid +  pid_str[1])


