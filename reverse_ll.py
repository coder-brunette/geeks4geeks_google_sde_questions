class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_linked_list(head):
    curr = head
    next = None
    prev = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
    return head
    
head = Node(1)
head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)

# Reverse the linked list
head = reverse_linked_list(head)

while head is not None:
    print(head.value, end=" ")
    head = head.next