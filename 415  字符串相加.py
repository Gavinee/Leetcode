"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

    num1 和 num2 的长度都小于 5100.
    num1 和 num2 都只包含数字 0-9.
    num1 和 num2 都不包含任何前导零。
    你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
"""
__author__ = 'Qiufeng'

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        tt1 = []
        tt2 = []
        tt3 = []
        
        length = 0
        temp = ""
        
        for i in num1:
            tt1.append(int(i))
        tt1.reverse()
    
        for i in num2:
            tt2.append(int(i))
        tt2.reverse()
        
        max1 = max(len(tt1),len(tt2))
        length = max(len(tt1),len(tt2)) - min(len(tt1),len(tt2))
        
        for i in range(0,max1+1,1):
            tt3.append(0)
        
        if len(tt1)<len(tt2):
            for i in range(0,length,1):
                tt1.append(0)
        else:
            for i in range(0,length,1):
                tt2.append(0)
        
        for i in range(0,max1,1):
            
            if tt3[i] + tt1[i] + tt2[i]>=10:
                tt3[i+1] = 1
            tt3[i] = (tt3[i]+tt2[i]+tt1[i])%10

        tt3.reverse()
      
        if tt3[0] == 0:
            del tt3[0]
            
        for i in range(0,len(tt3),1):
            temp= temp+ str(tt3[i])
        
        return temp
