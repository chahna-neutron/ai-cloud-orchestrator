from fastapi import FastAPI
from server.cloud_env import CloudEnv
from server.tasks import easy_task, medium_task, hard_task
from server.models import Action

app = FastAPI()
env = CloudEnv()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/reset")
def reset():
    return env.reset()

@app.get("/state")
def state():
    return env.state()

@app.post("/step")
def step(action: Action):
    state, reward, done, info = env.step(action.action)
    return {
        "state": state,
        "reward": reward,
        "scores": {
            "easy": easy_task(state),
            "medium": medium_task(state),
            "hard": hard_task(state)
        },
        "done": done,
        "info": info
    }




def main():
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()