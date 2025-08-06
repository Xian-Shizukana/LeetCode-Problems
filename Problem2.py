def addTwoNumbers(l1: Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
    sum_arr = []
    carry = 0
    sum_list = ListNode()
    current = sum_list
    
    while l1 or l2:
        # If both still has value, add them both
        if l1 and l2:
            sum = l1.val + l2.val + carry
            carry = max(0, carry - 1)
            if sum > 9:
                carry += 1
            sum_arr.append(sum % 10)
            l1 = l1.next
            l2 = l2.next
            continue

        if l1:
            sum = l1.val + carry
            carry = max(0, carry - 1)
            if sum > 9:
                carry += 1
            sum_arr.append(sum % 10)
            l1 = l1.next
            continue

        if l2:
            sum = l2.val + carry
            carry = max(0, carry - 1)
            if sum > 9:
                carry += 1
            sum_arr.append(sum % 10)
            l2 = l2.next
            continue

    for num in sum_arr:
        current.next = ListNode(num)
        current = current.next

    return sum_list.next





