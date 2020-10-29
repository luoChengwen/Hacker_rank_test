https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = ListNode(0)
        lst = head
        c = 0
        
        while True:
            if l1 is None and l2 is None:
                if c != 0:
                    lst.next = ListNode(1)
                    c = 0
                    lst = lst.next
                break
            elif l1 is None:
                while l2 is not None:
                    tmp_v = l2.val + c 
                    lst.next = ListNode(tmp_v % 10)
                    c = tmp_v//10
                    l2 = l2.next
                    lst = lst.next
                if c != 0:
                    lst.next = ListNode(1)
                break
            elif l2 is None:
                while l1 is not None:
                    tmp_v = l1.val + c 
                    lst.next = ListNode(tmp_v % 10)
                    c = tmp_v//10
                    l1 = l1.next
                    lst = lst.next
                if c != 0:
                    lst.next = ListNode(1)
                break
            else:
                tmp_v = l1.val + c + l2.val 
                lst.next = ListNode(tmp_v % 10)
                c = tmp_v//10
                l1 = l1.next
                l2 = l2.next
                lst = lst.next
        return head.next
