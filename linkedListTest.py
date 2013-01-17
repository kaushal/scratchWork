class Node: 
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next
    def __str__(self):
        return str(self.cargo)

node1 = Node('hello')
node2 = Node('this')
node3 = Node('is')
node1.next = node2
#node2.next = node3

temp = node1

while temp is not None:
    print temp.cargo
    temp = temp.next
