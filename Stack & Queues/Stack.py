
# Last in First Out.....
# You can also use array as the Stack...
# But Linked List are more best for this Job... (Because it's Dynamic)

# Treat Top Node as the Head Node...
# Each time you push you are creating new Head...

class Node:

    def __init__(this, value):
        this.value = value
        this.next = None


class Stack:

    def __init__(this):

        this.top = None
        this.length = 0

    def peek(this):

        if this.length == 0:
            return None
        
        print(this.top.value)


    def push(this, value):

        # Adding to the Top....
        newNode = Node(value)

        if this.length == 0:

            this.top = newNode
            
        else:
            previous_node = this.top
            this.top = newNode
            this.top.next = previous_node

        this.length += 1

        print(this.top.value)
        

    def pop(this):

        if this.length == 0:

            return None


        this.top = this.top.next
        this.length -= 1


        
s = Stack()
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.peek()
s.pop()
s.peek()

print()

# Just to Understand Whats going on....
# Top is creating different ladder of list..
# And Buttom is creating different ladder of list...
# Unlike Queue where it is referencing the same Node Ladder...

# n = Node(10)
# p = s.buttom
# s.buttom.next = n
# s.buttom = n

# print(p.value)
# print(s.buttom.value)
# print(p.next.value)

