class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def __repr__(self):
        return f'{self.data}->{repr(self.next)}'
class Context:
    def __init__(self, first, second):
        self.first = first
        self.second = second
def move_node(source, dest):
    if not source:
        raise ValueError
    new_source=source.next
    new_dest=Node(source.data,dest)
    return Context(new_source, new_dest)