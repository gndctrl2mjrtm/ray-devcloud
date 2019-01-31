import sys
import os

with open('head_ip','r') as f:
    head_ip_addr = f.read()

for i in range(int(sys.argv[1])): 
    os.system('/usr/local/bin/qsub create_worker {}'.format(head_ip_addr))
