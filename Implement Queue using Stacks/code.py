class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self, head=None) -> None:
        self.head = head

    def push(self, value):
        n = Node(value)
        n.next = self.head
        self.head = n

    def pop(self):
        n = self.head.data
        self.head = self.head.next
        return n

    def reverse(self):
        st = Stack()
        head = self.head
        while head:
            st.push(head.data)
            head = head.next
        self.head = st.head


class MyQueue:

    def __init__(self):
        self.stack = Stack()

    def push(self, x: int) -> None:
        self.stack.push(x)

    def pop(self) -> int:
        if not self.stack.head:
            return None

        if not self.stack.head.next:
            n = self.stack.head.data
            self.stack.head = None
            return n

        self.stack.reverse()
        n = self.stack.pop()
        self.stack.reverse()
        return n

    def peek(self) -> int:
        if not self.stack.head:
            return None

        if not self.stack.head.next:
            return self.stack.head.data
        self.stack.reverse()
        n = self.stack.head.data
        self.stack.reverse()
        return n

    def empty(self) -> bool:
        return self.stack.head is None
