# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None :
            return list2
        if list2 == None :
            return list1 
        
        l1, l2, nl = list1, list2, None

        if (l1.val <= l2.val) :
            nl = l1 
            l1 = l1.next
        
        else :
            nl = l2 
            l2 = l2.next

        res = nl 
        
        while l1 and l2 :
            if l1.val <= l2.val :
                nl.next = l1
                nl = l1 
                l1 = l1.next

            else :
                nl.next = l2
                nl = l2
                l2 = l2.next
        

        nl.next = l1 or l2 
        
        return res
