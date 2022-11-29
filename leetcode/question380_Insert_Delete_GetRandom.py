# 나의 풀이 

import random
class RandomizedSet:

    def __init__(self):
        self.r_set = []

    def insert(self, val: int) -> bool:
        if val in self.r_set:
            return False
        else : 
            self.r_set.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.r_set:
            return False
        else:
            self.r_set.remove(val)
            return True

    def getRandom(self) -> int:
        return random.choice(self.r_set)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

