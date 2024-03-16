class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def height_of_binary_tree(root):

    if root is None:
        return 0
    
    else:
        ldepth = height_of_binary_tree(root.left)
        rdepth = height_of_binary_tree(root.right)

        if ldepth > rdepth:
            return ldepth + 1
        else:
            return rdepth +1 
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Height of tree is %d" % (height_of_binary_tree(root)))