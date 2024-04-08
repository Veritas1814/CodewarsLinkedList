class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def __repr__(self):
        return f'{self.data}->{repr(self.next)}'
def loop_size(node):
    seen={}
    while not node in seen:
        seen[node]=1
        node=node.next
    curr=node.next
    looplen=1
    while curr!=node:
        curr=curr.next
        looplen+=1
    return looplen
