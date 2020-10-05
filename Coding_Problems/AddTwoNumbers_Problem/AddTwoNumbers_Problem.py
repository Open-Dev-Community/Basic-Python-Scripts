# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def printList(nodeStart):
    print(nodeStart.val)
    if nodeStart.next is None:
        return False
    else:
        return printList(nodeStart.next)


class Solution(object):
    def addTwoNumbers(self, l1, l2):

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        sval = l1.val + l2.val
        if sval < 10:
            ansnode = ListNode(sval)
            ansnode.next = self.addTwoNumbers(l1.next, l2.next)
            return ansnode
        else:
            rval = l1.val + l2.val - 10
            ansnode = ListNode(rval)
            ansnode.next = self.addTwoNumbers(ListNode(1), self.addTwoNumbers(l1.next, l2.next))
            return ansnode
