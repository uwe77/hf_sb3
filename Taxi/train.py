import gymnasium as gym
from stable_baselines3 import PPO
import os


model_dir  = 'models/tb_ppo'
logdir     = 'logs'
TIMESTEPS = 10000


if not os.path.exists(model_dir):
    os.makedirs(model_dir)

if not os.path.exists(logdir):
    os.makedirs(logdir)

env = gym.make('Taxi-v3')
env.reset()

model = PPO('MlpPolicy', env, verbose=1, tensorboard_log=logdir)
for i in range(1, 300):
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name='tb_ppo')
    model.save(f'{model_dir}/{i*TIMESTEPS}')

env.close()