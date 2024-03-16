
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def nth_node_from_end(head, n):
    if not head:
        return None
    first = head
    second = head

    for _ in range(n):
        if not second:
            return None
        second = second.next

    while second.next:
        first = first.next
        second = second.next

    return first.value

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

print(nth_node_from_end(head,4))