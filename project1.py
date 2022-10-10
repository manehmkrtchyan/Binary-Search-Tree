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

    def levelorder(self):
        self._levelorder(self.root)
    def _levelorder(self, root):
        queue = []
        queue.append(root)
        while len(queue) != 0:
            root = queue.pop(0)
            print(root.value)
            if root.left_child is not None:
                queue.append(root.left_child)
            if root.right_child is not None:
                queue.append(root.right_child)    


    def erase(self, value):
        self._erase(self.root, value, None, None)
    def _erase(self, current, value, previous, is_left):
        if current:
            if current.value == value:
                if current.left_child is None and current.right_child is None: #The node is a leaf node
                    if previous:
                        if is_left: previous.left_child = None                            
                        else: previous.right_child = None                             
                    else: self.root = None                        
                elif current.left_child is None: #The left child is None
                    if previous:
                        if is_left: previous.left_child = current.right_child
                        else: previous.right_child = current.right_child                           
                    else: previous.root = current.right_child
                elif current.right_child == None: #The right child is None
                    if previous:
                        if is_left: previous.left_child == current.left_child
                        else: previous.right_child = current.left_child
                    else: self.root = current.left_child
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


    def get_root_data(self):
        return self.root.value
    
    def get_number_of_nodes(self):
        return self._get_number_of_nodes(self.root)
    def _get_number_of_nodes(self, child):
        if child == None:
            return 0
        return 1 + self._get_number_of_nodes(child.left_child) + self._get_number_of_nodes(child.right_child) 
    

    # def clear(self):
    #     self._clear(self.root)
    # def _clear(self, current):
    #     self._clear(current.left_child)
    #     self._clear(current.right_child)
    #     current.value = None
    global lst;
    lst = []
    def inorder_to_list(self):
        return (self._inorder_to_list(self.root))
    def _inorder_to_list(self, current):
        if current != None:
            self._inorder_to_list(current.left_child)
            lst.append(current.value)
            self._inorder_to_list(current.right_child)
        return (lst)
    def merge(self, tree2):
        tree2.inorder_to_list()
        for ele in set(lst):
            self.insert(ele)
        return self.inorder()

        


    
         
        


tree1 = BinarySearchTree()
tree2 = BinarySearchTree()


tree1.insert(5)
tree1.insert(10)
tree1.insert(3)
tree1.insert(8)
tree1.insert(2)
tree1.insert(4)

tree2.insert(10)
tree2.insert(20)
tree2.insert(30)
tree2.insert(100)
tree2.insert(200)
tree2.insert(300)

# print(tree.erase(11))

# print(tree.contains(10))
# print(tree.contains(11))
# print(tree.preorder())
# print(tree.inorder())
# print(tree.postorder())
# print(tree.get_height())
# print(tree.find(8))
#print(tree1.preorder())
#print(tree1.inorder())
#print(tree1.postorder())
#print(tree1.get_root_data())
#print(tree1.levelorder())
print(tree1.merge(tree2))
