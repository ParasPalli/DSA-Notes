
# Binary Search Tree...

class Node:

    def __init__(this, value):
        this.value = value
        this.left = None
        this.right = None


class BST:

    def __init__(this):
        this.root = None

    def insert(this, value):

        newNode = Node(value)

        if this.root == None:

            this.root = newNode

        else:

            currentNode = this.root

            while True:

                if value < currentNode.value:

                    if currentNode.left == None:
                        currentNode.left = newNode
                        return 0

                    currentNode = currentNode.left

                else:

                    if currentNode.right == None:
                        currentNode.right = newNode
                        return 0

                    currentNode = currentNode.right

        

    def lookup(this, value):

        if this.root == None:
            return None

        currentNode = this.root

        while currentNode != None:

            if currentNode.value > value:

                currentNode = currentNode.left

            elif currentNode.value < value:

                currentNode = currentNode.right

            elif currentNode.value == value:

                return currentNode

        return False
    
    def remove(this, value):

        if this.root == None:
            return False
        
        currentNode = this.root
        parentNode = None

        while(currentNode != None):

            # Iterate to Left
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left

            # Iterate to Right
            elif value > currentNode.value:

                parentNode = currentNode
                currentNode = currentNode.right 

            # We have a match
            elif value == currentNode.value:
                
                # 1) CurrentNode: Has Left Child No Right Child:
                if currentNode.right == None:

                    # If its root
                    if parentNode == None:
                        this.root = currentNode.left

                    else:

                        #Basically these conditions checking the CurrentNode Position...

                        # If parent > current value, make current left child a child of parent
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.left

                        # If parent < current value, make left child a right child of parent
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.left


                # 2) CurrentNode: Has Right Child no Left Child:
                elif currentNode.right.left == None:

                    currentNode.right.left = currentNode.left
                    
                    # If it's root...
                    if parentNode == None:
                        this.root = currentNode.right

                    else:
                    
                        # parent > current, make right child of CN to left of the paerent
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.right

                        # parent < current, make right child of CN to right of the paerent
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.right

                
                # 3) CurrentNode: RightChild that has Left Child:
                else:

                    # Find the Right Child's Left most child
                    leftmost = currentNode.right.left
                    leftmostParent = currentNode.right

                    while leftmost.left != None:
                        leftmostParent = leftmost
                        leftmost = leftmost.left

                    # Parent's left subtree is now leftmost's right subtree

                    leftmostParent.left = leftmost.right
                    leftmost.left = currentNode.left
                    leftmost.right = currentNode.right


                    if parentNode == None:
                        this.root = leftmost

                    else:

                        if currentNode.value < parentNode.value:
                            parentNode.left = leftmost

                        elif currentNode.value > parentNode.value:
                            parentNode.right = leftmost

                return True



b = BST()
b.insert(4)
b.insert(1)
b.insert(3)
b.insert(-2)
b.insert(-1)
b.insert(-5)
b.insert(-4)


# Breadth First Search / Traversal...

def BFS(root):
    if root is None:
        return
    
    queue = [root]

    while queue:

        node = queue.pop(0)
        print(node.value, end = " ")

        # enqueue left child
        if node.left != None:               # [1]
            queue.append(node.left)

        if node.right:                      # [2] => [1] & [2] Both are Similar Operations....
            queue.append(node.right)


BFS(b.root)


