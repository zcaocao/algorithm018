"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack,  ans = [root, ], []
        while stack:
            root = stack.pop()
            ans.append(root.val)
            stack.extend(root.children[::-1])
        return ans
