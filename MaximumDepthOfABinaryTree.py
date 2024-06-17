def maxDepth(root) -> int:
        
    def getDepth(node):
        # just return the height of the tree

        if node is None:              # base case
                return 0

        # find the maximum height bw left and right sub trees
        return 1 + max(getDepth(node.left), getDepth(node.right))

    return getDepth(root)
