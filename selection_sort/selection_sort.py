# Author: Anthony Rafidison <benjaraf006@gmail.com>
import random 


class SelectionSort:
    def __init__(self, L: list[int|float]):
        self.list = L
    
    def sort(self):
        for unsorted_index in range(len(self.list) - 1):
            min = self.list[unsorted_index]
            min_index = unsorted_index

            for i in range(unsorted_index+1, len(self.list)):
                if (actual := self.list[i]) < min:
                    min = actual
                    min_index = i

            self.list[min_index] = self.list[unsorted_index]
            self.list[unsorted_index] = min
    
    def __repr__(self) -> str:
        return self.list.__repr__()


if __name__ == '__main__':
    l = list(range(10))
    random.shuffle(l)

    s = SelectionSort(l)
    s.sort()

    print(s.list)
