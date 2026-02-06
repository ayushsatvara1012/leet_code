# To convert the Linked list to list apply the given method to_LL() and to_List()

class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

def reverseLL(head):
    prev = None
    curr = head

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev