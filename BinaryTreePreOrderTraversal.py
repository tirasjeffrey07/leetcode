"""
This solution uses an iterative solution not the easier recursive solution
Refer neetcode.io on Youtube

"""




class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def preorderTraversal(root) -> list[int]:

        cur = root
        res, stack = [], []

        # termination condition is cur pointing to None and Stack being empty
        while cur or stack:

            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()

        return res


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

print(preorderTraversal(tree))
