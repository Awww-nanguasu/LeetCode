# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = head # pre节点用于串联新链表
        flag = pre
        while head and head.next:
            # 如果后一个节点 与 当前节点不同， 连上
            if head.next.val != pre.val:  
                pre.next = head.next
                pre = pre.next
            head = head.next
        # 结尾
        if pre:
            pre.next = None
        return flag

