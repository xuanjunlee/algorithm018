# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 方法1：设置哨兵节点，比较节点值，指向值小的节点
        if not l1:
            return l2

        if not l2:
            return l1

        dummy = ListNode(0)
        node1, node2 = l1, l2
        pre = dummy

        while node1 and node2:
            if node1.val <= node2.val:
                pre.next = node1
                pre = node1
                node1 = node1.next
                continue

            pre.next = node2
            pre = node2
            node2 = node2.next

        pre.next = node1 if node1 else node2

        return dummy.next
