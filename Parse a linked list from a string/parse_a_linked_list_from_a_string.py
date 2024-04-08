class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next
def linked_list_from_string(s):
    if "->" not in s:
        return None
    new_s=s.split(" -> ")
    if any(new_s) is False:
        return Node(None)
    current=None
    for i in new_s[-2::-1]:
        current= Node(int(i),current)
    return current
