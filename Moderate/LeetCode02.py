# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list_l1 = [l1.val]
        list_l2 = [l2.val]

        while l1.next or l2.next:
            if l1.next:
                l1 = l1.next
                list_l1.append(l1.val)

            if l2.next:
                l2 = l2.next
                list_l2.append(l2.val)

        list_l1 = list_l1[::-1]
        list_l2 = list_l2[::-1]

        if len(list_l1)>len(list_l2):
            a = list_l1
            b = list_l2
            min_len = len(list_l2)
        else:
            b = list_l1
            a = list_l2
            min_len = len(list_l1)

        # print("a", list_l1)
        # print("b", list_l2)

        val = 0
        # print("=============")
        for i in range(-1, -min_len-1, -1):
            # if i == -1:
            #     print("=============")
            #     print(a[i], b[i])
            #     a[i] = a[i] + b[i]
            #     val = a[i] // 10
            #     print(val)
            #     a[i] = a[i]%10
            #     print(a[i])
            #     print("=============")
            #     continue

            # print(f'a[i]={a[i]}')
            # print(f'b[i]={b[i]}')
            # print(f'val={val}')
            a[i] = a[i] + b[i] + val
            # print(f"sum = {a[i]}")
            val = a[i] // 10
            # print(f'new_val={val}')
            
            a[i] = a[i] % 10
            # print(f"newa = {a[i]}")
            # print("=============")

        idx = -min_len-1
        while val!=0 and idx>-len(a)-1:
            a[idx] = a[idx] +  val
            val = a[idx] // 10
            a[idx] = a[idx] % 10
            idx -= 1

        head = ListNode()
        new = head
        # print(a)
        
        for x in a[::-1]:
            new.next = ListNode(x)
            new = new.next

        if idx == -len(a)-1 and val!=0:
            new.next = ListNode(1)


        return head.next