

# First in First Out...
# Arrays are not optimal for this Queues...

# Creating Simple LinkedList...
# while dequeue (pop) change the head...

class Node:

    def __init__(this, value):

        this.value = value
        this.next = None


class Queue:

    def __init__(this): 

        this.first = None
        this.last = None
        this.length = 0

    def peek(this):

        if this.length == 0:
            return None

        print(this.first.value)
        

    def enqueue(this, value):

        # Adding to the Buttom....
        newNode = Node(value)

        if this.length == 0:
            this.first = newNode
            this.last = newNode

        else:

            this.last.next = newNode
            this.last = newNode

        this.length += 1


    def dequeue(this):

        if this.length == 0:
            return None
        
        this.first = this.first.next
        this.length -= 1


q = Queue()
q.peek()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

q.peek()

q.dequeue()
q.dequeue()

q.peek()

print()

# q.iter()

# # As the First and Last both are accessing the same Node...
# # And Appending the values to the same ladder...
# # Unlike the stack where it is creating the new ladder...
# # For top and buttom....

# p_n = q.first

# n = Node(6)
# q.first.next = n
# q.first = n

# print(p_n.value)
# print(p_n.next.value)
# print(q.first.value)

# By understanding and performing the above methods we
# somehow lost reference so, we can't iterate...
# means it's showing only 3, 6 which is prev value..
# and our modified value....









