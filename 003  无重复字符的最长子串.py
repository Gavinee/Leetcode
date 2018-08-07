"""
给定一个字符串，找出不含有重复字符的最长子串的长度。

示例：
给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。

给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。

给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。
"""
__author__ = 'Qiufeng'

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1 = {}
        prt1 = 0        #指针1  首地址
        prt2 = 1        #指针2  尾地址
        slist = []
        ptr = []
        
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        for i in range(0,len(s),1):
            slist.append(s[i])
        
        i = 0
        flag = True
        while i<len(slist):
            temp = slist[prt1:prt2] 
            if temp.count(slist[prt2])==0:
                prt2+=1
                if flag == True:
                    dict1[prt1] = prt2-prt1
                    ptr.append(dict1[prt1])
            else:
                dict1[prt1] = prt2-prt1
                ptr.append(dict1[prt1])
                prt1 = prt1 + temp.index(slist[prt2])+1
                temp = []
                flag = False
            i=prt2
            if i == len(slist)-1:
                flag =True
                
        Max = 0
        for key in dict1:
            if Max < dict1[key]:
                Max = dict1[key]
                
        return Max
