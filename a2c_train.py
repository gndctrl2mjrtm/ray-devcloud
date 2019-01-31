import ray
import ray.rllib.agents.a3c as a3c
from ray.tune.logger import pretty_print

with open('head_ip','r') as f:
    head_ip_address = f.read()

ray.init(redis_address="{}".format(head_ip_address))

config = a3c.DEFAULT_CONFIG.copy()
config["num_gpus"] = 0
config["num_gpus_per_worker"] = 0
config["num_workers"] = 5

agent = a3c.A2CAgent(config=config, env="SpaceInvadersNoFrameskip-v4")

for i in range(1000):
   result = agent.train()
   print(pretty_print(result))
   if i % 100 == 0:
       checkpoint = agent.save() 
       print("checkpoint saved at", checkpoint)
