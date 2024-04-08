class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def __repr__(self):
        return f'{self.data}->{repr(self.next)}'
def get_nth(node, index):
    if node is None:
        raise ValueError
    all_data=[]
    while node.next:
        all_data.append(str(node.data))
        node =node.next
    all_data.append(str(node.data))
    if index<0 or index>=len(all_data):
        raise ValueError
    return Node(int(all_data[index]))