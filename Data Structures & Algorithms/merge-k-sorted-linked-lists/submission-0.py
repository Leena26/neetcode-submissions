# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        
        while len(lists) >1:
            tmp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                tmp.append(self.mergeLists(l1, l2))
            lists = tmp
        return lists[0]

    
    def mergeLists(self, list1, list2):
        new = ListNode()
        head = new

        while list1 and list2:
            if list1.val< list2.val:
                new.next = list1
                list1 = list1.next
            else:
                new.next = list2
                list2 = list2.next
            new = new.next
        
        if list1:
            new.next = list1
        if list2:
            new.next = list2
        
        return head.next