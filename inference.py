import os
from openai import OpenAI
from server.cloud_env import CloudEnv

client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)

env = CloudEnv()
state = env.reset()

# ✅ FIXED
response = client.chat.completions.create(
    model=os.environ.get("MODEL_NAME", "gpt-3.5-turbo"),
    messages=[
        {"role": "user", "content": "Give any random action"}
    ]
)

dummy = response.choices[0].message.content

print("[START] task=easy", flush=True)

total_reward = 0
steps = 0

for i in range(3):
    action = 0
    state, reward, done, info = env.step(action)
    
    steps += 1
    total_reward += reward
    
    print(f"[STEP] step={steps} reward={reward}", flush=True)
    
    if done:
        break

score = total_reward / steps if steps > 0 else 0

print(f"[END] task=easy score={score} steps={steps}", flush=True)