"""
给定一个 32 位有符号整数，将整数中的数字进行反转。

示例1：
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
"""
__author__ = 'Qiufeng'

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #将数据化为正整数
        if(x<0):         #判断输入数据是否大于0,如果小于0则取反
            y = -x
        else :
            y = x
        count = []       #创建一个列表
        i = 0
        while(y/10 or y%10):    
            count.append(y%10)     #将各个位的数保存为列表元素
            i=i+1
            y = y/10
        cnt = 0
        for j in range(0,i):       #将保存的数据倒置
            cnt = cnt + count[i-1-j]*pow(10,j)
        #将数据还原
        if (x < 0):                
            cnt = -cnt
        else:
            cnt = cnt
        #判断数据是否在范围内，不在返回值为0,在则返回倒置的数据
        if cnt > pow(2,31)-1 or cnt <- pow(2,31):
            return 0
        else:
            return cnt
