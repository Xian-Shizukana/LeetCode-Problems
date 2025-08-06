def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    count = 0
    # For counting
    itr = head
    # For removing
    itr2 = head

    # Counting the amount of nodes in the list
    while itr:
        count += 1
        itr = itr.next

    to_remove = count - n

    # If the head is removed, return the list without the head,
    if to_remove == 0:
        return head.next

    count = 0

    # If the list only contains one value, return None as
    # the constraints say n cannot be 0.
    if head.next == None:
        return head.next

    # If the node to be removed is next, skip over it, essentially
    # removing it.
    while itr2:
        if count == to_remove - 1:
            itr2.next = itr2.next.next
            break
        count += 1
        itr2 = itr2.next

    return head


