# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # intuition: r - l = n, when r reach the end node, l + 1 is the nth node to remove
        
        l = r = head
        for i in range(n):
            r = r.next
        
        # if r points to null of linked list end, need to remove the first node
        if not r:
            return head.next
        
        # now the distance btw l pointer and r pointer is n - 1
        # keep moving l, r pointer until r is at the end
        while r.next:
            l = l.next
            r = r.next
        # remove the l + 1 node
        l.next = l.next.next    
             
        return head