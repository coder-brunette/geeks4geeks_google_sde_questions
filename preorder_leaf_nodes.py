class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert_into_bst(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert_into_bst(root.left, key)
    else:
        root.right = insert_into_bst(root.right, key)
    return root

def construct_bst_from_preorder(preorder):
    if not preorder:
        return None
    root = Node(preorder[0])
    for i in range(1, len(preorder)):
        insert_into_bst(root, preorder[i])
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right) 

# root = construct_bst_from_preorder([10, 5, 1, 7, 40, 50])
# inorder(root)

# O(N^2)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def construct_bst_from_preorder(preorder):
    if not preorder:
        return None

    root = Node(preorder[0])
    stack = [root]

    for i in range(1, len(preorder)):
        temp = None
        while stack and preorder[i] > stack[-1].key:
            temp = stack.pop()
        if temp:
            temp.right = Node(preorder[i])
            stack.append(temp.right)
        else:
            temp = stack[-1]
            temp.left = Node(preorder[i])
            stack.append(temp.left)

    return root

root = construct_bst_from_preorder([10, 5, 1, 7, 40, 50])
inorder(root)