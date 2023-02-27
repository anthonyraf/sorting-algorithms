from bubble_sort.bubble_sort import BubbleSort
from selection_sort.selection_sort import SelectionSort
from quick_sort.quick_sort import QuickSort

import random

if __name__ == '__main__':
    l = list(range(10))
    random.shuffle(l)

    qs = QuickSort(l).sort()
    ss = SelectionSort(l).sort()
    bs = BubbleSort(l).sort()

    print(qs)
    print(ss)
    print(bs)
    
