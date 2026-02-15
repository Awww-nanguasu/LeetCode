# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: 
    def reverse(self, head, right, cur=1):
        if head == None or cur == right + 1:
            dummy = ListNode()
            self.dummy = dummy
            if head == None:
                self.next = None
            else:
                self.next = head
            return None

        tmp = self.reverse(head.next, right, cur+1)
        if tmp == None:
            self.dummy.next = head
        else:
            tmp.next = head
    
        return head

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head
        i = 1
        pre = head
        if left == right:
            return head

        while(i<left):
            if cur.next == None:
                return head
            pre = cur    
            cur = cur.next
            i = i+1

        cur = self.reverse(cur, right, i)        
        pre.next = self.dummy.next
        cur.next = self.next
        return head