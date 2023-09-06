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


player_first = str(input()).split()
player_second = str(input()).split()
p1 = list(map(lambda x: int(x), player_first))
p2 = list(map(lambda x: int(x), player_second))
i = 0
n = len(p1)
deck1 = Queue()
deck2 = Queue()
for j in range(n):
    map1 = QueueObj(p1[j])
    map2 = QueueObj(p2[j])
    deck1.push(map1)
    deck2.push(map2)
while i < 10 ** 6 and (deck1.size() != 0 and deck2.size() != 0):
    map1 = deck1.front()
    map2 = deck2.front()
    i += 1
    if (map1 == 0 and map2 == 9) or ((map1 != 9 or map2 != 0) and map1 > map2):
        one = deck1.pop()
        two = deck2.pop()
        deck1.push(QueueObj(one))
        deck1.push(QueueObj(two))
    else:
        one = deck1.pop()
        two = deck2.pop()
        deck2.push(QueueObj(one))
        deck2.push(QueueObj(two))


if deck1.size() == 0:
    print('second', i)
elif deck2.size() == 0:
    print('first', i)
else:
    print('botva')
