# Maximum Sum of a Linked List
# Soln: 194ms runtime, beats 57.35%, 71.32MB memory, beats 66.97%1431

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        s, f = head, head
        value = 0

        while f and f.next:
            f = f.next.next
            s = s.next
        
        curr, prev = s, None

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        while prev:
            value = max(value, head.val + prev.val)
            prev = prev.next
            head = head.next
        return value