class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leafSimilar(self, root1: [TreeNode], root2: [TreeNode]) -> bool:
    def dfs(root, leaves):
        # if root is empty
        if not root:
            return
        # if the left and right child of the node is empty
        if not root.left and not root.right:
            leaves.append(root.val)
            return
        #traverse left first then right
        dfs(root.left,leaves)
        dfs(root.right,leaves)
    
    leaves1, leaves2 = [], []
    dfs(root1, leaves1)
    dfs(root2, leaves2)

    return leaves1 == leaves2        