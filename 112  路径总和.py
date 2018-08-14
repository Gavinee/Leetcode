"""
"""
__author__ = 'Qiufeng'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        sum1 = []
        list1 = []
        if root == None:
            if sum == None:
                return True
            else:
                return False
        
        sum1.append(root.val)
        self.dfs(root,sum1,list1)
        
        for i in list1:
            if i == sum:
                return True
        return False
            
        
        
    def dfs(self,root,sum1,list1):
        temp = 0
        if root.left == None and root.right == None:
            for i in sum1:
                temp+=i
            list1.append(temp)
            
        else:
            if root.left!=None:
                sum1.append(root.left.val)
                self.dfs(root.left,sum1,list1)
                del sum1[len(sum1)-1]
            if root.right!=None:
                sum1.append(root.right.val)
                self.dfs(root.right,sum1,list1)
                del sum1[len(sum1)-1]




