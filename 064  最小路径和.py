"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""
__author__ = 'Qiufeng'

"""
输入二维数组
  [1,3,1],
  [1,5,1],
  [4,2,1]
  
走到当前数组元素的最小数字之和(最优子解)
  [1,4,5],
  [2,7,6],
  [6,8,7]
  
  该解中包含重叠问题，采用minValue[row][col] = min(minValue[row-1][col]+grid[row][col],minValue[row][col])来更新最小值
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        col = 0             #列
        row = 0             #行
        minValue = []
        for i in range(0,len(grid),1):
            minValue.append([])
            for j in range(0,len(grid[0]),1):
                minValue[i].append(-1)
        for row in range(0,len(grid),1):
            for col in range(0,len(grid[0]),1):    
                self.dynamicProgramming(row,col,grid,minValue)
        return minValue[len(grid)-1][len(grid[0])-1]
    
    def dynamicProgramming(self,row,col,grid,minValue):
        if row + col == 0:
            minValue[0][0] = grid[0][0]
            return
            
        if row < len(grid) and row > 0:        #行边界
            if minValue[row][col] == -1:
                minValue[row][col] = minValue[row-1][col]+grid[row][col]
            else:
                minValue[row][col] = min(minValue[row-1][col]+grid[row][col],minValue[row][col])
            
        if col < len(grid[0]) and col > 0:           #列边界
            if minValue[row][col] == -1:
                minValue[row][col] = minValue[row][col-1]+grid[row][col]
            else:
                minValue[row][col] = min(minValue[row][col-1]+grid[row][col],minValue[row][col])
