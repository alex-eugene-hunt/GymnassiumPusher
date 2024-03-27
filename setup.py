from Algorithms.q_learning import run_q_learning
from Algorithms.deep_q_network import run_deep_q_network
from Algorithms.policy_gradient import run_policy_gradient
from Algorithms.actor_critic import run_actor_critic
from Algorithms.proximal_policy import run_proximal_policy
from Algorithms.model_based import run_model_based

run_algorithms = [
    ("Q-Learning", run_q_learning),
    ("Deep Q-Network (DQN)", run_deep_q_network),
    ("Policy Gradient Methods", run_policy_gradient),
    ("Actor-Critic Methods", run_actor_critic),
    ("Proximal Policy Optimization (PPO)", run_proximal_policy),
    ("Model-Based RL", run_model_based)
]