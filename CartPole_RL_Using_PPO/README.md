# CartPole Reinforcement Learning using PPO

A reinforcement learning project that trains an intelligent agent to solve the **CartPole-v1** environment using the **Proximal Policy Optimization (PPO)** algorithm from Stable-Baselines3. The agent learns to balance a pole on a moving cart by interacting with the environment and maximizing cumulative rewards.

---

## Overview

CartPole is a classic reinforcement learning control problem where an agent must keep a pole balanced on a moving cart for as long as possible. Instead of being explicitly programmed, the agent learns an optimal policy through trial-and-error interactions with the environment.

This project demonstrates the complete reinforcement learning pipeline, including environment setup, PPO agent training, policy evaluation, and visualization of the trained agent's performance.

---

## Environment

- **Environment:** CartPole-v1
- **Framework:** Gymnasium
- **Algorithm:** Proximal Policy Optimization (PPO)
- **Reinforcement Learning Library:** Stable-Baselines3
- **Training Steps:** 100,000 Timesteps
- **Platform:** Google Colab

---

## Problem Description

The CartPole environment consists of a cart that can move horizontally with a pole attached to its center.

### State Space

The agent observes four continuous variables:

- Cart Position
- Cart Velocity
- Pole Angle
- Pole Angular Velocity

### Action Space

The agent can perform two discrete actions:

- Move Left
- Move Right

### Reward

The agent receives **+1 reward** for every timestep the pole remains balanced. An episode ends when:

- The pole falls beyond the allowed angle.
- The cart moves outside the allowed position.
- The maximum episode length is reached.

---

## Technologies Used

- Python
- Gymnasium
- Stable-Baselines3
- PyTorch
- NumPy
- Matplotlib
- ImageIO

---

## Project Workflow

1. Create the CartPole environment.
2. Initialize the PPO reinforcement learning agent.
3. Train the agent through interactions with the environment.
4. Evaluate the learned policy.
5. Visualize the trained agent's performance.
6. Analyze the cumulative rewards achieved during evaluation.

---

## Features

- PPO-based reinforcement learning agent
- Automated environment interaction
- Policy training and evaluation
- Deterministic policy testing
- Performance visualization
- Agent model saving and loading

---

## Results

The trained PPO agent successfully learns to balance the pole for extended durations and achieves near-optimal performance on the CartPole-v1 environment. During evaluation, the agent consistently reaches rewards close to the maximum possible score, demonstrating stable and effective policy learning.

---

## Repository Structure

```text
CartPole-PPO/
│
├── cartpole_ppo.ipynb
├── trained_model.zip
├── README.md
└── results/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/CartPole-PPO.git
```

Install the required libraries:

```bash
pip install gymnasium stable-baselines3 torch numpy matplotlib imageio
```

Run the Jupyter Notebook:

```bash
jupyter notebook cartpole_ppo.ipynb
```

---

## Future Improvements

- Compare PPO with DQN and A2C algorithms
- Hyperparameter optimization
- TensorBoard integration for training visualization
- Train on more complex reinforcement learning environments such as LunarLander and BipedalWalker

---

## Conclusion

This project demonstrates the application of Proximal Policy Optimization (PPO) to solve the CartPole control problem using reinforcement learning. It provides practical experience in environment interaction, policy optimization, agent evaluation, and performance analysis, serving as a strong introduction to modern reinforcement learning techniques.
