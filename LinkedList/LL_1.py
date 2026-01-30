# Creating LinkedList

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traversal_ll(head):
    temp = head
    while temp:
        print(temp.data,"-->",end=" ")
        temp = temp.next
    print('None')

def countEle(head):
    temp = head
    cnt = 0
    while temp:
        cnt+=1
        temp = temp.next
    return cnt 

def deleteHead(head):
    if head:
        return head.next
    return None

def deleteTail(head):
    if head == None or head.next == None:
        return None
    temp = head
    while temp.next.next != None:
        temp = temp.next
    temp.next = None
    return head

def delete_Kth_ele(head,k):
    if head == None:
        return head
    
    if k == 1:
        return head.next
    cnt = 0
    temp = head
    prev = None
    while temp:
        cnt+=1
        if cnt == k:
            prev.next = prev.next.next
            break
        prev = temp
        temp = temp.next
    return head

def insert_start(head,val):
    newNode = Node(val)
    newNode.next = head
    return newNode
 
def insert_tail(head,val):
    newNode = Node(val)
    if head is None:
        return newNode
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = newNode
    return head

def insert_kth_ele(head,val,k):
    newNode = Node(val)
    if head == None:
        return None
    if k == 1:
        newNode.next = head
        return newNode
    cnt = 1
    temp = head
    prev = None
    while temp:
        if k == cnt:
            prev.next = newNode
            newNode.next = temp
        prev = temp
        temp = temp.next
        cnt+=1 
    return head

# Driver code
if __name__ == "__main__":
    arr = [2, 5, 8, 7]
    head = Node(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = Node(val)
        curr = curr.next

    print("Original Linked List:")
    traversal_ll(head)

    
    # head = deleteHead(head)   # assign the new head

    # print("After deleting head:")
    # traversal_ll(head)

    # head = deleteTail(head)   

    # print("After deleting Tail:")
    # traversal_ll(head)

    
    # head = delete_Kth_ele(head,2)
    traversal_ll(head)
    count = countEle(head)
    head = insert_start(head,100)
    print("insert -->",head)
    traversal_ll(head)
    head2 = insert_tail(head,200)
    insert_tail(head,500)
    insert_kth_ele(head,250,2)
    traversal_ll(head2)
    print("Count -->", count)
