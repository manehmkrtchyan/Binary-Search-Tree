class Node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None 
    

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else: 
            self._insert(value, self.root)
    def _insert(self, value, current):
        if value < current.value:
            if current.left_child == None: 
                current.left_child = Node(value)
            else:
                self._insert(value, current.left_child)
        else: 
            if current.right_child == None:
                current.right_child = Node(value)
            else: 
                self._insert(value, current.right_child)
        

    def preorder(self):
        """Root, Left, Right"""
        self._preorder(self.root)
    def _preorder(self, current):
        if current != None:
            print(current.value)
            self._preorder(current.left_child)
            self._preorder(current.right_child)         

    
    def inorder(self):
        """Left, Root, Right"""
        self._inorder(self.root)
    def _inorder(self, current):
        if current != None:
            self._inorder(current.left_child)
            print(current.value)
            self._inorder(current.right_child)


    def postorder(self):
        """Left, Right, Root"""
        self._postorder(self.root)
    def _postorder(self, current):
        if current != None:
            self._inorder(current.left_child)
            self._inorder(current.right_child)
            print(current.value)


    # def find(self, value):
    #     return self._find(self.root, value)
    # def _find(self, current, value):
    #     if current != None:
    #         if current.value["value"] == value:
    #             return current.value
    #         elif value < current.value[value]:
    #             return self._find(current.left_child, value)
    #         elif value > current.value[value]:
    #             return self._find(current.right_child, value)
    #     return "Value not found in the tree"


    def erase(self, value):
        self._erase(self.root, value, None, None)
    def _erase(self, current, value, previous, is_left):
        if current:
            if current.value == value:
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
                    self._erase(current.right_child, current_value, current, False)

            elif value < current.value:
                return self._erase(current.left_child, value, current, True)
            elif value > current.value:
                return self._erase(current.right_child, value, current, False) 
    def get_min_right(self, current):
        if current.left_child is None:
            return current
        else:
            self.get_min_right(current.left_child)


    def get_height(self):
        if self.root != None:
            return self._get_height(self.root, 0)
        else:
            return 0
    def _get_height(self, current, current_height):
        if current == None:
            return current_height
        left_height = self._get_height(current.left_child, current_height + 1)
        right_height = self._get_height(current.right_child, current_height + 1)
        return max(left_height, right_height)


    def contains(self, value):
        if self.root != None:
            return self._contains(value, self.root)
        else:
            return False
    def _contains(self, value,current_node):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left_child != None:
            return self._contains(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child != None:
            return self._contains(value, current_node.right_child)
        return False   


    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        return None
    def _find(self, value, current_node):
        if value == current_node.value:
            same_value  = current_node.value 
            return same_value
        elif value < current_node.value and current_node.left_child != None:
            return self._find(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child != None:
            return self._find(value, current_node.right_child)


# def fill_tree(tree, num_elems = 100, max_int = 1000):
#     from random import randint 
#     for _ in range(num_elems):
#         cur_elem = randint(0, max_int)
#         tree.insert(cur_elem)
#     return tree

tree = BinarySearchTree()


tree.insert(0)
tree.insert(5)
tree.insert(4)
tree.insert(9)
tree.insert(8)
tree.insert(7)
tree.insert(11)
tree.insert(12)
tree.insert(13)
tree.insert(12)
tree.insert(12)

print(tree.erase(11))

print(tree.contains(10))
print(tree.contains(11))
print(tree.preorder())
print(tree.inorder())
print(tree.postorder())
print(tree.get_height())
print(tree.find(8))
