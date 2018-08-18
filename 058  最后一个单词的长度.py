"""
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:
输入: "Hello World"
输出: 5
"""
__author__ = 'Qiufeng'

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        i = len(s)-1
        if len(s) == 0:                 #如果字符串为空串，return 0
            return 0
        if s.count(" ") == 0:           #如果字符串中无空格，直接返回字符串长度
            return len(s)
        
        while i<len(s):                 #如果字符串小于s的长度
            if i == len(s)-1 and s[i] == " ":       #当s的尾部为空格，则删除空格
                s = s[0:-1]                         #删除空格
                if s == "":                         #如果删除后字符串为空串，则返回空字符串的长度
                    return len(s)                   
                i = i-1                             
                continue                            #跳出当前循环
            if s[i] == " ":                         #如果第i个值为空格
                return len(s)-1-i                   #则用最后的元素下标减去第i个元素的下标则为最后一个字符串的长度
            if i == 0 and s[i]!=" ":                #如果循环一直执行到下标为0的时候，则直接返回该字符串的长度
                return len(s)
            i=i-1
            
