"""
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:
输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true

示例 2:
输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false

示例 3:
输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false
"""
__author__ = 'Qiufeng'

#此程序是来自CSDN用户bdpyjp的，https://blog.csdn.net/IT_job/article/details/80215141


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if p and q and p.val==q.val:
            l=self.isSameTree(p.left,q.left)
            r=self.isSameTree(p.right,q.right)
            return l and r#and操作，需要l与r皆为true时，才返回真。只用最后一次递归边界return值
        else:
            return False
