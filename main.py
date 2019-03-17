import matplotlib.pyplot as plt
import numpy as np
import random
from sortings import bubble

class Array(list):
    def __init__(self, n=None):
        super().__init__(self)
        if n is not None:
            for i in range(n):
                self.append(i)

        self.initialized = False
        self.item_access = 0
        self.swaps = 0

    def shuffle(self):
        random.shuffle(self)
        self.initialized = True

    def __getitem__(self, item):
        if self.initialized:
            self.item_access += 1
        return super().__getitem__(item)

n = 50
coordinates = list(range(n))
arr = Array(n)
arr.shuffle()
plt.ion()
bubble(arr, plt)
# for i in range(50):
#     arr.shuffle()
#     plt.bar(coordinates, arr)
#     plt.draw()
#     plt.pause(0.0001)
#     plt.clf()