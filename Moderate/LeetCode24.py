# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = head
        flag = 0
        while(1):
            if pre is None:
                break

            cur = pre.next
            if cur is None:
                break

            nex = cur.next
            
            pre.next = cur.next
            cur.next = pre

            if flag == 0:
                head = cur
                flag = 1
                
            pre = pre.next
        
        return head`