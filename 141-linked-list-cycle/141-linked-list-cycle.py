# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # a neater version:
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
        
        
        
        
        
#         if not head or not head.next:
#             return False
        
#         # use slow and fast pointers
#         slow = head
#         fast = head.next
        
#         while slow != fast:
#             # fast or fast.next is null means you've reached to 
#             # a tail without cycle
#             if fast == None or fast.next == None:
#                 return False
#             slow = slow.next
#             fast = fast.next.next
        
#         return True
        