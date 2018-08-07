"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""
__author__ = 'Qiufeng'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp1 = l1
        temp2 = l2
        temp = ListNode(0)
        csq = temp
        
        while temp1 != None and temp2 != None:
            if temp1.val > temp2.val:
                temp.next = temp2
                temp2 = temp2.next
                
                
            else:
                temp.next = temp1
                temp1 = temp1.next
               
            temp = temp.next
        if temp1 == None:
            temp.next = temp2
        elif temp2 == None:
            temp.next = temp1
    
        return csq.next
