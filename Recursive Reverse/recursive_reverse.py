class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def __repr__(self):
        return f'{self.data}->{repr(self.next)}'
def reverse(head):
    def reverse_recursive(current, prev):
        if not current:
            return prev
        next_node = current.next
        current.next = prev
        return reverse_recursive(next_node, current)
    return reverse_recursive(head, None)