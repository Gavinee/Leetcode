"""
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""
__author__ = 'Qiufeng'


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp1 = l1
        temp2 = l2
        cnt = ListNode(0)
        sum = 0
        tt = 0
        csq = cnt
        
        while(temp1 != None and temp2 != None):
            num = (temp1.val + temp2.val + tt)%10
            tt = int((temp1.val + temp2.val +tt)/10)
                
            cnt.next = ListNode(num)
            cnt = cnt.next
            temp1 = temp1.next
            temp2 = temp2.next
            
        if temp1 == None :
            temp1 = temp2
        
        while temp1 != None:
                num = (temp1.val+ tt)%10
                tt = int((temp1.val+ tt)/10)
                cnt.next = ListNode(num)
                cnt = cnt.next
                temp1 = temp1.next

        if tt != 0:
            cnt.next = ListNode(tt)
            cnt = cnt.next

        return  csq.next           
