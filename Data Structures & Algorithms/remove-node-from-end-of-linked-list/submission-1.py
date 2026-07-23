# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f = head
        x = 0
        while f:
            x+=1
            f = f.next
            
        y = x-n
        if y==0:
            return head.next
        
        f = head
        for i in range(x-1):
            if (i+1) == y:
                f.next = f.next.next
                break
            f = f.next
        return head








        

