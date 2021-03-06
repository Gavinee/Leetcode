"""
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能
会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而
不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"
的一个子序列，而"aec"不是）。

示例 1:
s = "abc", t = "ahbgdc"
返回 true.

示例 2:
s = "axc", t = "ahbgdc"
返回 false.

后续挑战 :
如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，
你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

"""
__author__ = 'Qiufeng'

class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sposition = 0
        if len(s) == 0:
            return True
        if len(s)>len(t):
            return False
        strlen = len(t)
        for tposition in range(0,strlen,1):
            if t[tposition] == s[sposition]:
                if sposition == len(s)-1:
                    return True
                sposition+=1
            tposition+=1
        return False
