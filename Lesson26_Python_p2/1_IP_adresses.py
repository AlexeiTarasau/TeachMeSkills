import subprocess
import sys

ip_addresses = ["127.0.0.1", "8.8.8.8"]
tmp_out  = sys.stdout
f = open (r"C:/Work/Home_Work_TMS/file.txt", "a")
sys.stdout  = f 

for i in ip_addresses:
    print(subprocess.run(["ping", i]))

f.close ()