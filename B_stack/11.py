class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top == None:
            self.top = obj
        else:
            node = self.top
            self.top = obj
            obj.prev = node
        return 'ok'

    def pop(self):
        if self.top != None:
            node = self.top
            self.top = node.prev
            return node.value
        else:
            return 'error'

    def back(self):
        if self.top != None:
            return self.top.value
        else:
            return 'error'

    def size(self):
        if self.top == None:
            return 0
        length = 1
        node = self.top
        while node.prev != None:
            node = node.prev
            length += 1
        return length

    def clear(self):
        self.top = None
        return 'ok'

    def exit(self):
        return 'bye'


class StackObj:
    def __init__(self, value):
        self.value = value
        self.prev = None


s = ''
stack = Stack()
data = {
    'push': stack.push,
    'pop': stack.pop,
    'back': stack.back,
    'size': stack.size,
    'clear': stack.clear,
    'exit': stack.exit
}
while s != 'exit':
    s = str(input()).split()
    function = data[s[0]]
    if len(s) > 1:
        value = s[1]
        print(function(StackObj(value)))
    else:
        if s[0] == 'exit':
            print(function())
            s = 'exit'
        else:
            print(function())
