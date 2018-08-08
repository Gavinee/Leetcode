"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
  '2':'abc'
  '3':'def'
  '4':'ghi'
  '5':'jkl'
  '6':'mno'
  '7':'pqrs'
  '8':'tuv'
  '9':'wxyz'

"""
__author__ = 'Qiufeng'


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        i = 0
        strr = ""
        list1 = []
        if digits =="":
            return []
        
        self.Combination(i,digits,strr,list1)
        
        return list1

    def Combination(self,i,digits,strr,list1):
        if i==len(digits):
            list1.append(strr)
            return

        str1 = ""
        temp = []
        if digits[i]=='2':
            str1 = 'abc'
        elif digits[i]=='3': 
            str1 = 'def'
        elif digits[i]=='4': 
            str1 = 'ghi'
        elif digits[i]=='5': 
            str1 = 'jkl'
        elif digits[i]=='6': 
            str1 = 'mno'
        elif digits[i]=='7': 
            str1 = 'pqrs'
        elif digits[i]=='8': 
            str1 = 'tuv'
        elif digits[i]=='9': 
            str1 = 'wxyz'


        for j in range(0,len(str1),1):
            tt = strr
            tt+=str1[j]
            self.Combination(i+1,digits,tt,list1)
