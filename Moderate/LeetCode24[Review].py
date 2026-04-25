# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pos1 = head
        if pos1 != None:
            head = pos1.next
            preNode = head
        while(pos1 != None and pos1.next != None):
            tempNode = pos1.next
            pos1.next = tempNode.next
            tempNode.next = pos1
            if preNode != head:
                preNode.next = tempNode
            preNode = pos1
            pos1 = pos1.next
        return head
