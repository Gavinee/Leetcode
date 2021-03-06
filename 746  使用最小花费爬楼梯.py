"""
数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例 1:
输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。

示例 2:
输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。

注意：
    cost 的长度将会在 [2, 1000]。
    每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。
"""
__author__ = 'Qiufeng'

#                 超时程序（256 / 276 个通过测试用例）
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        minCost = [-1]
        step = -1
        temp = 0
        cost.append(0)
        self.dynamicProgramming(cost,step,minCost,temp)
        return minCost[0]
    
    def dynamicProgramming(self,cost,step,minCost,temp):
        if minCost[0] > 0 and temp >minCost[0] :
            return
        
        if step == len(cost)-1:
            if minCost[0] == -1:
                minCost[0] = temp
            minCost[0]=min(minCost[0],temp)
            return
        
        #if temp == 0 and step == 0:
         #   temp = cost[0]
        
        if step <= len(cost)-3:
            step+=2
            temp = temp + cost[step]
            self.dynamicProgramming(cost,step,minCost,temp)
            temp = temp - cost[step]
            step = step - 2
        
        if step <= len(cost)-2:
            step+=1
            temp = temp + cost[step]
            self.dynamicProgramming(cost,step,minCost,temp)
            temp = temp - cost[step]
            step = step - 1

            
#                       通过的程序       
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = {}
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(cost)):
            dp[i] = min(dp[i-2]+cost[i],dp[i-1]+cost[i])
        return min(dp[len(cost)-1],dp[len(cost)-2])
    
