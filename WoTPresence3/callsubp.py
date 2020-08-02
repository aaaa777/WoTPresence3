import subprocess
import time

subp = subprocess.Popen(r'C:\Users\a774n\source\repos\WoTPresence3\dist\WoTPresence3.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE)

#line = subp.stdout.readline()

print(subp.pid)

subp.stdin.write('{"state": "test2"}\n')

time.sleep(120)
