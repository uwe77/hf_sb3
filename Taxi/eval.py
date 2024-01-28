import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_vec_env
from huggingface_sb3 import load_from_hub, ModelRepoId, ModelName, EnvironmentName
import time


checkpoint = load_from_hub(
    repo_id="uwwee/ppo-Taxi-v3",
    filename="600000.zip",
)
model = PPO.load(checkpoint)

vec_env = make_vec_env("Taxi-v3", n_envs=1)
episodes = 10

for ep in range(episodes):
    obs = vec_env.reset()
    done = False
    while not done:
        action, _states = model.predict(obs)
        obs, reward, done, info = vec_env.step(action)
        vec_env.render("human")
        time.sleep(0.1)
vec_env.close()