class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if not head or not head.next:
        raise ValueError
    head1 = head
    head2 = head.next
    curent1 = head1
    current2 = head2
    while curent1 and current2:
        if current2.next:
            curent1.next = current2.next
            curent1 = curent1.next
        else:
            curent1.next = None
            break
        if curent1.next:
            current2.next = curent1.next
            current2 = current2.next
        else:
            current2.next = None
            break
    return Context(head1, head2)