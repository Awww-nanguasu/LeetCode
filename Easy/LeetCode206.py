# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head):

        if head == None:
            dummy = ListNode()
            return dummy, dummy
        
        dummy, tmp = self.reverse(head.next)
        tmp.next = head
        return dummy, head

    def reverseList(self, head):
        dummy, _ = self.reverse(head)
        return dummy

def readList(list):
    while(list.next):
        list = list.next
        print(list.val)

dummy = ListNode()
cur = dummy
for i in range(1, 6):
    cur.next = ListNode(i)
    cur = cur.next

readList(dummy)

b = Solution()
c = b.reverseList(dummy.next)
readList(c)