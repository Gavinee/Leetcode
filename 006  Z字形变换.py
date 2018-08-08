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

"""
方法一：
    找z子形与横行读取之间的映射关系，通过list存储之间的映射关系
    此方法可行，但在拼接成字符串时，无法删除已经使用的元素，造成
    程序在运行时可能会超时。
"""

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

"""
方法二：
    通过对方法一的优化，利用dict来储存二者之间的映射关系。
    并在遍历dict时，可以删除已经使用的元素，使程序效率大大
    增加，方法一运行时间是1740ms，而方法而运行时间缩短到
    1170ms.
    
    Python -- 遍历字典时删除元素技巧
    
    d = {'a':1, 'b':0, 'c':1, 'd':0}
    keys = list(d.keys())
    for key in keys:
        del(d[key])
"""

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        tt = ""
        #Col = []
        dict1 = {}
        if len(s)<=numRows:
            return s
        
        if numRows <2:
            return s
        
        for i in range(0,len(s),1):
            position = numRows - 1
            row = i//position#列
            temp = i%(2*position)
            col = position - abs(temp-position)  #行
            dict1[i] = col
            #Col.append(col)   
            position = 0

            
        k = 0
        for j in range(0,numRows,1):
            
            keys = list(dict1.keys())
            for key in keys:
                if dict1[key] == k:
                    tt+=s[key]
                    del(dict1[key])
            k+=1
            j+=1
        return tt
    
