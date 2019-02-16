from random import randrange


class MinHeap:

    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    # Heap Helper Methods
    # DO NOT CHANGE

    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            print("There is only a left child")
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child < right_child:
                print("Left child is smaller")
                return self.left_child_idx(idx)
            else:
                print("Right child is smaller")
                return self.right_child_idx(idx)

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count

    # End of Helper Methods

    def retrieve_min(self):
        if self.count == 0:
            print("No items in heap")
            return None

        min = self.heap_list[1]
        print("Removing: {0} from {1}".format(min, self.heap_list))
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        print("Last element moved to first: {0}".format(self.heap_list))
        self.heapify_down()
        return min

    def heapify_up(self):
        print("Heapifying Up...")
        idx = self.count
        swap_count = 0
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]

            if parent > child:
                print("Swapping {0} with {1}".format(parent, child))
                swap_count += 1
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child

            idx = self.parent_idx(idx)

        print("Heap Restored! {0} with {1}".format(self.heap_list, swap_count))

    def heapify_down(self):

        idx = 1
        swap_count = 1
        while self.child_present(idx):
            print("Heapifying down...")
            smaller_child_idx = self.get_smaller_child_idx(idx)
            child = self.heap_list[smaller_child_idx]
            parent = self.heap_list[idx]
            if parent > child:
                swap_count += 1
                self.heap_list[idx] = child
                self.heap_list[smaller_child_idx] = parent

            idx = smaller_child_idx
            print("Heap Restored! {0} with {1} swaps".format(self.heap_list, swap_count))

    def add(self, element):
        print("Adding {0} to {1}".format(element, self.heap_list))
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()




#TEST AREA

min_heap = MinHeap()


# populate with random numbers
random_nums = [randrange(1, 101) for n in range(6)]
for el in random_nums:
    min_heap.add(el)
#min_heap.heap_list = [None, 10, 13, 21, 61, 22, 23, 99]
#min_heap.count = 7

print(min_heap.heap_list)
min_heap.add(7)
min_heap.add(12)
min_heap.add(42)
print(min_heap.retrieve_min())

print("The smaller child of index 1 is: ")
smaller_child_of_idx_1 = min_heap.get_smaller_child_idx(1)
print(smaller_child_of_idx_1)
smaller_child_element = min_heap.heap_list[smaller_child_of_idx_1]
print(smaller_child_element)

print("The smaller child of index 2 is: ")
smaller_child_of_idx_2 = min_heap.get_smaller_child_idx(2)
print(smaller_child_of_idx_2)
smaller_child_element = min_heap.heap_list[smaller_child_of_idx_2]
print(smaller_child_element)

print("The smaller child of index 3 is: ")
smaller_child_of_idx_3 = min_heap.get_smaller_child_idx(3)
print(smaller_child_of_idx_3)
smaller_child_element = min_heap.heap_list[smaller_child_of_idx_3]
print(smaller_child_element)