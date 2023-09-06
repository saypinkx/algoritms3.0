class Queue:
    def __init__(self):
        self.head = None

    def push(self, obj):
        if self.head is None:
            self.head = obj
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = obj
        return 'ok'

    def pop(self):
        if self.head is not None:
            node = self.head
            self.head = node.next
            return node.value

        else:
            return 'error'

    def front(self):
        if self.head is not None:
            return self.head.value
        else:
            return 'error'

    def size(self):
        length = 0
        node = self.head
        if node is not None:
            while node is not None:
                length += 1
                node = node.next

        return length

    def clear(self):
        self.head = None
        return 'ok'

    def exit(self):
        return 'bye'


class QueueObj:
    def __init__(self, value=None):
        self.value = value
        self.next = None


queue = Queue()
data = {
    'push': queue.push,
    'pop': queue.pop,
    'front': queue.front,
    'size': queue.size,
    'clear': queue.clear,
    'exit': queue.exit
}
s = ''
while s != 'exit':
    s = str(input())
    mass = s.split()
    func = data[mass[0]]
    if len(mass) == 1:
        print(func())
    else:
        elem = int(mass[1])
        print(func(QueueObj(elem)))

