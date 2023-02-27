# Author: Anthony Rafidison <benjaraf006@gmail.com>
import random

class BubbleSort:
    def __init__(self, L: list[int|float]):
        self.list = L

    def sort(self):
        while True:
            permutations = 0
            for n in range(len(self.list)-1):
                if self.list[n] > self.list[n+1]:
                    self.list[n], self.list[n+1] = self.list[n+1], self.list[n]
                    permutations += 1
            
            if permutations in [0,1]:
                break

if __name__ == "__main__":
    l = list(range(10))
    random.shuffle(l)

    s = BubbleSort(l)
    s.sort()

    print(s.list)

