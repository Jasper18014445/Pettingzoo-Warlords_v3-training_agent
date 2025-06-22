
import numpy as np

class Agent3:
    def act(self, observation):
        return np.random.choice([1, np.random.randint(2, 6)])
