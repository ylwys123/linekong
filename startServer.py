import os
import sys,datetime,time



cmd_listpid = "ps -ef | grep '.jar -work' | grep -v grep"
cmd_start = "java -XX:-OmitStackTraceInFastThrow -jar logicserver.jar -work $1 > \\nohup.out &"

result = os.popen(cmd_listpid)

pid_line = result.read()

print len(pid_line)

if len(pid_line) > 0:
    exit() 
else:
    datenow  = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
    os.system("mv nohup.out nohuplog/nohup.out.old."+datenow)
    print("Start Server at :------------------------------------"+ datenow)
    os.system(cmd_start)


