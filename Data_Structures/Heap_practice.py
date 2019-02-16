from random import randrange
from Data_Structures.min_heap import MinHeap

# INSTANCE
min_heap = MinHeap()

# populate min_heap with random numbers
random_nums = [randrange(1, 101) for n in range(3)]
for el in random_nums:
    min_heap.add(el)


# remove minimum until min_heap is empty
while min_heap.count != 0:
    min_heap.retrieve_min()

