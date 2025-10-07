

class StackBasedQueue():
    def __init__(self):
        self._InboundStack = []
        self._OutboundStack = []
        self._size = 0

    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = self._InboundStack[::-1]
        values.extend(self._OutboundStack)
        return f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(values)}]>'

    def enqueue(self, data):
        self._InboundStack.append(data)
        self._size += 1

    def dequeue(self):
        if not self._OutboundStack:
            while self._InboundStack:
                self._OutboundStack.append(self._InboundStack.pop())
        if not self._OutboundStack:
            return None
        self._size -= 1
        return self._OutboundStack.pop()
