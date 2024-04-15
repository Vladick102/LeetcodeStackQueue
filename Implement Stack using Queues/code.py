class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Queue:
    def __init__(self, head=None) -> None:
        self.head = head

    def push(self, value):
        n = Node(value)
        n.next = self.head
        self.head = n

    def pop(self):
        head = self.head
        if head is None:
            return None

        if head.next is None:
            data = head.data
            self.head = None
            return data

        while head.next:
            if head.next.next is None:
                data = head.next.data
                head.next = None
                return data
            head = head.next


class MyStack:

    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        self.queue.push(x)

    def pop(self) -> int:
        data = self.queue.head.data
        self.queue.head = self.queue.head.next
        return data

    def top(self) -> int:
        if self.queue.head:
            return self.queue.head.data
        else:
            None

    def empty(self) -> bool:
        return self.queue.head is None


def stringify(queue):
    l = []
    node = queue.head
    while node:
        l.append(str(node.data))
        node = node.next
    return " -> ".join(l + ["None"])
