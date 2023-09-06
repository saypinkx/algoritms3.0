class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, obj):
        if self.head is None:
            self.head = obj
        else:
            obj.next = self.head
            self.head = obj
        return 'ok'

    def push_back(self, obj):
        if self.head is None:
            self.head = obj
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = obj
        return 'ok'

    def pop_front(self):
        if self.head is None:
            return 'error'
        else:
            node = self.head
            self.head = node.next
            return node.value

    def pop_back(self):
        if self.head is None:
            return 'error'
        else:
            node = self.head
            if node.next is None:
                result = self.head
                return result.value
            else:
                while node.next.next is not None:
                    node = node.next
                result = node.next
                node.next = None
                return result.value

    def front(self):
        if self.head is None:
            return 'error'
        else:
            return self.head.value

    def back(self):
        if self.head is None:
            return 'error'
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            return node.value

    def size(self):
        length = 0
        if self.head is not None:
            node = self.head
            while node is not None:
                length += 1
                node = node.next
        return length

    def clear(self):
        self.head = None
        return 'ok'

    def exit(self):
        return 'bye'


class DequeObj:
    def __init__(self, value):
        self.next = None
        self.value = value


deque = Deque()
data = {
    'push_front': deque.push_front,
    'push_back': deque.push_back,
    'pop_front': deque.pop_front,
    'pop_back': deque.pop_back,
    'front': deque.front,
    'back': deque.back,
    'size': deque.size,
    'clear': deque.clear,
    'exit': deque.exit
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
        print(func(DequeObj(elem)))