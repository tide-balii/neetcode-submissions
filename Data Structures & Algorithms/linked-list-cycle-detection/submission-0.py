# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        res = False
        Set = set()
        while curr :
            if curr.next == None :
                return False
            elif curr.next in Set : 
                res = True
                return res 
            Set.add(curr)
            curr = curr.next
             
