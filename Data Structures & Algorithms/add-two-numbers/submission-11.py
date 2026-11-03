# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Pointer = l1 
        l2Pointer = l2 
        newHead = ListNode()
        newHeadPointer = newHead

        while l1Pointer and l2Pointer : 
            newValue = l1Pointer.val + l2Pointer.val + newHeadPointer.val
            if newValue > 9 : 
                newValue = newValue - 10
                newNode = ListNode(1)
            else : 
                newNode = ListNode()
            
            newHeadPointer.val = newValue
            l1Pointer = l1Pointer.next
            l2Pointer = l2Pointer.next

            if l1Pointer or l2Pointer or newNode.val == 1 :
                newHeadPointer.next = newNode
                newHeadPointer.next = newNode
                newHeadPointer = newHeadPointer.next
            else : 
                break


            while (not l1Pointer and l2Pointer) or (not l2Pointer and l1Pointer) : 
                newValue = 0 
                if not l1Pointer : 
                    newValue = l2Pointer.val + newHeadPointer.val 
                    newNode = ListNode()
                    if newValue > 9 : 
                        newValue = newValue - 10 
                        newNode = ListNode(1)

                    newHeadPointer.val = newValue
                    l2Pointer = l2Pointer.next

                    if l2Pointer or newNode.val == 1 : 
                        newHeadPointer.next = newNode
                        newHeadPointer = newHeadPointer.next 
                    

                elif not l2Pointer : 
                    newValue = l1Pointer.val + newHeadPointer.val 
                    newNode = ListNode()
                    if newValue > 9 : 
                        newValue = newValue - 10 
                        newNode = ListNode(1)
                    
                    newHeadPointer.val = newValue
                    l1Pointer = l1Pointer.next
                    
                    if l1Pointer or newNode.val == 1 : 
                        newHeadPointer.next = newNode
                        newHeadPointer = newHeadPointer.next 
                    
 
        return newHead
                    