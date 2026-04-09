# 🚀 AI Cloud Orchestrator

A FastAPI-based cloud orchestration simulator that dynamically manages server scaling based on incoming traffic and CPU utilization.

---

## 📌 Overview

This project simulates a cloud environment where:

* Requests fluctuate randomly
* CPU usage depends on load and server count
* The system decides whether to scale up or down

It mimics real-world cloud auto-scaling logic used in platforms like AWS, Azure, and Kubernetes.

---

## ⚙️ System Architecture

```
          +----------------------+
          |   Client / API Call  |
          +----------+-----------+
                     |
                     v
          +----------------------+
          |      FastAPI App     |
          |      (app.py)        |
          +----------+-----------+
                     |
                     v
          +----------------------+
          |   Cloud Environment  |
          |   (cloud_env.py)     |
          +----------+-----------+
                     |
        +------------+------------+
        |                         |
        v                         v
  CPU Calculation          Request Simulation
        |                         |
        +------------+------------+
                     |
                     v
          +----------------------+
          |   Reward Function    |
          +----------------------+
```

---

## 📁 Project Structure

```
ai-cloud-orchestrator/
│
├── app.py                # FastAPI entry point
├── inference.py         # API logic handler
├── Dockerfile           # Deployment config
├── requirements.txt     # Dependencies
├── openenv.yaml         # API endpoint config
│
└── server/
    ├── cloud_env.py     # Environment simulation logic
    ├── models.py        # Request/response models
    └── tasks.py         # Action handling logic
```

---

## 🔥 Features

* 📊 Dynamic request simulation
* ⚡ CPU usage calculation
* 🔄 Auto-scaling (scale up / scale down)
* 🎯 Reward-based decision system
* 🚀 Fully deployed on Hugging Face Spaces

---

## 🌐 Live API

👉 https://chahnaaa-ai-cloud-orchestrator.hf.space

Swagger Docs:
👉 https://chahnaaa-ai-cloud-orchestrator.hf.space/docs

---

## 📡 API Endpoints

| Method | Endpoint | Description       |
| ------ | -------- | ----------------- |
| GET    | `/`      | Check API status  |
| POST   | `/reset` | Reset environment |
| GET    | `/state` | Get current state |
| POST   | `/step`  | Perform action    |

---

## 🧠 How It Works

1. System starts with:

   * 2 servers
   * 100 requests
   * 50% CPU

2. Each step:

   * Requests change randomly
   * CPU recalculated:

     ```
     cpu = requests / (servers * 2)
     ```

3. Action:

   * `scale_up` → increase servers
   * `scale_down` → decrease servers

4. Reward:

   * CPU > 90 → ❌ overload (-1)
   * CPU < 30 → ⚠ underutilized (-0.5)
   * Optimal → ✅ (+1)

---

## 🐳 Deployment

This project is containerized using Docker and deployed on Hugging Face Spaces.

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

---

## 📌 Tech Stack

* Python
* FastAPI
* Uvicorn
* Docker

---

## 💡 Future Improvements

* Add reinforcement learning agent
* Improve scaling strategy
* Add real-time dashboard
* Integrate cloud metrics APIs

---

## 👩‍💻 Author

**Chahna Sri G**
