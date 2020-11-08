# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuildTree(pre_start: int, pre_end: int, in_start: int, in_end: int):
            if pre_start > pre_end:
                return None
            # root index
            pre_root = pre_start
            in_root = index[preorder[pre_root]]
            # build root
            root = TreeNode(preorder[pre_root])
            # length of left tree
            left_size = in_root - in_start
            # recursively build left and right tree
            root.left = myBuildTree(pre_start + 1, pre_start + left_size, in_start, in_root - 1)
            root.right = myBuildTree(pre_start + left_size + 1, pre_end, in_root + 1, in_end)
            return root

        n = len(preorder)
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)

