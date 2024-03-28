def run_q_learning():

    import gymnasium as gym
    from gymnasium import utils
    from gymnasium.envs.mujoco.pusher_v4 import PusherEnv

    env = PusherEnv(render_mode='human')
    observation = env.reset()

    for _ in range(3000):
        action = env.action_space.sample()  # Randomly sample an action
        observation, reward, done, info, _ = env.step(action)


        if done:
            observation = env.reset()

    return