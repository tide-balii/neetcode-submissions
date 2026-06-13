# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        curr = head 
        dummy = curr 

        if not head : 
            return head

        while curr != None : 
            dummy = curr 
            curr = curr.next
            dummy.next = prev 
            prev = dummy
        return prev 

