class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        """
        Float the last element of the heap until the heap is in order
        """
        if self._size == 1:
            return
        current_index = self._size - 1
        while current_index > 0:
            parent_index = (current_index - 1) // 2
            if self._heap[current_index] < self._heap[parent_index]:
                self._heap[current_index], self._heap[parent_index] = (
                    self._heap[parent_index],
                    self._heap[current_index],
                )
                current_index = parent_index
            else:
                break
