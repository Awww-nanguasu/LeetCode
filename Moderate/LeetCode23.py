# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sen = ListNode()
        head = sen
        flag = 0
        while(1):
            for x in lists:
                if x == [None]:
                    lists.remove(x)
            
            K = len(lists)
            if K == 0:
                break
            print(lists)
            node_list = [lists[j].val for j in range(K)]
            min_val = min(node_list)
            min_idx = node_list.index(min_val)
            sen.next = lists[min_idx]
            sen = sen.next
            lists[min_idx] = lists[min_idx].next
        return head.next