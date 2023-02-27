# Author: Anthony Rafidison <benjaraf006@gmail.com>
import random


class QuickSort:
    def __init__(self, L: list[int|float]):
        self.list = L

    def sort(self):
        self.qsort(self.list, 0, len(self.list)-1)

    def qsort(self, l, imin, imax): # imin = index min, imax = index max
        if imax-imin == 1: # Test if there are only 2 elements in the list
            if l[imin] > l[imax]:
                l[imin], l[imax] = l[imax], l[imin] # Exchange the 2 elements
            return
        if imax-imin == 0: # Test if the list is empty
            return

        p = l[imax] # pivot
        a = 0 # Index of the last element smaller than the pivot
        for i in range(imin, imax):
            if l[i] <= p: # If the element is smaller than the pivot
                l[a+imin], l[i] = l[i], l[a+imin]
                a += 1
        l[a+imin], l[imax] = p, l[a+imin]
        if a != 0:
            self.qsort(l, imin, a+imin-1)
        if imax > a+imin+1:
            self.qsort(l, a+imin+1, imax)
        
if __name__ == '__main__':
    l = list(range(10))
    random.shuffle(l)

    s = QuickSort(l)
    s.sort()

    print(s.list)
