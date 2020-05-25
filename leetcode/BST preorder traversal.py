# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        stack = []
        root = None

        for val in preorder:
            node = TreeNode(val)
            if not root:
                root = node
            elif val < stack[-1].val:
                stack[-1].left = node
            else:
                while stack and val > stack[-1].val:
                    lastnode = stack.pop()
                lastnode.right = node

            stack.append(node)
        return root






