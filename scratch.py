from tree import Node

Bob = Node("Bob")
Marni = Node("Marni")
Declan = Node("Declan")

Bob.add_child(Marni)
Bob.add_child(Declan)

Declan.parent = Bob
Declan.parent = Marni

print('Bob\'s children:  ', Bob.children)
print('Marni\'s parent:  ', Marni.parent)
print('Marni\'s children:  ', Marni.children)
print('Declan\'s parent:  ', Declan.parent)
print('Declan\'s children:  ', Declan.children)
