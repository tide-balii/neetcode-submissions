# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2 :
            return None
        
        if not list1 and list2 : 
            return list2
        
        if not list2 and list1 : 
            return list1
        

        pointer1 = list1 
        pointer2 = list2 
        res = ListNode()
        resPointer = res

        while pointer1 or pointer2 :
            if not pointer1 and pointer2 : 
                resPointer.next = pointer2
                break
            
            elif not pointer2 and pointer1 : 
                resPointer.next= pointer1 
                break
            
            else : 
                if pointer1.val <= pointer2.val : 
                    resPointer.next = pointer1
                    pointer1 = pointer1.next
                else :
                    resPointer.next = pointer2 
                    pointer2 = pointer2.next

            resPointer = resPointer.next
        
        return res.next 



            

