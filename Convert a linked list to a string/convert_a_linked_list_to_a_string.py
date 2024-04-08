class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def __repr__(self):
        return f'{self.data}->{repr(self.next)}'
def stringify(node):
    if node is None:
        return 'None' 
    all_data=[]
    while node.next:
        all_data.append(str(node.data))
        node =node.next
    if node.next is None:
        all_data.append(str(node.data))
        all_data.append("None")
        return " -> ".join(all_data)
