# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        m = 0
        temp = head
        while temp:
            m += 1
            temp = temp.next
        
        if m%2 != 0:
            for _ in range(int(m/2)):
                head = head.next
        
        else:
            for _ in range(int(m/2)):
                head = head.next
        
        return head



        