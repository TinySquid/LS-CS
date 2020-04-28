"""
Given pointers to the head nodes of 2 linked lists that merge together at some point, 
find the Node where the two lists merge. It is guaranteed that the two head Nodes will be different, and neither will be NULL.

In the diagram below, the two lists converge at Node x:

[List #1] a--->b--->c
                     \
                      x--->y--->z--->NULL
                     /
     [List #2] p--->q

Complete the int findMergeNode(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2) 
method so that it finds and returns the data value of the Node where the two lists merge. 
"""

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    """
    1--->2
        \
        3--->Null
        /
        1

    Traverse both lists at the same time
    put nodes in dict to mark as seen
    if dict key already exists, that's the merge point
    return node .data value
    """
    visited = {}

    # Node pointers
    c_node1 = head1
    c_node2 = head2

    # Status booleans
    l1_is_done = False
    l2_is_done = False

    # Lose DRYness but gain speed by traversing two lists of unequal length
    # in one loop
    while not l1_is_done or not l2_is_done:

        # Check list 1
        if not l1_is_done:
            # Check if node is already visited
            # if it is then we know it comes from the other list
            # meaning they merged at this point
            if visited.get(c_node1):
                return visited.get(c_node1)
            else:
                # Add node to visited
                visited[c_node1] = c_node1.data
            # Continue traversing list 1 by moving pointer
            c_node1 = c_node1.next

            # End of list 1 reached, mark complete
            if c_node1 is None:
                l1_is_done = True

        # Check list 2, code is same as above
        if not l2_is_done:
            # Continue traversing list 2
            if visited.get(c_node2):
                return visited.get(c_node2)
            else:
                visited[c_node2] = c_node2.data

            c_node2 = c_node2.next

            # End of list 2 reached, mark complete
            if c_node2 is None:
                l2_is_done = True
