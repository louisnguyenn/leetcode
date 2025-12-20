# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # GIVEN 
        # two non-empty linked lists 
        # representing two non-negative integers 
        # stored in reverse order
        
        # REQUIRED
        # add the two numbers
        # return sum as a linked list

        # ANALYSIS
        # 1. walk through both of the linked lists 
        # 2. add each node one by one
        # 3. first node -> ones column, second node -> tens column (remember to carry)
        # 4. create linked list as we are walking through both of the linked lists

        # SOLUTION
        head = None
        last = None
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            if l1:
                x = l1.val
            else:
                x = 0
            if l2:
                y = l2.val
            else:
                y = 0
            sum = x + y + carry
            digit = sum % 10
            carry = sum // 10  # save carry for next iteration
            # print(sum)
            node = ListNode(digit)  # create node with digit 
            if head is None:
                head = node
                last = node
            else:
                last.next = node
                last = node
            # move both linked lists forward
            if l1 is not None:
                l1 = l1.next
            else:
                l1 = None
            if l2 is not None:
                l2 = l2.next
            else:
                l2 = None
        return head