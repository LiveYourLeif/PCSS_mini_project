import random
import numpy as np
from abc import ABC, abstractmethod

#Interface for the stats
class Stats(ABC):
    @abstractmethod
    def hitpoints(self) -> int:
        pass

    def strength(self) -> int:
        pass
    
    def defense(self) -> int:
        pass

    def magic(self) -> int:
        pass
