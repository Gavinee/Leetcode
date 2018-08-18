"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5
  
输出: ["1->2->5", "1->3"]
解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
"""
__author__ = 'Qiufeng'

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import copy
class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        route = []
        res = []
        temp =""
        rot = []
        self.allRoute(route,res,root)
        
        for i in range(0,len(route)):
            for j in range(0,len(route[i])):
                if j ==0:
                    temp = str(route[i][j])
                else:
                    temp = temp+"->"+str(route[i][j])
            rot.append(temp)
            temp = ""
        return rot
    
    
    def allRoute(self,route,res,root):
        if  root == None:
            return
        
        if res == []:
            res.append(root.val)
            
        if root.left == None and root.right == None:
            tt=copy.deepcopy(res)
            route.append(tt)
            return
        
        if root.left!=None:
            res.append(root.left.val)
            self.allRoute(route,res,root.left)
            del res[-1]
        
        if root.right!=None:
            res.append(root.right.val)
            self.allRoute(route,res,root.right)
            del res[-1]
        
