"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为6。

进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""
__author__ = 'Qiufeng'

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        value        -2       1     -3        4      -1        2       1       -5        4
            i         1       2      3        4       5        6       7       8         9   
          max        -2       1      1        4       4        5       6       6         6    
          子解       [0]      [1]    [1]      [4]     [4]      [4:6]  [4:7]   [4:7]     [4:7]
        最优子解     -2        1     -2        4       3        5       6       1        5
        """
        substructure = [] #最优子结构
        tt = 1
        self.dynamicProgramming(tt,nums,substructure)
        maxValue =  substructure[0]
        for i in substructure:
            if maxValue < i:
                maxValue = i
        return maxValue
        
    def dynamicProgramming(self,tt,nums,substructure):
        if tt == len(nums):
            if len(nums) == 1:
                substructure.append(nums[tt-1])
            return
        if tt == 1:
            substructure.append(nums[0])
        
        substructure.append(max(substructure[tt-1]+nums[tt],nums[tt])) 
        self.dynamicProgramming(tt+1,nums,substructure)
