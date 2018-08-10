"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：
    所有数字（包括 target）都是正整数。
    解集不能包含重复的组合。 

示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]

示例 2:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
__author__ = 'Qiufeng'

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        i = 0                       #循环变量
        items = []                  #items是记录元素累加的元组
        combination = []            #返回的items的集合
        temp = target               #将target值赋给temp
        notes = []                  #notes是记录上一层的元素的序号
        while i <len(candidates):
            cnt = []                        #中间变量cnt
            if temp == candidates[i]:      #当值等于目标元素时
                if temp == target:
                #当中间值等于目标值时，直接将元素加到items中，并且再加到combination中
                    cnt.append(temp)
                    combination.append(cnt)
                    if i == len(candidates)-1:
                        #如果遍历完candidates,则直接返回combination
                        break
                        
                    #否则循环变量加一
                    i+=1
                else:
                    #先将items中元素从小到大排序
                    #如果combination中无现有的items,则将items加到combination
                    items.append(temp)
                    #将temp的值赋值给cnt,再将cnt进行排序，然后将cnt加到combination中
                    for j in items:
                        cnt.append(j)
                    cnt.sort()
                    if combination.count(cnt) ==0:
                        combination.append(cnt)
                    #返回上一层
                    del items[len(items)-1]
                    while i == len(candidates)-1:
                        #进行判断，是否上一层也是为最尾端的元素，不是则循环变量加一，是则继续返回上一层
                        #如果遍历了notes中没有元素，且i ==len(candidates)，则直接返回combination
                        if len(notes)==0:
                            break
                            
                        i = notes[len(notes)-1] #继续返回上一层
                        temp = temp + candidates[notes[len(notes) - 1]]
                        del notes[len(notes)-1]
                        del items[len(items)-1]
                    i+=1
            elif temp > candidates[i]:
                temp = temp - candidates[i]
                items.append(candidates[i])
                notes.append(i)
                i = 0
            elif temp < candidates[i]:
                while i == len(candidates) - 1:
                # 进行判断，是否上一层也是为最尾端的元素，不是则循环变量加一，是则继续返回上一层
                # 如果遍历了notes中没有元素，且i ==len(candidates)，则直接返回combination
                    if len(notes) == 0:
                        return combination
                    i = notes[len(notes) - 1]  # 继续返回上一层
                    temp = temp + candidates[notes[len(notes) - 1]]
                    del notes[len(notes) - 1]
                    del items[len(items) - 1]
                i+=1
                
        return combination                     #返回二维list
    
