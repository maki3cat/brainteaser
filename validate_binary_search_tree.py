# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def recurBST(self, root:Optional[TreeNode], minV, maxV) -> bool:
#         # This is pre-order
#         # print(root and root.val, minV, maxV,"\n")
#         if root is None: return True
#         if (maxV is not None and root.val >= maxV) or (minV is not None and root.val <= minV):
#             return False
#         if root.left and root.left.val>=root.val:
#             return False 
#         if root.right and root.right.val <= root.val:
#             return False
#         # this part is nunanced
#         nextMax = root.val
#         if maxV is not None: nextMax = min(maxV, root.val)
#         leftIsBST = self.recurBST(root.left, minV, nextMax)
#
#         nextMin = root.val
#         if minV is not None: nextMin = max(minV, root.val)
#         rightIsBST = self.recurBST(root.right, nextMin, maxV)
#         return leftIsBST and rightIsBST

#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         return self.recurBST(root, None, None)

class Solution:
    def isValidBST(self, root: Optional[TreeNode], left=-inf, right=inf) -> bool:
        if root is None:
            return True
        x = root.val
        return left < x < right and \
               self.isValidBST(root.left, left, x) and \
               self.isValidBST(root.right, x, right)
# max(left, x) min(right, x) are also correct 
# but not necessary, because min(right, x) should be x for the first line x < right
# same for x > left

# https://leetcode.cn/problems/validate-binary-search-tree/

