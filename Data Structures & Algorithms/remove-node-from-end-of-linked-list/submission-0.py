# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0 
        curr = head

        while curr : 
            length += 1 
            curr = curr.next 

        if length - n == 0 : 
            return head.next 

        newLen = length - n 
        counter = 1
        nodeBefore = head
        while counter < newLen:
            counter += 1 
            nodeBefore = nodeBefore.next

        nodeBefore.next = nodeBefore.next.next

        return head  

