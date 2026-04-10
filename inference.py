from server.cloud_env import CloudEnv

env = CloudEnv()

state = env.reset()

print("[START] task=easy", flush=True)

total_reward = 0
steps = 0

for i in range(3):
    action = 0  # simple action
    state, reward, done, info = env.step(action)
    
    steps += 1
    total_reward += reward
    
    print(f"[STEP] step={steps} reward={reward}", flush=True)
    
    if done:
        break

score = total_reward / steps if steps > 0 else 0

print(f"[END] task=easy score={score} steps={steps}", flush=True)