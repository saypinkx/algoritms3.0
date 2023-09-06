class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top is None:
            self.top = obj
        else:
            node = self.top
            self.top = obj
            obj.prev = node
        return 'ok'

    def pop(self):
        if self.top is not None:
            node = self.top
            self.top = node.prev
            return node.value
        else:
            return 'error'

    def back(self):
        if self.top is not None:
            return self.top.value
        else:
            return 'error'

    def size(self):
        if self.top is None:
            return 0
        length = 1
        node = self.top
        while node.prev is not None:
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


stack = Stack()

string = str(input())

for char in string:
    if char == ')' and stack.back() == '(':
        stack.pop()
    elif char == ']' and stack.back() == '[':
        stack.pop()
    elif char == '}' and stack.back() == '{':
        stack.pop()
    else:
        stack.push(StackObj(char))

if stack.size() == 0:
    print('yes')
else:
    print('no')
