import implementation as imp

tree1 = imp.BinarySearchTree()
tree2 = imp.BinarySearchTree()
tree3 = imp.BinarySearchTree()

"""
'Insert' function adds elements to the Binary Search Tree.
It raises an exception the user inserts a non-integer value, telling to input a number.
"""
tree1.insert(5)
tree1.insert(10)
tree1.insert(3)
tree1.insert(8)
tree1.insert(2)
tree1.insert(4)

tree3.insert(300)
tree3.insert(600)
tree3.insert(100)
tree3.insert(400)
tree3.insert(500)
tree3.insert(200)


"""
Overloading the '+=' operator.
This operator returns the sum of two binary trees adding the value of each of the nodes from the second tree
to the corresponding node from the first tree.
That is it returns the first tree changed in-place.
The operator doesn't move the nodes from the second tree to the first one in case the corresponding nodes from the first tree
don't exist.
"""
tree1 += tree3
print(tree1)