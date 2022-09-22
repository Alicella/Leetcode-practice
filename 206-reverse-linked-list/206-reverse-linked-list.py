# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # iteratively, two pointers
        prev = None
        cur = head
        
        while cur != None:
            # store the linked list part after the cur pointer
            nxt = cur.next
            
            # change cur to point to the prev linked list
            cur.next = prev
            
            # move the two pointers
            prev = cur
            cur = nxt
            
        return prev
        
        
        
        
        
        
        
        
        
        
#         if not head or not head.next:
#             return head
        
#         else:
#             tmp = head.val
#             head.val = head.next.val
#             head.next.val = tmp
#             return head
            