# Reverse a Linked List
#Soln: 3ms runtime, beats 16.68%, 14.41mb memory, beats 41.40% (attempt 2, recursion)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        reversed_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversed_head
        

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nodes = []
        n = head
        while n:
            nodes.append(n)
            n = n.next
        if not nodes or len(nodes) == 1:
            return head
        new_head = nodes[-1]
        n2 = new_head
        for x in range(len(nodes) - 2, -1, -1):
            n2.next = nodes[x]
            n2 = n2.next
        n2.next = None
        return new_head
        