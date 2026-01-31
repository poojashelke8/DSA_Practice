class Node:
    def __init__(self,data,next = None,back=None):
        self.data = data
        self.next = next
        self.back = back

def print_DLL(head):
    if head == None:
        return None
    temp = head
    while temp:
        print(temp.data,end=" <--> ")
        temp = temp.next
    print("None")

def delete_Head_DLL(head):
    if head == None:
        return None
    if head:
        head = head.next
        head.back = None
        return head
    return None
def delete_k_ele(head,k):
    if head == None:
        return None
    
    if k== 1:
        head = head.next
        head.back = None
        return head
    cnt = 1
    temp = head
    while temp:
        if cnt == k:
            prev_node = temp.back
            next_node = temp.next
            if prev_node:
                prev_node.next = next_node
            if next_node:
                next_node.back = prev_node
        cnt+=1
        temp = temp.next
    return head

def delete_Tail_DLL(head):
    if head == None or head.next == None:
        return None
    temp = head
    while temp.next.next != None:
        temp = temp.next
    temp.next = None
    return head

def insert_head(head,val):
    newNode = Node(val)
    if head == None:
        return newNode
    newNode.next = head
    head.back = newNode
    return newNode

def insert_tail(head,val):
    newNode = Node(val)
    if head == None:
        return newNode
    temp = head
    while temp.next.next!=None:
        temp = temp.next
    temp.next.next = newNode
    newNode.back = temp
    return head

def insert_k_ele(head,val,k):
    newNode= Node(val)
    if head == None:
        return None
    if k == 1:
        newNode.next = head
        head.back = newNode
        return newNode
    
    cnt = 1
    temp = head
    while temp:
        if k == cnt:
            prev = temp.back
                
            prev.next = newNode
            newNode.back = prev
            newNode.next = temp
            temp.back = newNode
           
        cnt+=1
        temp = temp.next

    if cnt == k:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = newNode
        newNode.back = temp

    return head
            
if __name__ == "__main__":
    arr = [2, 5, 8, 7]
    head = Node(arr[0])
    prev = head
    for val in arr[1:]:
        temp = Node(val,None,prev)
        prev.next = temp
        prev = temp
        
    print_DLL(head)
    head = delete_Head_DLL(head)
    print_DLL(head)
    head = delete_Tail_DLL(head)
    print_DLL(head)
    head = delete_k_ele(head,2)
    print_DLL(head)
    head = insert_head(head,100)
    print_DLL(head)
    head = insert_tail(head,500)
    head = insert_tail(head,650)
    head  =insert_k_ele(head,1000,4)
    head  =insert_k_ele(head,5,3)
    head  =insert_k_ele(head,10,5)

    print_DLL(head)

    
