# https://leetcode.com/problems/validate-binary-search-tree/

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        leftLst = []
        rightLst = []

        self.sortedTree(root.left, leftLst)
        self.sortedTree(root.right, rightLst)

        if len(leftLst) > 0 and max(leftLst) >= root.val:
            return False
        if len(rightLst) > 0 and min(rightLst) <= root.val:
            return False

        left = self.isValidBST(root.left)
        right = self.isValidBST(root.right)

        return left and right

    def sortedTree(self, root, lst):
        if root == None:
            return

        self.sortedTree(root.left, lst)
        lst.append(root.val)
        self.sortedTree(root.right, lst)
