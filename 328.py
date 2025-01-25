# Odd Even Linked List
# Soln: 0ms runtime, beats 100.00%, 15.84MB memory, beats 25.87%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        if not head.next:
            return head

        even = head
        even_head = even
        odd = head.next
        odd_head = odd
        p = None

        while (even and even.next) and (odd and odd.next):
            even.next = even.next.next
            odd.next = odd.next.next
            odd = odd.next
            even = even.next
        even.next = odd_head
        return even_head