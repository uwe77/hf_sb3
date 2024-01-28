import gymnasium as gym
from stable_baselines3 import DQN, PPO, A2C, DDPG, SAC, TD3
import os, argparse



# Initialize parser
parser = argparse.ArgumentParser()
# Adding optional argument
parser.add_argument("-p", "--policy", type=str, help="policy name", default="ppo")
# Read arguments from command line
args = parser.parse_args()
policy_name = args.policy
policy = None
if policy_name == "ppo":
    policy = PPO
elif policy_name == "dqn":
    policy = DQN
elif policy_name == "a2c":
    policy = A2C
elif policy_name == "ddpg":
    policy = DDPG
elif policy_name == "sac":
    policy = SAC
elif policy_name == "td3":
    policy = TD3
else:
    raise Exception("Invalid policy name")

model_dir  = f'models/tb_{policy_name}'
logdir     = 'logs'
TIMESTEPS = 10000


if not os.path.exists(model_dir):
    os.makedirs(model_dir)

if not os.path.exists(logdir):
    os.makedirs(logdir)

env = gym.make('Taxi-v3')
env.reset()

model = policy('MlpPolicy', env, verbose=1, tensorboard_log=logdir)
for i in range(1, 300):
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=f'tb_{policy_name}')
    model.save(f'{model_dir}/{i*TIMESTEPS}')

env.close()