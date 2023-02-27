from bubble_sort.bubble_sort import BubbleSort
from selection_sort.selection_sort import SelectionSort
from quick_sort.quick_sort import QuickSort

import random

if __name__ == '__main__':
    l = list(range(10))
    random.shuffle(l)

    qs = QuickSort(l)
    qs.sort()
    
    ss = SelectionSort(l)
    ss.sort()
    
    bs = BubbleSort(l)
    bs.sort()

    print(qs)
    print(ss)
    print(bs)

