from node import Node
from Tree import Tree

elements = [2, 3, 6, 0, -1]
tree = Tree()
root = tree.make_tree(elements)

print('\nLeaves')
tree.print_leaves(root)
print('\nDepth of tree:{}'.format(tree.tree_height(root)))
print('in order: ')
tree.in_order(root)
print('\nDFS: ')
tree.depth_search(root)
