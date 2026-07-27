# Lunar Lander Reinforcement Learning using PPO

A reinforcement learning project that trains an intelligent agent to successfully land a spacecraft in the **LunarLander-v3** environment using the **Proximal Policy Optimization (PPO)** algorithm from Stable-Baselines3. The agent learns an optimal landing strategy through continuous interaction with the environment while maximizing cumulative rewards.

---

## Overview

LunarLander is a challenging reinforcement learning benchmark from Gymnasium's Box2D environments. The objective is to safely land a spacecraft between two landing flags while maintaining balance, controlling velocity, and minimizing unnecessary fuel consumption.

This project demonstrates the complete reinforcement learning workflow, including environment setup, PPO agent training, policy evaluation, and performance analysis.

---

## Environment

- **Environment:** LunarLander-v3
- **Framework:** Gymnasium (Box2D)
- **Algorithm:** Proximal Policy Optimization (PPO)
- **Reinforcement Learning Library:** Stable-Baselines3
- **Training Steps:** 1,000,000 Timesteps
- **Platform:** Google Colab

---

## Problem Description

The Lunar Lander environment simulates a spacecraft attempting to perform a controlled landing on the moon's surface.

### State Space

The agent observes eight continuous variables:

- Lander Position (X, Y)
- Lander Velocity (X, Y)
- Lander Angle
- Angular Velocity
- Left Leg Ground Contact
- Right Leg Ground Contact

### Action Space

The agent can perform four discrete actions:

- Do Nothing
- Fire Left Thruster
- Fire Main Engine
- Fire Right Thruster

### Reward

The reward function encourages the agent to:

- Land safely on the landing pad
- Maintain a stable orientation
- Reduce landing speed
- Minimize unnecessary fuel usage

Large positive rewards are given for successful landings, while crashes and inefficient movements receive penalties.

---

## Technologies Used

- Python
- Gymnasium (Box2D)
- Stable-Baselines3
- PyTorch
- NumPy
- Matplotlib

---

## Project Workflow

1. Create the LunarLander-v3 environment.
2. Initialize the PPO reinforcement learning agent.
3. Train the agent through continuous interaction with the environment.
4. Evaluate the learned policy on unseen episodes.
5. Analyze the cumulative rewards achieved during evaluation.
6. Visualize the trained agent performing successful landings.

---

## Features

- PPO-based reinforcement learning agent
- Environment interaction and policy optimization
- Agent training and evaluation
- Deterministic policy testing
- Performance analysis using evaluation rewards
- Trained model saving and loading

---

## Results

The trained PPO agent successfully learns a stable landing policy for the LunarLander-v3 environment. After training, the agent consistently achieves evaluation rewards above the environment's solved threshold, demonstrating effective navigation, controlled descent, and safe landing behavior.

---

## Repository Structure

```text
Lunar-Lander-PPO/
│
├── lunar_lander_RL.ipynb
├── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Lunar-Lander-PPO.git
```

Install the required libraries:

```bash
pip install gymnasium[box2d] stable-baselines3 torch numpy matplotlib
```

Run the Jupyter Notebook:

```bash
jupyter notebook lunar_lander_ppo.ipynb
```

---

## Future Improvements

- Compare PPO with DQN, A2C, and SAC algorithms
- Perform hyperparameter optimization
- Integrate TensorBoard for training visualization
- Extend the project to the continuous-action version of LunarLander using SAC or TD3

---

## Conclusion

This project demonstrates the application of Proximal Policy Optimization (PPO) to solve the LunarLander-v3 environment. It provides practical experience in reinforcement learning, policy optimization, environment interaction, and agent evaluation, serving as a foundation for tackling more complex robotics and autonomous control problems.
