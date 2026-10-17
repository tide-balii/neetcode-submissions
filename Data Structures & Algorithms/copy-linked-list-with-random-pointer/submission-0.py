"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head : 
            return None
        
        hashMap = {}
        newHead = Node(head.val)
        hashMap[head] = newHead

        while head : 
            if head not in hashMap : 
                cloneHead = Node(head.val)
                hashMap[head] = cloneHead
            
            if head.next : 
                if head.next not in hashMap : 
                    hashMap[head.next] = Node(head.next.val)
                hashMap[head].next = hashMap[head.next]
            
            else : 
                hashMap[head].next = None

            if head.random : 
                if head.random not in hashMap : 
                    hashMap[head.random] = Node(head.random.val)
                hashMap[head].random = hashMap[head.random]  
            else : 
                hashMap[head].random = None
            
            head = head.next

        return newHead




