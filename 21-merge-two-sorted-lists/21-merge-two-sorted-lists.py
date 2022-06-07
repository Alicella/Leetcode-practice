# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sorted = ListNode()
        
        if not list1 and not list2:
            return sorted.next
        # elif not list1:
        #     return list2
        # elif not list2:
        #     return list1
        elif not list1 or not list2: 
            return list1 if list1 else list2
        else:
            if list1.val <= list2.val:
                sorted.val = list1.val
                sorted.next = self.mergeTwoLists(list1.next, list2)
                
            else:
                sorted.val = list2.val
                sorted.next = self.mergeTwoLists(list1, list2.next)
            
        return sorted