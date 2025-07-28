# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        node_k=head
        for _ in range(k-1):
            node_k=node_k.next
        node_k_from_end=head
        current=node_k
        while current.next:
            current = current.next
            node_k_from_end=node_k_from_end.next

        node_k.val,node_k_from_end.val=node_k_from_end.val,node_k.val

        return head


        