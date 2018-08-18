"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""
__author__ = 'Qiufeng'

#                               超时程序（递归形式）
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [0]             #有count[0]种方案
        step = 0                #记录已经走完的步数
        self.dynamicProgramming(count,n,step)
        return count[0]
    
    def dynamicProgramming(self,count,n,step):
        
        if step == n:
            count[0] +=1
            return 
            
        if step<n:
            step+=1
            self.dynamicProgramming(count,n,step)
            step-=1
            if step<=n-2:
                step+=2
                self.dynamicProgramming(count,n,step)
                step-=2

                
#                               通过的程序
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = []
        for i in range(0,n+1,1):
            dp.append(0)

        dp[1] = 1
        if n ==1:
            return dp[1]
        
        dp[2] = 2
        if n==2:
            return dp[2]
        
        for i in range(3,n+1,1):
            dp[i] = dp[i-1]+dp[i-2]
            
        return dp[n]
                
