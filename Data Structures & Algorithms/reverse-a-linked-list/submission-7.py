# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None :
            return None
            
        elif head.next == None :
            return head

        prev, curr, future = None, head, head.next 

        while future != None :
            curr.next = prev 
            prev = curr 
            curr = future
            future = future.next

        curr.next = prev
        return curr  