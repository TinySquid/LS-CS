# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # Recursive solution

    # base cases
    # l1 None: return l2
    # l2 None: return l1

    def merge(l1, l2):
        if l1 == None:
            return l2
        elif l2 == None:
            return l1

        if l1.val <= l2.val:
            # Dive l1
            l1.next = merge(l1.next, l2)
            # l1 value is less or equal, so it will be the next node
            return l1
        else:
            # Dive l2
            l2.next = merge(l1, l2.next)
            # l2 is the bigger number so it gets pushed to the right
            return l2

    return merge(l1, l2)


###### DRIVER CODE ######
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

lr = mergeTwoLists(l1, l2)

cur = lr

merged = []

while cur is not None:
    merged.append(cur.val)
    cur = cur.next

print(merged)
