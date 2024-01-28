import gymnasium as gym
from stable_baselines3 import PPO, DQN, A2C, DDPG, SAC, TD3
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_vec_env
from huggingface_sb3 import load_from_hub, ModelRepoId, ModelName, EnvironmentName
import time, argparse



# Initialize parser
parser = argparse.ArgumentParser()
# Adding optional argument
parser.add_argument("-p", "--policy", type=str, help="policy name", default="ppo")
parser.add_argument("-m", "--model", type=int, help="model name", default=1000)
# Read arguments from command line
args = parser.parse_args()
model_name = args.model
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


checkpoint = load_from_hub(
    repo_id="uwwee/Taxi-v3",
    filename=f"{model_name}.zip",
)
model = policy.load(checkpoint)

vec_env = make_vec_env("Taxi-v3", n_envs=1)
episodes = 10

for ep in range(episodes):
    obs = vec_env.reset()
    done = False
    while not done:
        action, _states = model.predict(obs)
        obs, reward, done, info = vec_env.step(action)
        vec_env.render("human")
        time.sleep(0.01)
vec_env.close()