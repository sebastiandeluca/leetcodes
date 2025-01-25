# Delete the Middle Node of a Linked List
#Soln: 72ms runtime, beats 64.38%, 91.69MB memory, beats 37.10%
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return None
        s = head
        f = head
        p = None

        while f and f.next:
            p = s
            s = s.next
            f = f.next.next
        
        p.next = s.next
        return head
            


# Soln: 218ms Runtime, beats 5.06%, 94.04MB memory, beats 6.91% (1st attempt)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return None
        res = []
        node = head
        while node.next != None:
            res.append(node)
            node = node.next
        
        res.append(node)
        mid = len(res) // 2
        y = res.pop(mid)
        new_head = res[0]
        node = new_head
        for x in range(1,len(res)):
            node.next = res[x]
            node = node.next
        node.next = None
        return new_head
            