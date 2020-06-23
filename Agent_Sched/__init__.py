from gym.envs.registration import register

register(
    id='Agent_Sched-v0',
    entry_point='Agent_Sched.envs:AgentSchedEnv',
)
