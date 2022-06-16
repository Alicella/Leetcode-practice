# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         lsum = ListNode()
#         def f(l1, l2, lsum):
#             if not l1 and not l2:
#                 return 
#             elif not l1:
#                 return f(ListNode(), l2, lsum)    
#             elif not l2:
#                 return f(l1, ListNode(), lsum) 
            
#             ttl = l1.val + l2.val
#             lsum.val += ttl % 10

#             if l1.next or l2.next or ttl >= 10:
#                 lsum.next = ListNode(ttl // 10)
            
#             if lsum.val >= 10:
#                 lsum.val -= 10
#                 lsum.next = ListNode(ttl // 10 + 1)
                
#             return f(l1.next, l2.next, lsum.next)
        
#         f(l1, l2, lsum)
#         return lsum
        
# https://leetcode.com/problems/add-two-numbers/discuss/1032/Python-concise-solution.

        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
        return dummy.next
    