class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def parent(self):
        return self._parent

    @property
    def children(self):
        return self._children

    def add_child(self, node):
        if node not in self._children:
            self._children.append(node)

    @parent.setter
    def parent(self, node):
        self._parent = node
        
    def __repr__(self):
        return f'<Node val={self._value}>'