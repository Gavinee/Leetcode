"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

    1.左括号必须用相同类型的右括号闭合。
    2.左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true
"""
__author__ = 'Qiufeng'

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tt = []
        ss = []
        for i in range(0,len(s),1):
            if s[i] == '(':
                tt.append(1)
                ss.append('(')
            elif s[i] == ')':
                tt.append(-1)
                ss.append(')')
            elif s[i] == '[':
                tt.append(2)
                ss.append('[')
            elif s[i] == ']':
                tt.append(-2)
                ss.append(']')
            elif s[i] == '{':
                tt.append(7)
                ss.append('{')
            elif s[i] == '}':
                tt.append(-7)
                ss.append('}')
        
        if len(tt) > 0:        
            if tt[0] < 0 or tt[len(tt)-1] > 0:           
                #最左边一个元素不能是为负值（')','],'}'）  同理 最右边的元素不能为正值  （'(','[','{')
                return False
        
        if len(tt)%2==1 or sum(tt) != 0:                         
            #如果长度为单数，则说明有未匹配的括号；如果求和后不为0，就说明没匹配好
            return False
        
        i = 0        
        while i<len(ss)-1:
            if ss[i] == '(':
                if ss[i+1] == ')': 
                    del ss[i]
                    del ss[i]
                    i -=1
                    continue
                elif ss[i+1] == '[' or ss[i+1] == '{' or ss[i+1] == '(':
                    i+=1
                    continue
                else:
                    return False

            elif ss[i] == '[':
                if ss[i+1] == ']':
                    del ss[i]
                    del ss[i]
                    i -=1
                    continue
                elif ss[i+1] == '(' or ss[i+1] == '{' or ss[i+1] == '[':
                    i+=1
                    continue
                else:
                    return False

            elif ss[i] == '{':
                if ss[i+1] == '}':
                    del ss[i]
                    del ss[i]
                    i -=1 
                    continue
                elif ss[i+1] == '(' or ss[i+1] == '{' or ss[i+1] == '[':
                #if s[i+1] == '(' or s[i+1] == '[' or s[i+1] == '}':  
                    i+=1
                    continue
                else:
                    return False
                    
            else:
                i+=1
                continue
                
        return True 
