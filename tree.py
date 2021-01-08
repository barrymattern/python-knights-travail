class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self, node):
        if node not in self._children:
            self._children.append(node)
            node.parent = self

    def remove_child(self, node):
        if node in self._children:
            self._children.remove(node)
            node.parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if self._parent:
            self._parent.remove_child(self)
        if node:
            node.add_child(self)
        self._parent = node

    def depth_search(self, value):
        if self.value == value:
            return self
        for node in self.children:
            new_node = node.depth_search(value)
            if new_node:
                return new_node
        return

    def breadth_search(self, value):
        queue = [self]
        while len(queue) > 0:
            node = queue.pop(0)
            if node.value == value:
                return node
            queue += node.children
        return

    def __repr__(self):
        return f'<Node val={self._value}>'
