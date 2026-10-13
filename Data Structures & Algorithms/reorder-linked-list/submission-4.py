# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        
        prev = None 
        curr = slow.next 
        slow.next = None

        while curr : 
            nextNode = curr.next
            curr.next = prev 
            prev = curr
            curr = nextNode


        firstHalf, secondHalf = head, prev

        while secondHalf : 
            FHTmp = firstHalf.next
            SHTmp = secondHalf.next 
            firstHalf.next = secondHalf
            secondHalf.next = FHTmp
            secondHalf = SHTmp 
            firstHalf = FHTmp  

        
