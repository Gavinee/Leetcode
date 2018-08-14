"""
给定一个二叉树，返回它的中序遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
"""
__author__ = 'Qiufeng'

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        list1 = []
        self.traversal(root,list1)
        return list1
    
    def traversal(self,root,list1):
        if root == None:
            return 
        
        else:
            self.traversal(root.left,list1)
            list1.append(root.val)
            self.traversal(root.right,list1)
