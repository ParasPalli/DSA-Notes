
class node:
    
    def __init__(this, value):
        this.value = value
        this.next = None
        this.prev = None


class LinkedList:
    
    def __init__(this, value):

        this.head = node(value)
        this.tail = this.head
        this.length = 1

    def print_list(this):

        currentNode = this.head

        while(currentNode != None):
            print(currentNode.value)
            currentNode = currentNode.next
			
    def append_ls(this, value):

        newNode = node(value)
        newNode.prev = this.tail
        this.tail.next = newNode
        this.tail = newNode
        this.length += 1

    def prepend_ls(this, value):

        newNode = node(value)
        
        this.head.prev = newNode
        newNode.next = this.head
        this.head = newNode
        this.length += 1

    def insert_ls(this, index, value):

        newNode = node(value)

        if index < this.length:

            currentNode = this.head

            # 0-1-2-3...
            # if we want to insert at 2 we want 1 node info...
            
            # As we want the node that is previous to the index
            for x in range(0, index):

                currentNode = currentNode.next

            # We are storing the nextNode info.. Means the info of remaining list....
            nextNode = currentNode.next

            currentNode.next = newNode
            newNode.prev = currentNode
            
            newNode.next = nextNode
            nextNode.prev = currentNode

            this.length += 1

        else:

            this.append_ls(value)
            

    def remove_ls(this, index):

        if index < this.length:

            currentNode = this.head

            for x in range(0, index):
                currentNode = currentNode.next

            unwantedNode = currentNode.next
            currentNode.next = unwantedNode.next
            unwantedNode.next.prev = currentNode

            this.length -= 1
                            

# Executing...
z = LinkedList(1)
z.append_ls(2)
z.append_ls(3)
z.prepend_ls(0)
z.insert_ls(1, 5)
z.print_list()
z.remove_ls(1)
print()
z.print_list()
