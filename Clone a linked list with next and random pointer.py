#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None
'''

def copyList(head):
    '''
    param: head:  head of linkedList to copy
    return: the head of the copied linked list the #output will be 1 if successfully copied
    '''
    cur = head
    next = head.next
    while cur:
        cur.next = Node(cur.data)
        cur.next.next = next
        cur = next
        next = cur.next if cur else None
    
    cur = head
    while cur:
        cur.next.arb = cur.arb.next if cur.arb else None
        cur = cur.next.next

    cur = head
    next = head.next
    res = head.next
    while cur:
        cur.next = cur.next.next
        next.next = next.next.next if next.next else None
        cur = cur.next if cur.next else None
        next = next.next if next.next else None

    return res
