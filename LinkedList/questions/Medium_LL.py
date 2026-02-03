# Add 1

class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None


def reverse(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def addOne(head):
    head = reverse(head)

    curr = head
    carry = 1  # we are adding ONE

    while curr and carry:
        total = curr.val + carry
        curr.val = total % 10
        carry = total // 10

        if curr.next is None and carry:
            curr.next = ListNode(carry)
            carry = 0
        curr = curr.next

    return reverse(head)


def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":
    arr = [2, 5, 8, 7]
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    print("Original Linked List:")
    printList(head)

    head = addOne(head)

    print("After Adding One:")
    printList(head)
