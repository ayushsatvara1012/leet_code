class LinkedList:
    def __init__(self, val=0, next=None):
       self.next = next
       self.val = val

def createLinkedList(arr):
    head = LinkedList(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = LinkedList(val)
        curr = curr.next
    return head

def printLL(head):
    curr = head
    while curr is not None:
        print(curr.val,end='->')
        curr = curr.next
    print('None')


def mergelist(head1,head2):
    dummy = LinkedList(0)
    curr = dummy

    while head1 and head2:
        if head1.val <= head2.val:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next

    if head1 is not None:
        curr.next = head1
    if head2 is not None:
        curr.next = head2

    return dummy.next

list1 = createLinkedList([1,3,5])
list2 = createLinkedList([2,4,6])
merge = mergelist(list1,list2)
printLL(merge)
