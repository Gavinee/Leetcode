"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
__author__ = 'Qiufeng'

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        Parenthesis = ['(',')']
        stringList = []                     #最后输出的结果
        str1 = ""                           #过程字符串
        
        answer = addParenthesis(n-1,Parenthesis)        #调用函数，得到生成的list
        
        stringOne = getnewList(answer)                 
        #将多维list转换为一维list,参考别人的代码 
        #https://blog.csdn.net/zouyang2014/article/details/77129157
        
        j =1                               
        """
        j的作用是字符串生成个数，i%((2*n)*j-1) == 0 
        这个语句的作用是寻找到每个字符串的最后一个元素的下标
        """
        
        
        """
        以下代码是将每个单独的字符串（字符）拼接成每个项，每个项答案中每个list的每一项
        """
        for i in range(0,len(stringOne),1):     
            str1 += stringOne[i]
                                    
            if i!= 0 and i%((2*n)*j-1) == 0:
                if stringList.count(str1) == 0:     #count函数是返回str1值在stringList中的个数
                    stringList.append(str1)         #添加list项
                str1 = ""
                j+=1                                #记录字符串生成个数
            
        
        return stringList
        
def addParenthesis(n,Parenthesis):
    temp = []                                               
    tmp = []
    if n == 0:
        return Parenthesis
    
    for i in range(1,len(Parenthesis),1):
        if Parenthesis[i-1] =="(" and Parenthesis[i] == ")":
            Parenthesis.insert(i,"(")
            Parenthesis.insert(i+1,")")
            for tt in range(0,len(Parenthesis),1):
                tmp+=Parenthesis[tt]      
            #tmp = Parenthesis
            res = addParenthesis(n-1,tmp)
            if temp.count(res) == 0:
                temp.append(res)
            del Parenthesis[i]
            del Parenthesis[i]
            
            res = []
            tmp = []
            
            Parenthesis.insert(i+1,"(")
            Parenthesis.insert(i+2,")")
            for tt in range(0,len(Parenthesis),1):
                tmp+=Parenthesis[tt]    
            #tmp = Parenthesis
            res = addParenthesis(n-1,tmp)
            if temp.count(res) == 0:
                temp.append(res)
            del Parenthesis[i]
            del Parenthesis[i]
            
            res = []
            tmp = []
    return temp


def getnewList(newlist):
	d = []
	for element in newlist:
		if not isinstance(element,list):
			d.append(element)
		else:
			d.extend(getnewList(element))
	
	return d
