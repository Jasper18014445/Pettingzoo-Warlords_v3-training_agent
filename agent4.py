
import numpy as np

class Agent4:
    def act(self, observation):
        return np.random.choice([1, np.random.randint(2, 6)])
