"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

说明:
如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
"""
__author__ = 'Qiufeng'
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        right = 0
        left = 1
        temp1 = []
        temp2= []
        
        if root == None:
            return True
        
        temp1.append(root.val)
        temp2.append(root.val)
        self.dfs(root,temp1,right)
        self.dfs(root,temp2,left)
        
        if len(temp1)==len(temp2):
            for i in range(0,len(temp1),1):
                if temp1[i] !=temp2[i]:
                    return False
            return True
        else:
            return False
        
        
    def dfs(self,root,temp,direct):
        tt = []
        tt = root
        if root.left==None and root.right == None:
            return 
        
        if direct == 1:                 #左
            if root.left !=None:
                root = root.left
                temp.append(root.val)
                self.dfs(root,temp,direct)
                root = tt
            else:
                temp.append(None)
            
            if root.right!=None:
                root = root.right
                temp.append(root.val)
                self.dfs(root,temp,direct)
                root = tt
            else:    
                temp.append(None)
                
        if direct == 0:                 #右
            if root.right!=None:
                root = root.right
                temp.append(root.val)
                self.dfs(root,temp,direct)
                root = tt
            else:    
                temp.append(None)
            if root.left !=None:
                root = root.left
                temp.append(root.val)
                self.dfs(root,temp,direct)
                root = tt
            else:
                temp.append(None)      
            



