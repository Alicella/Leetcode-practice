# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # initialize number of nodes = 1
        # initialize mid pointer position = 1
        # initialize mid and cur pointers point to head
        node_num = 1
        mid_pos = 1
        mid = head
        cur = head
        
        while cur.next != None:
            cur = cur.next
            node_num += 1       
            
            while mid_pos <= node_num / 2:
                mid = mid.next
                mid_pos += 1
        
        return mid