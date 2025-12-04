class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    # Constructor just assigns an empty root.
    def __init__(self):
        self.root = None

    # Search for a node containing a matching key. Returns the
    # Node object that has the matching key if found, None if
    # not found.
    def search(self, desired_key):
        current_node = self.root
        while current_node is not None:
            # Return the node if the key matches.
            if current_node.key == desired_key:
                return current_node
                
            # Navigate to the left if the search key is
            # less than the node's key.
            elif desired_key < current_node.key:
                current_node = current_node.left
                
            # Navigate to the right if the search key is
            # greater than the node's key.
            else:
                current_node = current_node.right
      
        # The key was not found in the tree.
        return None

    # Inserts the new node into the tree.
    def insert(self, node):

        # Check if the tree is empty
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node is not None: 
                if node.key < current_node.key:
                    # If there is no left child, add the new
                    # node here; otherwise repeat from the
                    # left child.
                    if current_node.left is None:
                        current_node.left = node
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    # If there is no right child, add the new
                    # node here; otherwise repeat from the
                    # right child.
                    if current_node.right is None:
                        current_node.right = node
                        current_node = None
                    else:
                        current_node = current_node.right       
   
    # Removes the node with the matching key from the tree.
    def remove(self, key):
        parent = None
        current_node = self.root
        
        # Search for the node.
        while current_node is not None:
        
            # Check if current_node has a matching key.
            if current_node.key == key: 
                if current_node.left is None and current_node.right is None:   # Case 1: node is a leaf
                    if parent is None: # Node is root
                        self.root = None
                    elif parent.left is current_node: 
                        parent.left = None
                    else:
                        parent.right = None
                    return  # Node found and removed
                elif current_node.left is not None and current_node.right is None:  # Case 2: node has one child
                    if parent is None: # Node is root
                        self.root = current_node.left
                    elif parent.left is current_node: 
                        parent.left = current_node.left
                    else:
                        parent.right = current_node.left
                    return  # Node found and removed
                elif current_node.left is None and current_node.right is not None:  # Case 2
                    if parent is None: # Node is root
                        self.root = current_node.right
                    elif parent.left is current_node:
                        parent.left = current_node.right
                    else:
                        parent.right = current_node.right
                    return  # Node found and removed
                else: # Case 3: node has two children
                    # Find successor (leftmost child of right subtree)
                    successor_parent = current_node # establish current node as parent of the successor
                    successor = current_node.right # move to right child
                    while successor.left is not None: # check for left child
                        successor_parent = successor # move parent pointer down
                        successor = successor.left # move to left child
                    current_node.key = successor.key # Copy successor to current node
                    current_node.value = successor.value # copy value as well
                    if successor_parent.left is successor: # Remove successor from right subtree
                        successor_parent.left = successor.right
                    else:
                        successor_parent.right = successor.right
                    return # node deleted
            parent = current_node # continue searching
            if current_node.key < key: # Search right
                current_node = current_node.right
            else: # Search left
                current_node = current_node.left
        return # Node not found
    
    def inorder_traversal(self, node, result = None): # returns in-order traversal, traverse the left subtree, then the root node, finally traverse the right subtree.
        if result is None:
            result = []
        if node is None:
            return result
        self.inorder_traversal(node.left, result)
        result.append((node.key, node.value)) # appending a tuple
        self.inorder_traversal(node.right, result)
        return result

    def preorder_traversal(self, node, result = None): # returns pre-order traversal, start at root, traverse left subtree, then traverse right subtree.
        if result is None:
            result = []
        if node is None:
            return result
        result.append((node.key, node.value))
        self.preorder_traversal(node.left, result)
        self.preorder_traversal(node.right, result)
        return result

    def postorder_traversal(self, node, result = None): # returns post-order traversal, traverse left subtree, traverse right subtree, then root.
        if result is None:
            result = []
        if node is None:
            return result
        self.postorder_traversal(node.left, result)
        self.postorder_traversal(node.right, result)
        result.append((node.key, node.value))
        return result