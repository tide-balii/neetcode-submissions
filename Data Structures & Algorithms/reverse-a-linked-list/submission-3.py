# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        if head.next == None :
            return head

        prev, curr, neg = head, head.next, None 

        if curr.next == None :
            prev.next = None
            curr.next = prev
            return curr
        
        while curr != None : #Deal with edgecase of when curr.next == None 
            if neg == None :
                prev.next = None 
                neg = prev
                prev = curr 
                curr = curr.next
                continue

            prev.next = neg 
            neg = prev 
            prev = curr 

            if curr.next == None :
                curr.next = neg
                return curr

            curr = curr.next

           
            

            


            


          





        