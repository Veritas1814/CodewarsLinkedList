class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def remove_duplicates(head):
    if head is None:
        return None
    current = head
    while current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head