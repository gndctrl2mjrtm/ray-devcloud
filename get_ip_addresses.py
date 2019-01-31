import ray
import time
import sys
import os

with open('head_ip','r') as f:
    head_ip_address = f.read()

ray.init(redis_address="{}".format(head_ip_address)) 

@ray.remote
def f():
    time.sleep(0.01)
    return ray.services.get_node_ip_address()

while True:
    ips = set(ray.get([f.remote() for _ in range(1000)])) 
    print(ips)
    print(len(ips))
    time.sleep(1)
