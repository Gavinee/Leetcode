"""
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。

示例1:
输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]

注意:
你可以重复使用键盘上同一字符。
你可以假设输入的字符串将只包含字母。
"""
__author__ = 'Qiufeng'

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        dict1 = {}
        tt1 = "QWERTYUIOPqwertyuiop"
        tt2 = "ASDFGHJKLasdfghjkl"
        tt3 = "ZXCVBNMzxcvbnm"
        list1 = [tt1,tt2,tt3]
        i = 0
        j = 0
        x = 0
        while i<len(list1):
            while j<len(list1[i]):
                dict1[list1[i][j]] = x
                j += 1
            x += 1
            j = 0
            i += 1
        
        i = 0
        j = 1
        temp = []
        while i<len(words):
            if len(words[i]) ==1:
                temp.append(words[i])
                i += 1
                continue
            
            while j<len(words[i]):
                if j == len(words[i])-1 and dict1[words[i][j-1]] == dict1[words[i][j]]:
                    temp.append(words[i])
                    i += 1
                    j = 1
                    break
                if dict1[words[i][j-1]] != dict1[words[i][j]]:
                    i += 1
                    j = 1
                    break
                else:
                    j += 1
        return temp
