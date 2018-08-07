"""

给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:
    1.可以认为区间的终点总是大于它的起点。
    2.区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

示例 1:
输入: [ [1,2], [2,3], [3,4], [1,3] ]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。

示例 2:
输入: [ [1,2], [1,2], [1,2] ]
输出: 2
解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。

示例 3:
输入: [ [1,2], [2,3] ]
输出: 0
解释: 你不需要移除任何区间，因为它们已经是无重叠的了。

"""
__author__ = 'Qiufeng'

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        本题要点，以区间为节点，每个节点end的越早，则有更大的区间可以供选择。
        符合条件的控件也就越多，需要删除的空间也就越少
        
        first.end < second.start
        second.end <other.end
        """
        first = Interval(0,0)
        second = Interval(0,0)
        inter = []
        initCount = len(intervals)
        
        if initCount == 0 or initCount==1:
            return 0

        #寻找第一个节点,第一个节点对于起始位置没有限制
        first = intervals[0]
        
        temp = 0               #记录需要删除的第一个节点的位置信息
        
        for i in range(1,len(intervals),1):
            if  first.end> intervals[i].end:
                first = intervals[i]
                temp = i
 
        del intervals[temp]
        

        #接下来利用贪心算法进行寻找下一个节点
        j = 0
        count  = 1
        while j<len(intervals) :                        #增加节点
            for i in range(0,len(intervals),1):         #寻找符合first.end <= intervals[i].start的元素
                if first.end <= intervals[i].start:
                    inter.append(intervals[i])
            
            if len(inter) == 0:
                return initCount-count
            
            if len(inter) == 1:
                return initCount-count-1
            
            second = inter[0]
            temp = 0
            for i in range(1,len(inter),1):
                if second.end > inter[i].end:
                    second = inter[i]
                    temp = i
            first = inter[temp] 
            del inter[temp]
            intervals = inter               #排除的不符合的区间以及已经计算的区间
            #return intervals
            second = []
            inter = []
            count+=1

