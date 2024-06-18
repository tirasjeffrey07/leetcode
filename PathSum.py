"""
Leetcode 112

given a target, check if the given binary tree has a root-to-leaf path where the sum of all the values of the nodes in that path is equal to the target sum

only approach = visit all root-to-leaf path and check if the sum is equal to the target

at each leaf node, check if the current Sum == target Sum

do dfs and get all the root-to-leaf paths, keep on adding the values of the node to the current sum

"""


def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, currSum):
            
            # empty tree so return False
            if not node:
                return False

            # each time, update the current sum
            currSum += node.val

            # if leaf node, check if the currSum == target
            if not node.left and not node.right:
                return currSum == targetSum
            
            #      visit left children first    visit right children
            return (dfs(node.left, currSum)) or (dfs(node.right, currSum))
        
        return dfs(root, 0)