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
        while r.next:
            pre = l
            l = l.next
            r = r.next
        
        if l == head:    # if l still points to head, then pre also points to head
            head = pre.next
        elif l != r:     
            pre.next = l.next    # remove the node that l points to
            
        # elif pre == r:     # only one element in the linked list, remove the single node
        #     head = None
        else:
            pre.next = None  # l == r, need to remove the last node, so pre points to none
            
        return head