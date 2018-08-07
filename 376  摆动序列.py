"""
如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。
第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。

例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负
交替出现的。相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，第一个序
列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。

给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删
除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。

示例1:
输入: [1,7,4,9,2,5]
输出: 6
解释: 整个序列就是一个摆动序列。

示例2:
输入: [1,17,5,10,13,15,10,5,16,8]
输出: 7
解释: 它的几个子序列满足摆动序列。其中一个是[1,17,10,13,10,16,8]。

示例3:
输入: [1,2,3,4,5,6,7,8,9]
输出: 2

进阶:
你能否用 O(n) 时间复杂度完成此题?

"""
__author__ = 'Qiufeng'

class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = True                                 
        #判断第一个元素和第二个元素做差后是正还是负 
        #temp = []         如果中间变量没有赋值，则temp = [] temp = nums  和temp = nums效果相同
        temp = nums
        temp.reverse()
        return max(tt(nums,flag),tt(temp,flag))     
        #来比较正序和倒序的最长子序列，取长的  

def tt(nums,flag):
    i = 1
    while i <len(nums):
        if i==1:
            differencing = nums[i] - nums[i-1]
            if differencing > 0:
                flag =True
            elif differencing<0:
                flag =False
            else:
                del nums[i-1]
                i = 1
                continue
                 
        if  i%2 == 1 :
            if flag ==True and nums[i] > nums[i-1]:
                i+=1
                continue
            elif flag ==False and nums[i] < nums[i-1]:
                i+=1
                continue
            else:
                del nums[i-1]
        else:
            if flag ==True and nums[i] < nums[i-1]:
                i+=1
                continue
            elif flag ==False and nums[i] > nums[i-1]:
                i+=1
                continue
            else :
                del nums[i-1]
                
    return len(nums)
        
        
