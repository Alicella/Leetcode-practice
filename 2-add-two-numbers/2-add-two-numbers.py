# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lsum = ListNode()
        def f(l1, l2, lsum):
            if not l1 and not l2:
                return 
            elif not l1:
                return f(ListNode(), l2, lsum)    
            elif not l2:
                return f(l1, ListNode(), lsum) 
                
            lsum.val += (l1.val + l2.val) % 10

            if l1.next or l2.next or l1.val + l2.val >= 10:
                lsum.next = ListNode((l1.val + l2.val) // 10)
            
            if lsum.val >= 10:
                lsum.val -= 10
                lsum.next = ListNode((l1.val + l2.val) // 10 + 1)
                
            return f(l1.next, l2.next, lsum.next)
        
        f(l1, l2, lsum)
        return lsum