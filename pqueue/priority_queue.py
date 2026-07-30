

class PriorityQueue:
    def __init__(self,elements:list[int]):
        self.heap = elements


    def pop(self):
        if self.isEmpty():
            raise ValueError("Priority queue is empty")
        root = self.heap[0]
        last  = self.heap.pop()

        if not self.isEmpty():
            self.heap[0] = last
            self.heapify_down()

        return root




    def insert(self,element:int):
        self.heap.append(element)
        self.heapify_up()


    def peek(self):
        if self.isEmpty():
            raise ValueError("Priority queue is empty")
        return self.heap[0]

    def __str__(self):
        return str(self.heap)
    def __len__(self):
        return len(self.heap)

    def heapify_up(self):
        if self.isEmpty():
            raise ValueError("Priority queue is empty")


        index = len(self.heap) - 1
        while index > 0:
            root_index = (index - 1) // 2

            if self.heap[root_index] > self.heap[index]:
                self.heap[root_index], self.heap[index] = self.heap[index], self.heap[root_index]
                index = root_index
            else:
                break

        return self.heap



    def heapify_down(self):

        index  = 0

        while index < len(self.heap):

            left = 2 * index  + 1
            right = 2 * index + 2

            if left >= len(self.heap):
                break

            smaller_child = left
            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                smaller_child = right
            if self.heap[index] <= self.heap[smaller_child]:
                break

            self.heap[index], self.heap[smaller_child] = (
                self.heap[smaller_child], self.heap[index]
            )
            index = smaller_child
        return self.heap

    def isEmpty(self):
        return len(self.heap) == 0

        