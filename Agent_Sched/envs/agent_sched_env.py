import gym
from gym import error, spaces, utils
from gym.utils import seeding

class AgentSchedEnv(gym.Env):
  def __init__(self):
    self.wip1 = 1000         #Number of tasks in Q1
    self.service_t1 = 1      #Takes 1 timeslot to finish 1 task
    self.wip2 = 100          #Number of tasks in Q2
    self.service_t2 = 2      #Takes 2 timeslots to finish 1 task
  
  def step(self, action):
  
  def reset(self):
  
  def render(self):
  
  def close(self):
