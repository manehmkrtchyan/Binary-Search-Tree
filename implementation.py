class Node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None 
    
    def insert(self, value):
        if not isinstance(value,int):
            raise Exception("Please, enter an integer!")
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
        (self._levelorder(self.root))

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

    def __contains__(self, value):
        if self.root != None:
            return self._contains(value, self.root)
        else:
            return False

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
    
    # global lst
    # lst = []
    global lst1
    lst1 = []

    def inorder_to_list(self, lst):
        return (self._inorder_to_list(self.root, lst))

    def _inorder_to_list(self, current, lst):
        if current != None:
            self._inorder_to_list(current.left_child, lst)
            lst.append(current.value)
            self._inorder_to_list(current.right_child, lst)
        return (lst)
    
    def merge(self, other_tree):
        other_tree.inorder_to_list(lst1)
        for ele in set(lst1):
            self.insert(ele)
        print(self)

    def clear(self):
        self.del_leaf_node(self.root)
        self.erase(self.root.value)

    def del_leaf_node(self, root):
        if root is None:
            return None
        if (root.left_child is None) and (root.right_child is None):
            return None
        root.left_child = self.del_leaf_node(root.left_child)
        root.right_child = self.del_leaf_node(root.right_child)

    def __eq__(self, other):
        if self.root is None and other.root is None:
            return True
        if (self.root and other.root) and (self.root.value == other.root.value):
            left = self.root.left_child.__eq__(other.root.left_child) 
            right = self.root.right_child.__eq__(other.root.right_child)
            if left is True and right is True:
                return True
            return False
        return False

    def __ne__(self, other):
        if self.root is None and other.root is None:
            return False
        if (self.root and other.root) and (self.root.value == other.root.value):
            left = self.root.left_child.__eq__(other.root.left_child) 
            right = self.root.right_child.__eq__(other.root.right_child)
            if left is True and right is True:
                return False
            return True
        return True

    def __str__(self):
        result = self._print(self.root, 0)
        return str(result)

    def _print(self, node, level):
        if node != None:
            self._print(node.left_child, level + 1)
            print(' ' * 4 * level + '->' + str(node.value))
            self._print(node.right_child, level + 1)
        
    
    def __iadd__(self, other):
        return self._iadd(self.root, other, other.root)
    def _iadd(self, node1, other, node2):
        if not node1:
            return other
        if not node2:
            return self
        node1.value += node2.value
        self._iadd(node1.left_child, other, node2.left_child)
        self._iadd(node1.right_child, other, node2.right_child)
        return self

    global lst2, lst3
    lst2 = []
    lst3 = []
    
    def __add__(self, other):
        new_tree = BinarySearchTree()
        self.inorder_to_list(lst2)
        other.inorder_to_list(lst3)
        if len(lst3) > len(lst2):
            times = len(lst3) - len(lst2)
            while times > 0:
                lst2.append(0)
                times -= 1
        else:
            times = len(lst2) - len(lst3)
            while times > 0:
                lst3.append(0)
                times -= 1
        res_lst = lst3
        for i in range(len(res_lst)):
            res_lst[i] += lst2[i]
        import random
        random.shuffle(res_lst)
        for i in res_lst:
            new_tree.insert(i)
        return new_tree    
