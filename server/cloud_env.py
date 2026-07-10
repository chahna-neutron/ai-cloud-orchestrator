import random
from typing import Dict, Any, Tuple

class CloudEnv:
    def __init__(self):
        self.cpu = 50.0
        self.servers = 2
        self.requests = 100
        self.reset()

    def reset(self) -> Dict[str, Any]:
        """Resets the environment simulation back to baseline metrics."""
        self.cpu = 50.0
        self.servers = 2
        self.requests = 100
        return self.state()

    def state(self) -> Dict[str, Any]:
        """Returns the current infrastructure telemetry data."""
        return {
            "cpu_usage": round(self.cpu, 2),
            "servers": self.servers,
            "requests": max(0, self.requests)  # Traffic can never be negative
        }

    def step(self, action: str) -> Tuple[Dict[str, Any], float, bool, Dict[str, Any]]:
        """Executes a cloud scaling action and computes the resulting environment state."""
        if action == "scale_up":
            self.servers += 1
        elif action == "scale_down" and self.servers > 1:
            self.servers -= 1

        # Simulate stochastic traffic fluctuations
        self.requests += random.randint(-20, 30)
        self.requests = max(0, self.requests)

        # Calculate CPU usage based on horizontal scale capacity
        calculated_cpu = self.requests / (self.servers * 2)
        # Absolute Clamping: Keeps CPU between realistic bounds (0% to 100%)
        self.cpu = min(100.0, max(0.0, calculated_cpu))  

        reward = self.calculate_reward()

        return self.state(), reward, False, {}

    def calculate_reward(self) -> float:
        """Evaluates infrastructure health step-rewards based on utilization thresholds."""
        if self.cpu > 90:
            return -1.0  # Overload penalty (Risk of service outage)
        elif self.cpu < 30:
            return -0.5  # Underutilization penalty (Wasted cloud spend)
        else:
            return 1.0   # Optimal operational efficiency