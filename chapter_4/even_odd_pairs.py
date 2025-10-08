def get_pairs(numbers):
    even_queue = Queue()
    odd_queue = Queue()
    pairs = []

    for num in numbers:
        if num % 2 == 0:
            if odd_queue._size > 0:
                odd_num = odd_queue.dequeue()
                pairs.append((num, odd_num))
            else:
                even_queue.enqueue(num)
        else:
            if even_queue._size > 0:
                even_num = even_queue.dequeue()
                pairs.append((even_num, num))
            else:
                odd_queue.enqueue(num)
    return pairs


class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __repr__(self):
        plural = "" if self._size == 1 else "s"
        values = []
        current = self._head
        while current is not None:
            values.append(current.data)
            current = current.next
        return f"<Queue ({self._size} element{plural}): [{", ".join(values)}]>"

    def enqueue(self, data):
        new_node = ListNode(data)
        if self._head is None:
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._size += 1

    def dequeue(self):
        if self._tail is None:
            return None
        data = self._tail.data
        if self._head == self._tail:
            self._tail = None
            self._head = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None
        self._size -= 1
        return data


class ListNode:
    pass