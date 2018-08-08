"""
将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：

P   A   H   N
A P L S I I G
Y   I   R

之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"

实现一个将字符串进行指定行数变换的函数:

string convert(string s, int numRows);

示例 1:
输入: s = "PAYPALISHIRING", numRows = 3
输出: "PAHNAPLSIIGYIR"

示例 2:
输入: s = "PAYPALISHIRING", numRows = 4
输出: "PINALSIGYAHRPI"
解释:
P     I    N
A   L S  I G
Y A   H R
P     I
"""
__author__ = 'Qiufeng'

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        tt = ""
        Col = []
        
        if len(s)<=numRows:
            return s
        
        if numRows <2:
            return s
        
        for i in range(0,len(s),1):
            position = numRows - 1
            row = i//position#列
            temp = i%(2*position)
            col = position - abs(temp-position)  #行
            Col.append(col)   
            position = 0
        
        k = 0
        for j in range(0,numRows,1):
            p = 0
            for p in range(0,len(Col),1):
                if Col[p] == k:
                    tt+=s[p]
                p+=1
            k+=1
            j+=1
        return tt
        
"""        
        j = 0
        k = 0
        while j < numRows:
            p = 0
            while p<len(Col):
                if Col[p] == k:
                    tt+=s[p]
                p+=1
                if p == len(Col):
                    k+=1
            j+=1
        return tt
"""                
