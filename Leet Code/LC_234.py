def palindromeLL(head):
    """ First we will go for the brute force """

    ## This is the optimised way
    # stack = []
    # while head:
    #     stack.append(head.val)
    #     head = head.next
    # return stack == stack[::-1]



    if not head or not head.next:
        return True

    ## Got the second half
    slow = fast = head
    while head:
        slow = slow.next
        fast = fast.next.next

    ## Reversing the second half
    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    ## Checking the values of second half and the full linked list
    left,right = head,prev
    while right:
        if right.val!=left.val:
            return False
        left = left.next
        right = right.next
    return True
