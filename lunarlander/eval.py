import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_vec_env
from huggingface_sb3 import load_from_hub, ModelRepoId, ModelName, EnvironmentName


checkpoint = load_from_hub(
    repo_id="uwwee/ppo-LunarLander-v2",
    filename="1600000.zip",
    # repo_id="osanseviero/ppo-LunarLander-v2",
    # filename="ppo-LunarLander-v2.zip",
)
model = PPO.load(checkpoint)

vec_env = make_vec_env("LunarLander-v2", n_envs=1)
episodes = 10

for ep in range(episodes):
    obs = vec_env.reset()
    done = False
    while not done:
        action, _states = model.predict(obs)
        obs, reward, done, info = vec_env.step(action)
        vec_env.render("human")
vec_env.close()