class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root) -> list[int]:
    trav = []

    def inorder(node):
        if not node:
            return

        inorder(node.left)
        trav.append(node.val)
        inorder(node.right)

    inorder(root)

    return trav
    


node1 = TreeNode(val = 12)
node2 = TreeNode(val = 13)
node3 = TreeNode(val = 14)
node4 = TreeNode(val = 15)
node5 = TreeNode(val = 16)
node6 = TreeNode(val = 17)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
node2.left = node6
node2.right = TreeNode(18)

tree = node1

print(inorderTraversal(tree))
