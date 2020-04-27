# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Build 2 integers from provided lists
            - They are in reverse
        list 1:
            make a string
            append each node value to string
            reverse string
        list 2:
            same process
            
        helper func to do the above process
        
        add both lists with helper func, convert to string again and reverse
        
        build linked list with result values
        return it
        """

        # Helper function to return string of node values cast to int
        def make_num(ll):
            # Setup
            str_num = ""
            current_node = ll

            while current_node is not None:
                # Build str_num until end of list is reached
                str_num += str(current_node.val)
                # Move pointer to next node
                current_node = current_node.next

            # return int
            return int(str_num[::-1])

        # Add both linkedlists, convert back to string
        result_str = str(make_num(l1) + make_num(l2))[::-1]

        # Build linked list out of the result string
        result_ll = ListNode(result_str[0])
        # Set pointer to head
        current_node = result_ll
        for i in range(1, len(result_str)):
            # Add new node with value at i
            current_node.next = ListNode(result_str[i])
            current_node = current_node.next

        return result_ll
