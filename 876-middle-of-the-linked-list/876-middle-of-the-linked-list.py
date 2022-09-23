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
#         node_num = 1
#         mid_pos = 1
#         mid = cur = head
        
#         while cur.next != None:
#             cur = cur.next
#             node_num += 1       
#             # below is how to move the mid pointer
#             while mid_pos <= node_num / 2:
#                 mid = mid.next
#                 mid_pos += 1
        
#         return mid
        
        # simplified solution 
        # https://leetcode.com/problems/middle-of-the-linked-list/discuss/154619/C%2B%2BJavaPython-Slow-and-Fast-Pointers
        
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow
        
        
        
        
    
        