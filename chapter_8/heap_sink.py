class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        # Start at the end of the heap
        index = self._size - 1
        # Calculate index of parent element
        parent_index = (index - 1) // 2
        # While not at Root node and value less than its parent
        while index > 0 and self._heap[index] < self._heap[parent_index]:
            # swap value with its parent
            self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
            # Update indices
            index = parent_index
            parent_index = (index - 1) // 2

    def insert(self, value):
        # Add the value to the heap
        self._heap.append(value)
        # Update size of the heap
        self._size += 1
        # And float the last element of the heap
        self._float()

    def _sink(self):
        """
        Sinks the root node of the heap until the heap is in order
        """
        if self._size <= 1:
            return
        current_index = 0

        while True:
            left_child = 2 * current_index + 1
            right_child = 2 * current_index + 2
            smallest = current_index

            if left_child < self._size and self._heap[left_child] < self._heap[smallest]:
                smallest = left_child
            if right_child < self._size and self._heap[right_child] < self._heap[smallest]:
                smallest = right_child

            if smallest != current_index:
                self._heap[current_index], self._heap[smallest] = (
                    self._heap[smallest],
                    self._heap[current_index]
                )
                current_index = smallest
            else:
                break
