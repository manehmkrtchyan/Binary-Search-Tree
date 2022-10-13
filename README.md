Binary Search Tree is a node-based binary tree data structure which has the following properties:

The left subtree of a node contains only nodes with keys lesser than the node’s key.
The right subtree of a node contains only nodes with keys greater than the node’s key.
The left and right subtree each must also be a binary search tree.


First to build a Binary Search Tree the user needs to insert the elements. That can be done with the insert() function. The user needs to call the frunction on the tree object that was declared earlier(for example tree = BinarySearchTree()) and give the node value as an argument. The result will be something like this: tree.insert(5). Now the user has got a binary search tree with one node, that has 5 as a value. The user can insert as many nodes as he/she wants. To see the tree represented on the standart output the user needs to use the print() function.
Also the user can use all the functions and operations listed below in the same way.


Operators
● Copy operator assignment =
● Move operator assignment =
● Operator stream out (cout) <<
● Operator is equal to ==
● Operator not equal to !=
● Operator +, +=

Functions
● insert ()
● clear ()
● get_height ()
● erase ()
● get_number_of_nodes ()
● preorder ()
● inorder
● postorder ()
● levelorder ()
● get_root_data ()
● merge ()
● contains ()
● find ()
