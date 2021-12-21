class Node:
    def __init__(self):
        self.value = None
        self.next = None

def find(node, element):
    if node.value == element:
        return True
    if node.next == None:
        return False
    return find(node.next, element)