

def main(head):
    inicio = head
    arr = []
    while head != None:
        arr.append(head.val)
        head = head.next
    head = inicio
    while arr != []:
        head.val = arr.pop()
        head = head.next
    return inicio



head = []

print(main(head))