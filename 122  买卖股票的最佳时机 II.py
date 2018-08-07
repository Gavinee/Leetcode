"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

示例 2:
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

示例 3:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""
__author__ = 'Qiufeng'

#########################################################################
#方法一：此方法效率不高，方法二大大提高了效率
算法：分多种情况讨论：
      1.价格一直升，则从prices[0]购买，prices[-1]抛出，利润为prices[-1]-prices[0]
      2.价格一直降，则不买，利润为0
      3.价格有波动，这种情况寻找波峰（购买点价格low）和波谷（抛出点high），波峰和波谷总是成对出现的。
        所以，sum(high-low)
 缺点：这个价格需要逐个遍历，使时间复杂度增高
########################################################################

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        high = []         #价格最高
        low = []          #价格最低
        bargain = 0      #利润
        temp1 = prices
        i = 0
        
        #删除连续的相等元素
        j = 1
        k = 0
        while j<len(temp1) :
            if temp1[j] == temp1[j-1]:
                k = k + 1
                del temp1[j]
            else:
                j = j + 1
        
        temp = temp1
        while i+1<len(temp) and temp[i] > temp[i+1]:        #若股市一直下跌
            if i + 1 == len(temp) - 1:
                return 0
            i = i + 1
        
        i = 0
        while i+1<len(temp) and temp[i] < temp[i+1]:        #若股市一直上涨
            if i + 1 == len(temp) - 1:
                return temp[len(temp)-1] - temp[0]
            i = i + 1
            

        for tt in range(2,len(temp),1):                             #若开始为low
            #if temp[tt-2] == temp[tt-1] or temp[tt-1] == temp[tt]:
            #    continue
            
            if  tt-2 == 0 and temp[tt-2] < temp[tt-1]:
                low.append(temp[tt-2])
            
            if temp[tt-1] < temp[tt-2] and temp[tt-1] < temp[tt]:   #购买
                low.append(temp[tt-1])
                
            if temp[tt-1] > temp[tt-2] and temp[tt-1] > temp[tt]:   #抛出
                high.append(temp[tt-1])
 
            if tt == len(temp)-1 and temp[tt-1] < temp[tt]:         #若结束时为high
                high.append(temp[tt])

        low_tt = 0
        high_tt = 0
        for q in range(0,len(low),1):
            low_tt = low_tt + low[q]
            
        for q in range(0,len(high),1):
            high_tt = high_tt +high[q]
            
            #cnt =high[q] - low[q]
            #bargain = bargain + cnt
        bargain = high_tt - low_tt
        return bargain


"""
#################################################################
方法二：
算法：贪心算法
使每个上升序列为问题的子问题。只用记录上升区间，并记录每个上升区间的最小值和最大值，
可以得到最优子结构：bargain = bargain + temp[i] - cnt 
其中：temp[i]是子区间的最大值
     cnt为子区间的最小值
     bargain为已经计算了的子区间累加的利润之和
#################################################################

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        
        temp = prices
        bargain = 0  # 利润
        i = 0
        cnt = 0
        flag = True
        while i<len(temp)-1 :
            if  temp[i]>temp[i+1]:
                i = i + 1
                continue
            while  i<len(temp)-1  and temp[i]<=temp[i+1] :
                if flag == True:
                    cnt = temp[i]            #价格最低
                    flag = False
                i = i + 1
            bargain = bargain + temp[i] - cnt       #每一次买到抛售为一个循环
            flag = True

        return bargain

"""











