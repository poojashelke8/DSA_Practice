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

def add_1_recursive(head):
    def helper(temp):
        if temp == None:
            return 1
        carry = helper(temp.next)
        temp.val += carry
        # temp.val = total%10
        # return total // 10

        if temp.val < 10:
            return 0
        temp.val = 0
        return 1
    carry = helper(head)
    if carry:
        newNode = ListNode(carry)
        newNode.next = head
        head = newNode
    return head


def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":
    arr = [2, 9, 9, 9,6]
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    print("Original Linked List:")
    printList(head)

    head = add_1_recursive(head)
    # addOne(head)

    print("After Adding One:")
    printList(head)
