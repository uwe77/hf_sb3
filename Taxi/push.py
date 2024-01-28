from huggingface_sb3 import package_to_hub, push_to_hub
import os, shutil, argparse


# Initialize parser
parser = argparse.ArgumentParser()
# Adding optional argument
parser.add_argument("-p", "--policy", type=str, help="policy name", default="ppo")
parser.add_argument("-m", "--model", type=int, help="model name", default=1000)
# Read arguments from command line
args = parser.parse_args()


model_file = args.model
policy_name = args.policy


model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"models/tb_{policy_name}")
current_path = os.path.dirname(os.path.abspath(__file__))
model_name = f"{model_file}.zip"

try:
    shutil.copy(f'{model_path}/{model_name}', f'{current_path}/{model_name}')
    push_to_hub(
    repo_id="uwwee/Taxi-v3",
    filename=model_name,
    commit_message=f"Added Taxi-v3 {model_file}.zip model trained with {policy_name}",
    )
    os.remove(f'{current_path}/{model_name}')
except Exception as e:
    print(e)
    pass