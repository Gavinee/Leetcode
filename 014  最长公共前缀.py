"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
"""
__author__ = 'Qiufeng'

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 1
        j = 0
        k = 0
        if strs == None:
            return ""
        while(i<len(strs) and j<len(strs[i]) and j<len(strs[i-1])and strs[i][j]!=None and strs[i-1][j]!=None):
            while (j<len(strs[i]) and j<len(strs[i-1]))and strs[i][j] == strs[i-1][j] :
                j = j + 1
            if j > 0:
                strs[i] = strs[i][0:j]
            else:
                return ""
            i = i + 1
            j = 0
        if i == len(strs):
            return strs[i-1]
        else:
            return ""




