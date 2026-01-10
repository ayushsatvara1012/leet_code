class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# -------------------------------------------------------------------------
# CREATED A LIST
# -------------------------------------------------------------------------

def createList(arr):
    head = LinkedList(arr[0])
    curr = head

    for val in arr[1:]:
        curr.next = LinkedList(val)
        curr = curr.next
    return head


# -------------------------------------------------------------------------
# PRINT A LIST
# -------------------------------------------------------------------------


def printList(head):
    curr = head
    while curr is not None:
        print(curr.val, end='->')
        curr = curr.next
    print('None')


# -------------------------------------------------------------------------
# Get the Length of the Linked list
# -------------------------------------------------------------------------

def getLength(head):
    curr = head
    count = 0
    while curr is not None:
        count += 1
        curr = curr.next
    return count


# -------------------------------------------------------------------------
# Find the Max Value
# -------------------------------------------------------------------------

def findMax(head):
    if head is None:
        return None
    curr = head.next
    max_val = head.val

    while curr is not None:
        if curr.val > max_val:
            max_val = curr.val
        curr = curr.next
    return max_val


# -------------------------------------------------------------------------
# Search for a Value, #target = 8
# -------------------------------------------------------------------------

def searchTarget(head, target):
    curr = head
    while curr is not None:
        if curr.val == target:
            return True
        curr = curr.next
    return False


# -------------------------------------------------------------------------
# Insert at Beginning
# -------------------------------------------------------------------------

def insertBeginning(head, val):
    new_node = LinkedList(val)
    new_node.next = head
    return new_node


# -------------------------------------------------------------------------
# Insert at End
# -------------------------------------------------------------------------

def insertEnd(head, val):
    new_node = LinkedList(val)
    if head is None:
        return new_node
    curr = head
    while curr.next is not None:
        curr = curr.next

    curr.next = new_node

    return head


# -------------------------------------------------------------------------
# Delete a Node val = 4
# -------------------------------------------------------------------------

def delNode(head, val):
    if head is None:
        return None
    if head.val == val:
        return head.next

    prev = head
    curr = head.next

    while curr is not None:
        if curr.val == val:
            prev.next = curr.next
            return head

        prev = curr
        curr = curr.next
    return head

# -------------------------------------------------------------------------
# Reverse a Linked List
# -------------------------------------------------------------------------

def reverselist(pointer):
    prev = None
    curr = pointer

    while curr is not None:
        next_node = curr.next

        curr.next = prev

        prev = curr
        curr = next_node
    return prev

# -------------------------------------------------------------------------
# Find the Middle Node
# -------------------------------------------------------------------------

def middleNode(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow.val

# -------------------------------------------------------------------------
# Remove Duplicate
# -------------------------------------------------------------------------

def removeDups(head):
    if head is None:
        return None
    seen = set()

    prev = head
    seen.add(prev.val)
    curr = head.next

    while curr is not None:
        if curr.val in seen:
            prev.next = curr.next
            curr = curr.next
        else:
            seen.add(curr.val)
            prev = curr
            curr = curr.next
    return head

# -------------------------------------------------------------------------
# Detect list cycle
# -------------------------------------------------------------------------

def detectCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
# -------------------------------------------------------------------------
# 10. Detect if List Has a Cycle
# Input: 1 -> 2 -> 3 -> 4 -> 2 (cycle back to 2)
# Output: True
# -------------------------------------------------------------------------


head = createList([1, 20,1,5, 3, 4, 5])
print('Current List',end=':')
printList(head)

print(f'Linked List Length: {getLength(head)}')
print(f'Linked List Max Value: {findMax(head)}')
print(f'Linked List Target Value: {searchTarget(head, 2)}')

print('New value beginning',end=':')
head = insertBeginning(head, 99)
printList(head)

print('New Value at end',end=':')
head = insertEnd(head, 88)
printList(head)

print('Delete Node',end=':')
delNode(head,20)
printList(head)

print('Reverse List',end=':')
head = reverselist(head)
printList(head)

print('Middle Node',end=':')
m_node = middleNode(head)
print(m_node)

new_head = createList([1,1,2,4,3,3,4])
print('Remove Duplicates',end=':')
removeDups(new_head)
printList(new_head)

print('Detect Cycle:',end='')
print(detectCycle(head))



