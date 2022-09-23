# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:     
        # iteratively, two(actually three) pointers
#         prev = None
#         cur = head
        
#         while cur != None:
#             # store the linked list part after the cur pointer
#             nxt = cur.next       
            
#             # change cur to point to the prev linked list
#             cur.next = prev           
            
#             # move the two pointers
#             prev = cur
#             cur = nxt
            
#         return prev
        
        # recursively
        
        if not head or not head.next:
            return head
        
        # leading downwards to the end of the linke list
        reversed_head = self.reverseList(head.next)
        
        # reverse the second last node's direction
        head.next.next = head;
        head.next = None
        
        return reversed_head
    
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            