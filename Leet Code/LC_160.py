class LinkedList:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

def createLL(arr):
    head = LinkedList(arr[0])
    curr = head

    for val in arr[1:]:
        curr.next = LinkedList(val)
        curr = curr.next
    return head

def getLength(head):
    count =0
    curr = head
    while curr is not None:
        count += 1
        curr = curr.next
    return count

def intersectionLL(headA,headB):
    if not headA or not headB:
        return None

    pA = headA
    pB = headB

    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    return pA



headA = createLL([1,2,3,4])
headB = createLL([1,2,3])
print(intersectionLL(headA,headB))