"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
"""
__author__ = 'Qiufeng'

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        front = 0                 #前指针
        behind = len(height)-1    #后指针
        max1Area = []
        length = 0
        max1 = 0
        
        while((front<len(height)-1 and behind > 0)and behind >front):
            length = behind - front
            max1Area.append(length*min(height[front],height[behind]))
            if height[front]>height[behind]:
                behind = behind - 1
            else :
                front = front + 1 
            
        for i in range(0,len(max1Area),1):
            if max1<max1Area[i] :
                max1 = max1Area[i]
        return max1
            



