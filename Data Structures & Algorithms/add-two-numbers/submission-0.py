# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = "", ""
        A, B = l1, l2

        while A:
            num1 = str(A.val) + num1
            A = A.next

        while B:
            num2 = str(B.val) + num2
            B = B.next
        
        sumn = str(int(num1) + int(num2))[::-1]
        l3 = cur = ListNode(int(sumn[0]))
        for i in range(len(sumn)):
            if i+1<len(sumn):
                cur.next = ListNode(int(sumn[i+1]))
            cur = cur.next
        return l3

        


