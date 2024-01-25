from huggingface_sb3 import package_to_hub, push_to_hub
import os, shutil


model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models/tb_ppo")
current_path = os.path.dirname(os.path.abspath(__file__))
model_name = "10000.zip"

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