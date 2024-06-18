"""

There are two approaches to this,
1 - BFS using queue
2 - DFS using recursion


BFS
---------------
1 - start with the root node in the queue with the starting height = 1
2 - pop the first element
3 - if the left node exists, enqueue it along with incremented height
4 - if the right node exists, enqueue it along with incremented height
5 - stop when you hit a leaf node or repeat till the queue is empty


DFS
--------------
1 - traverse till you hit a leaf, return 1 if leaf
2 - if left subtree doesnt exist, traverse right
3 - if right subtree doesnt exist, traverse left
4 - keep on adding 1 each time you move to the left subtree or the right subtree
5 - when you encounter an internal node, return the min(dfs(leftSubTree), dfs(rightSubTree))


"""

import collections


def minDepth(self, root:TreeNode) -> int:
    
    """ -------- BFS -----------
    if root is None:
        return 0
    
    # this queue has faster lookup time than list
    q = collections.deque()

    q.append((root, 1))

    while q:
        # popleft is just dequeue
        node, depth = q.popleft()

        # return depth if we hit a leaf node
        if not node.left and not node.right:
            return depth
    
        # if left child exists, increment depth and append it 
        if node.left:
            q.append((node.left, depth + 1))
        
        # if right child exists, increment the depth and append it
        if node.right :
            q.append((node.right, depth + 1))
        
        """

    if not root:
        return 0
    
    # leaf node
    if not root.right and not root.left:
        return 1

    # left child exists, right doesnt
    if root.left and not root.right:
        return 1 + self.minDepth(root.left)
    
    # right child exists, left doesnt
    if root.right and not root.left:
        return 1 + self.minDepth(root.right)
    
    # internal node
    if root.right and root.left:
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))