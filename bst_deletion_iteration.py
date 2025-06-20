# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNextNode(self, node: TreeNode) -> (TreeNode, TreeNode):
        pre = node
        nextNode = node.right
        while nextNode.left:
            pre = nextNode
            nextNode = nextNode.left
        return pre, nextNode
    def findTheNode(self, root: TreeNode, key: int) -> (TreeNode, TreeNode):
        node = root
        pre = None
        while node and node.val != key:
            pre = node
            if key < node.val:
                node = node.left
            else:
                node = node.right
        return pre, node
    # assume the key is in the root
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        pre, node = self.findTheNode(root, key)
        if not node:
            return root
        # child has none
        if not ((node.left is not None) and (node.right is not None)):
            child = node.left or node.right
            if not pre:
                return child
            else:
                if pre.left == node:
                    pre.left = child
                else:
                    pre.right = child
                return root
        # node 2 children, replace it with the next value
        nextNodePre, nextNode = self.findNextNode(node)
        nextNode.left = node.left
        if node.val != nextNodePre.val:
            # print("not child")
            nextNodePre.left = nextNode.right
            nextNode.right = node.right
        if pre:
            if pre.left == node:
                pre.left = nextNode
            else:
                pre.right = nextNode
        else:
            root = nextNode
        return root
