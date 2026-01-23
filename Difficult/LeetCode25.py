# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.start = None
        self.next = None

    def reverse(self, node, n, k):
        if node == None:
            return None

        if n == k:
            self.next = node.next
            self.start = node
        else:
            cur = self.reverse(node.next, n+1, k) 
            if cur == None:
                return None
            cur.next = node
            
        return node

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        iter_times = 0
        while(1):
            n = 0
            head = self.reverse(head, n+1, k)

            if head == None:
                break

            if iter_times==0 and self.start:
                dummy.next = self.start
        
            if iter_times!=0:
                tmp.next = self.start

            tmp = head
            head.next = self.next
            head = self.next
            iter_times = iter_times + 1
        return dummy.next