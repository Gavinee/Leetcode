"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例1.
输入： "babad"
输出： "bab"
注意:  "aba"也是一个有效答案

示例2.
输入： "cbbd"
输出： "bb"
"""
__author__ = 'Qiufeng'

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if len(s) == 0:
            return ""
        elif len(s) ==1:
            return s
        elif len(s) ==2:
            if s[0] == s[1]:
                return s
            else :
                return s[-1]                    #s[-1]是数组最后一个元素
        else:            
            i = 1
            temp =0
            dict1 = {len(s)-1:1}
            aim = 0
            Max = len(s)-1                                  #键值中间变量
            str1 =""
            while i<len(s):
                while i-temp-1>=0 and i+temp<len(s) and s[i-temp-1] == s[i+temp]:   #baab型
                    aim = 2+2*temp
                    """
                    减枝 ，保留最优解，如果符合，则添加元素到哈希表中。
                    默认第一个相对最长的回文字符串添加到哈希表中，注意是相对较长的回文字符串
                    这个相对是相对前面已经遍历过得s的元素得到的回文字符串。
                    比之前的回文字符串长，则保留，否则，舍弃。
                    这就是动态规划的核心了。
                    """
                    if dict1[Max] < aim:                                      
                        dict1[i-temp-1] =2+2*temp                             #i+temp-i+temp+1+1  回文字符串的长度
                        Max = i-temp-1
                    temp+=1
                    
                temp = 1
                while i-temp >=0 and i+temp<len(s) and s[i-temp] == s[i+temp]:          #bab型
                    aim = 2*temp +1
                    if dict1[Max] < aim:
                        dict1[i-temp] = 2*temp +1                             #i+temp-i+temp+1    回文字符串的长度
                        Max = i-temp
                    temp+=1
                temp = 0
                i+=1

            for tt in range(0,dict1[Max],1):                                #将最长的回文字符串拼接起来
                str1+=s[Max+tt]
            
            return str1 #返回最长的回文字符串。
