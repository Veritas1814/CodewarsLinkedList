class Node:
    def __init__(self, next=None):
        self.next = next
def swap_pairs(head):
    if not head or not head.next:
        return head
    current = Node()
    current.next = head
    priv = current
    while priv.next and priv.next.next:
        node1 = priv.next
        node2 = node1.next
        node1.next = node2.next
        node2.next = node1
        priv.next = node2
        priv = node1
    return current.next