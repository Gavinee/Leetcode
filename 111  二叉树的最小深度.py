"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

返回它的最小深度  2.
"""

__author__ = 'Qiufeng'


#初始程序:超过21.40%的python提交记录

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mindeep = []
        if root == None:
            return 0
        deep = 1
        self.dfs(root,deep,mindeep)        
        return min(mindeep)
                
    def dfs(self,root,deep,mindeep):
        if root !=None:
            if root.left == None and root.right == None:
                mindeep.append(deep)
                return 

            else:
                self.dfs(root.left,deep+1,mindeep)
                self.dfs(root.right,deep+1,mindeep)


#优化一  超过81.71%的python提交记录
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mindeep = []
        if root == None:
            return 0
        deep = 1
        self.dfs(root,deep,mindeep)        
        return mindeep[0]
                
    def dfs(self,root,deep,mindeep):
        if root !=None:
            if root.left == None and root.right == None:
                mindeep.append(deep)
                if len(mindeep)==2:
                    mindeep[0]=min(mindeep)
                    del mindeep[1]
                return 

            else:
                self.dfs(root.left,deep+1,mindeep)
                self.dfs(root.right,deep+1,mindeep)

#优化二  超过95.72%的python提交记录
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mindeep = [0]
        if root == None:
            return 0
        deep = 1
        self.dfs(root,deep,mindeep)        
        return mindeep[0]
                
    def dfs(self,root,deep,mindeep):
        if root !=None:
            if root.left == None and root.right == None:
                    if mindeep[0] == 0:
                        mindeep[0] = deep
                    else:
                        mindeep[0] = min(deep,mindeep[0])

            else:
                self.dfs(root.left,deep+1,mindeep)
                self.dfs(root.right,deep+1,mindeep)



