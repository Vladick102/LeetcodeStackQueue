class FreqNode:
    def __init__(self, data, freq=1) -> None:
        self.data = data
        self.freq = freq
        self.next = None


class FreqStack:
    def __init__(self, head=None) -> None:
        self.head = head

    def push(self, value):
        head = self.head
        c = 1
        while head:
            if head.data == value:
                c = head.freq + 1
                break
            head = head.next
        n = FreqNode(value, c)
        n.next = self.head
        self.head = n

    def pop(self):
        max_freq, max_freq_val = 0, None
        head = self.head
        while head:
            if head.freq > max_freq:
                max_freq = head.freq
                max_freq_val = head.data
            head = head.next

        head = self.head
        if head.data == max_freq_val:
            self.head = self.head.next
            return max_freq_val
        else:
            while head.next:
                if head.next.data == max_freq_val:
                    head.next = head.next.next
                    return max_freq_val
                head = head.next
