class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def mergeTwoSortedList(list1,list2):
    dummy = ListNode(0)
    curr = dummy

    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    if list1 is not None:
        curr.next = list1
    if list2 is not None:
        curr.next = list2

    return dummy.next

# -------------------------------------------------------------------------
# To print the Linked List
# -------------------------------------------------------------------------
def to_LL(iterable):
    dummy = ListNode(0)
    curr = dummy
    for val in iterable:
        curr.next = ListNode(val)
        curr = curr.next

    return dummy.next

def to_List(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    print( result)

l1 = to_LL([1,2,4])
l2 = to_LL([1,3,4])
merged = mergeTwoSortedList(l1,l2)
to_List(merged)

