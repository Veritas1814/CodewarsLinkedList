class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def sorted_insert(head, data):
    all_data=[]
    if head is None:
        return Node(data)
    while head.next:
        all_data.append(head.data)
        head =head.next
    if head.next is None:
        all_data.append(head.data)
        all_data.append(data)
    new_data=sorted(all_data)
    new_data.append(None)
    current=None
    for i in new_data[-2::-1]:
        a=Node(i)
        a.next=current
        current= a
    return current