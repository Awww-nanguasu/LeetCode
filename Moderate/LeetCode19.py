# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def iteration(self, node: Optional[ListNode], n: int) -> int:
        if node == None:
            return 0
        else:
            node_idx = self.iteration(node.next, n)
            if node_idx == n:
                node.next = node.next.next
            return 1 + node_idx

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sen = ListNode()
        sen.next = head
        self.iteration(sen, n)
        return sen.next