from node import Node
from tree import Tree

elements = [2, 3, 6, 0, -1]
tree = Tree()
root = tree.make_tree(elements)
print('\nTree')
tree.print_tree(root)
print('\nLeaves')
tree.print_leafs(root)
print('\nDepth of tree:{}'.format(tree.tree_depth(root)))
print('in order: ')
tree.in_order(root)
print('\npre order: ')
tree.pre_order(root)
print('\npost order: ')
tree.post_order(root)
print('\nDFS: ')
tree.depth_first(root)
