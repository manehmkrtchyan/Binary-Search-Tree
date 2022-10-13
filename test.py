import implementation as imp

tree1 = imp.BinarySearchTree()
tree2 = imp.BinarySearchTree()
tree3 = imp.BinarySearchTree()


"""
'Insert' function adds elements to the Binary Search Tree.
It raises an exception in case the user inserts a non-integer value, telling to input a number.
The funtion can also get non positive numbers.
"""
tree1.insert(5)
tree1.insert(10)
tree1.insert(3)
tree1.insert(-8)
tree1.insert(2)
tree1.insert(4)

tree3.insert(300)
tree3.insert(600)
tree3.insert(300)
tree3.insert(400)
tree3.insert(500)
tree3.insert(200)

"""
'Inorder' function returns the inordered tree.
The algorithm is to do the following 
Traverse the left subtree, i.e., call Inorder(left->subtree)
Visit the root.
Traverse the right subtree, i.e., call Inorder(right->subtree)
'Preorder' function does the following actions:
Visit the root.
Traverse the left subtree, i.e., call Preorder(left->subtree)
Traverse the right subtree, i.e., call Preorder(right->subtree) 
And the 'Postorder' function
Traverses the left subtree, i.e., call Postorder(left->subtree)
Traverses the right subtree, i.e., call Postorder(right->subtree)
Visits the root
"""
tree1.inorder()
tree1.preorder()
tree1.postorder()

"""
Level Order Traversal is the algorithm to process all nodes of a tree by traversing through depth, first the root, then the child of the root, etc.
"""
tree1.levelorder()

"""
'erase' function gets a value and deletes the node with that value.
In case getting a non-integer value, it raises an exception.
"""
#tree1.erase("hello")
tree1.erase(3)

"""
'get_height' function returns the height of the Binary Search Tree.
"""
tree1.get_height()

"""
The 'contains' function gets a value as an argument and returns True if the value is available in the tree and False if it is not.
You can also use 'in' operater, which is overloaded for a Binary Search Tree.
"""
print(tree1.contains(10))
print(10 in tree1)

"""
The 'find' function gets a value as an argument, finds the node with that value in the tree and returns another 
variable with that same value.
Returns None in case the node with the value given as an argument doesn't exist.
"""
#es funkcian skzbic enpes ei grel, vor iren poxancvac valueov node i 16-akan hascen veradardzner, 
# heto Johny pahanjy poxec, dra hamar hima ed valuen veragrum e urish popoxakani u return anum.
print(tree1.find(7))
print(tree1.find(-8))

"""
The function 'get_root_data' returns the value of the root node.
"""
print(tree1.get_root_data())

"""
The function 'get_number_of_nodes' returns the number of the nodes of the tree. 
Returns 0 if the tree doesn't have nodes.
"""
print(tree1.get_number_of_nodes())

"""
The function 'merge' gets two trees as arguments and merges the second tree on the firs one.
Returns a tree,  which consists of all the elemens both from the first and the second trees.
In case getting an empty tree(None) as an argument, the function returns the other non-empty tree.
"""
tree1.merge(tree3)
tree2.merge(tree2) #tree2 is None

"""
The function 'clear' erases all the nodes of the tree.
"""

"""
'__eq__' is the magic method for the operator ==
This checks if two Binary Search Trees are equal.
"""
print(tree1 == tree3)

"""
'__ne__' is the magic method for the operator !=
This checks if two Binary Search Trees are not equal.
"""
print(tree1 != tree3)

"""
The operator '+=' returns the sum of two binary trees adding the value of each of the nodes from the second tree
to the corresponding node from the first tree.
That is it returns the first tree changed in-place.
The operator doesn't move the nodes from the second tree to the first one in case the corresponding nodes from the first tree
don't exist.
Magic method for this operator is __iadd__.
"""
tree1 += tree3
print(tree1)

"""
The operator '+' returns the sum of two binary trees adding the values of the corresponding nodes.
Magic method for this operator is __add__.
Unlike the __iadd__ function, this one returns a new tree.
"""
print(tree1 + tree3)

"""
'print' function prints the tree.
The magic method for print is __str__.
If the function gets an empty tree as an argument, it will return None
"""
print(tree1)
