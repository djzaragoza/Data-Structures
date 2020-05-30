

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
        else:
            if target < self.value:
                if self.left is not None:
                    return self.left.contains(target)
                else:
                    return False
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        while self.right is not None:
            self = self.right
            
        return self.value
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        
        if self.left:
            self.left.for_each(fn)
            
        if self.right:
            self.right.for_each(fn)
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left is not None:
            self.left.in_order_print(self.left)
            
        print (node.value)
        
        if self.right is not None:
            self.right.in_order_print(self.right)
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = []
        queue.append(node)
        
        while(len(queue) > 0):
            node = queue.pop(0)
            print(node.value)
            
        if node.left is not None:
            queue.append(node.left)
            
        if node.right is not None:
            queue.append(node.right)
        pass
    
    # make a queue
    # enqueue the node
    # as long as the queue is not empty
    ## dequeue from the front of the queue, this is our current node
    ## enqueue the kids of the current node on the queue 

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        
        stack.append(node)
        while len(stack) != 0:
            node = stack.pop()
            print(node.value)
            if node.left is not None:
                stack.append(node.left) 
            if node.right is not None:
                stack.append(node.right)
        
        pass
    
    # make a stack
    # push the node on the stack
    # as long as the stack is not empty
    ## pop off the stack, this is our current node
    ## put the kids on the current node on the stack 
    ## (check that they are not None, then put them on the stack)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
        # pass

    # Print Post-order recursive DFT
    # def post_order_dft(self, node):
        # pass
