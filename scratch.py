from tree import Node

n1 = Node("n1")
n2 = Node("n2")
n3 = Node("n3")

n1.add_child(n2)
n1.add_child(n2)
n1.add_child(n3)

print(n1.children)
print(n2.parent == n1)