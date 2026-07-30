

class PriorityQueue:
    def __init__(self,elements:list[int] | None = None):
        self.heap = elements[:] if elements else []


    def pop(self):
        if self.isEmpty():
            raise ValueError("Priority queue is empty")
        heap = self.heap
        root = heap[0]
        last  = heap.pop()

        if not self.isEmpty():
            heap[0] = last
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
        heap = self.heap
        while index > 0:
            root_index = (index - 1) // 2

            if heap[root_index] > heap[index]:
                heap[root_index], heap[index] = heap[index], heap[root_index]
                index = root_index
            else:
                break

        return self.heap



    def heapify_down(self):

        index  = 0
        heap = self.heap
        while index < len(heap):

            left = 2 * index  + 1
            right = 2 * index + 2

            if left >= len(heap):
                break

            smaller_child = left
            if right < len(heap) and heap[right] < heap[left]:
                smaller_child = right
            if heap[index] <= heap[smaller_child]:
                break

            heap[index], heap[smaller_child] = (
                heap[smaller_child], heap[index]
            )
            index = smaller_child
        return heap

    def isEmpty(self):
        return len(self.heap) == 0

        