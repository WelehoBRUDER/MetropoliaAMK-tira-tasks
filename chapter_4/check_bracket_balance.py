class Stack:
    pass


def check_balance(text):
    pairs = {")": "(", "}": "{", "]": "["}
    stack = Stack()
    count = 0

    for index, char in enumerate(text):
        if char in "([{":
            stack.push((char, index))
        elif char in ")]}":
            if stack._size == 0:
                return f"Match error at position {index}"
            top, pos = stack.pop()
            if pairs[char] != top:
                return f"Match error at position {index}"
            count += 1

    if not stack._size == 0:
        _, pos = stack.pop()
        return f"Match error at position {pos}"

    return f"Ok - {count}"
