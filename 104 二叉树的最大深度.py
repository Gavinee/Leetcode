"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7

返回它的最大深度 3 。
"""
__author__ = 'Qiufeng'

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        deepMax = []                    #最大深度
        deep = 1
        maxn = 0
        if root == None:
            return 0
        self.dfs(root,deepMax,deep)
        for i in deepMax:
            if i>maxn:
                maxn = i
        return maxn
        
    def dfs(self,root,deepMax,deep):
        temp = root
        if root.left == None and root.right == None:
            deepMax.append(deep)
            return 
        
        if root.left!=None:
            root = root.left
            deep+=1
            deepMax.append(deep)
            self.dfs(root,deepMax,deep)
            deep-=1
            root = temp
        if root.right!=None:
            root = root.right
            deep+=1
            deepMax.append(deep)
            self.dfs(root,deepMax,deep)
            deep-=1
            root = temp
