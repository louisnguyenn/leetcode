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
        pred = None
        curr = head
        if head == None:
            return head
        
        while curr != None:
            succ = curr.next # save the next node in successor
            curr.next = pred
            # move pointers forward
            pred = curr
            curr = succ
        head = pred # predecessor is the new head
        return head