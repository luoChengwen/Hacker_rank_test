# https://leetcode.com/problems/merge-two-sorted-lists/


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        ls = head
        
        while True:
            if l1 is None and l2 is None:
                break
            elif l1 is None:
                ls.next = l2
                break
            elif l2 is None:
                ls.next = l1
                break
            else:
                if l1.val < l2.val:
                    sm = l1.val
                    l1 = l1.next
                else:
                    sm = l2.val
                    l2 = l2.next
                ls.next = ListNode(sm)
                ls = ls.next
        return head.next
