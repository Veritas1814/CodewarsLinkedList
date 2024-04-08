class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def push(head, data):
    if head is None:
        return Node(data)
    a=Node(data)
    a.next=head
    return a
def build_one_two_three():
    head=Node(1)
    curent=head
    for i in range(2,4):
        curent.next=Node(i)
        curent=curent.next
    return head