class Heap:
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def insert(self, obj):
        node = self.root
        if node is None:
            node = obj



    def extract(self):
        pass




class HeapObj:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value
        self.parent = None
