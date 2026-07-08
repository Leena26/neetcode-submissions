# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        use fast and slow pointers
        fast moves at twice the speed
        when fast reaches the end of the linked list, slow is at the middle

        1. move fast and slow pointers
        2. reverse the second half and store in prev (new linked list)
        3. compare first half and scond half


        '''
        if head == None:
            return False

        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            next= slow.next
            slow.next = prev
            prev = slow
            slow = next
        
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        
        return True


        
        
        
        
        



        