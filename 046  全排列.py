"""
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
__author__ = 'Qiufeng'

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(0,nums,res)
        return res

    def dfs(self,cur,nums,res):
        temp = []
        if cur == len(nums)-1:
            for i in nums:
                temp.append(i)
            res.append(temp)
            return

        for i in range(cur,len(nums),1):
            temp = [0]
            #swap(nums[cur],nums[i])
            temp[0] = nums[cur]
            nums[cur] = nums[i]
            nums[i] = temp[0]
            
            self.dfs(cur+1,nums,res)
            #swap(nums[cur],nums[i])
            temp[0] = nums[cur]
            nums[cur] = nums[i]
            nums[i] = temp[0]
            
