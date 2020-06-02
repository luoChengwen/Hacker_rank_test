'''
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root == None: return root

        def invert(root):
            if root.left != None or root.right != None:
                root.left, root.right = root.right, root.left

        queue = list()
        queue.append(root)

        while len(queue) > 0:
            node = queue.pop(0)
            invert(node)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return root
