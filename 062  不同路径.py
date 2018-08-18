"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？

说明：m 和 n 的值均不超过 100。

示例 1:
输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

示例 2:
输入: m = 7, n = 3
输出: 28
"""
__author__ = 'Qiufeng'

#                    超时程序（递归形式）
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int    列       col
        :type n: int    行       row
        :rtype: int
        """
        rect= [m,n]
        count = [0]     #有count[0]种方案
        col = 0
        row = 0
        
        self.dynamicProgramming(count,col,row,rect)
        return count[0]
    
    def dynamicProgramming(self,count,col,row,rect):
        if col == rect[0]-1 and row == rect[1]-1:
            count[0] = count[0]+1
            return 
        
        if col <rect[0]-1:
            if row == rect[1]-1:
                count[0] = count[0]+1
                return
            else:
                self.dynamicProgramming(count,col+1,row,rect)
        if row <rect[1]-1:
            if col == rect[0]-1:
                count[0] = count[0]+1
            else:
                self.dynamicProgramming(count,col,row+1,rect)
