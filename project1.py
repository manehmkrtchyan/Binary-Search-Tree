class Node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None 
    

    def insert(self, node):
        if not isinstance(node, Node):
            node = Node(node)
        if self.root == None:
            self.root = node
        else: 
            self._insert(node, self.root)
    def _insert(self, current, node):
        if node.value["value"] < current.value["value"]:
            if current.left_child == None: 
                current.left_child = node
            else:
                self._insert(current.left, node)
        if node.value["value"] > current.value["value"]: 
            if current.right_child == None:
                current.right_child = node
            else:
                self._insert(current.right, node)
        else:
            print("Value already in tree")


    def preorder(self):
        """Root, Left, Right"""
        self._preorder(self.root)
    def _preorder(self, current):
        if current != None:
            print(current.value)
            self._preorder(current.left_child)
            self._preorder(current.right_child)         

    
    def inoreder(self):
        """Left, Root, Right"""
        self._inorder(self.root)
    def _inoreder(self, current):
        if current != None:
            self._inoreder(current.left_child)
            print(current.value)
            self._inoreder(current.right_child)


    def postorder(self):
        """Left, Root, Right"""
        self._postorder(self.root)
    def _inorder(self, current):
        if current != None:
            self._inorder(current.left_child)
            self._inorder(current.right_child)
            print(current.value)


    def find(self, value):
        return self._find(self.root, value)
    def _find(self, current, value):
        if current != None:
            if current.value["value"] == value:
                return current.value
            elif value < current.value[value]:
                return self._find(current.left_child, value)
            elif value > current.value[value]:
                return self._find(current.right_child, value)
        return "Value not found in the tree"


    def erase(self, value):
        self._erase(self.root, value, None, None)
    def _erase(self, current, value, previous, is_left):
        if current:
            if current.value["value"] == value:
                if current.left_child is None and current.right_child is None: #The node is a leaf node
                    if previous:
                        if is_left:
                            previous.left_child = None
                        else:
                            previous.right_child = None 
                    else:
                        self.root = None
                elif current.left_child is None: #The left child is None
                    if previous:
                        if is_left:
                            previous.left_child = current.right_child
                        else:
                            previous.right_child = current.right_child
                    else:
                        previous.root = current.right_child
                elif current.right_child == None: #The right child is None
                    if previous:
                        if is_left:
                            previous.left_child == current.left_child
                        else:
                            previous.right_child = current.left_child
                    else: 
                        self.root = current.left_child
                else: #Neither the left nor the right child is None
                    min_right = self.get_min_right(current.right_child)
                    current_value = min_right.value
                    self._delete(current.right_child, min_right.value["salary"], current, False)

            elif value < current.value["value"]:
                return self._erase(current.left_child, value, current, True)
            elif value > current.value["value"]:
                return self._erase(current.right_child, value, current, False) 
    def get_min_right(self, current):
        if current.left_child is None:
            return current
        else:
            self.get_min_right(current.left_child)