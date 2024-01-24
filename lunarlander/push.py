import gymnasium as gym

from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from huggingface_sb3 import package_to_hub, push_to_hub
import os, shutil


# Create the environment
env_id = "LunarLander-v2"
env = make_vec_env(env_id, n_envs=1)
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models/tb_ppo")
current_path = os.path.dirname(os.path.abspath(__file__))
model_name = "1600000.zip"

try:
    shutil.copy(f'{model_path}/{model_name}', f'{current_path}/{model_name}')
    push_to_hub(
    repo_id="uwwee/ppo-LunarLander-v2",
    filename=model_name,
    commit_message="Added LunarLander-v2 model trained with PPO",
    )
    os.remove(f'{current_path}/{model_name}')
except Exception as e:
    print(e)
    pass
# sys.path.append(model_path)

# model = PPO.load(f'{model_path}/{model_name}')
# model.save("ppo-LunarLander-v2")
