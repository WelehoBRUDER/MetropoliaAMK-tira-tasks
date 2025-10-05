class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def peek(self):
        """
        Returns the value of the top node without altering the stack
        """
        return self._top.data if self._top else None

    def push(self, data):
        """
        Add an element to the stack

        Parameters:
        - 'data': Data/value being added

        Returns: None
        """

        new_node = Node(data)
        new_node.next = self._top
        self._top = new_node
        self._size += 1

    def pop(self):
        """
        Remove the top node from the stack and return its content

        Parameters: None

        Returns: The content of the node or None if stack is empty
        """

        if not self._top:
            return None

        value = self._top.data
        self._top = self._top.next
        self._size -= 1
        return value

    def __repr__(self):
        curr = self._top
        values = []
        while curr:
            values.append(str(curr.data))
            curr = curr.next
        s = "s" if self._size != 1 else ""
        return f"<Stack ({self._size} element{s}): [{', '.join(values)}]>"

