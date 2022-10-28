# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # intuition: r - l = n - 1, when r reach the end, l is the nth node to remove
        
        pre = l = r = head
        for i in range(n - 1):
            r = r.next
         
        # now the distance btw l pointer and r pointer is n - 1
        # move pre, l, r pointer until r is at the end
        while r.next:
            pre = l
            l = l.next
            r = r.next
        
        if l == head:    # need to remove the head node
            head = l.next
        elif l == r:       # need to remove the last node, so pre points to none
            pre.next = None                 
        else:                 # remove the middle node that l points to
            pre.next = l.next    
             
        return head