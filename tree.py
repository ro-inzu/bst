from node import Node


class Tree(object):
    def in_order(self, node: Node):
        if not node:
            return node
        self.in_order(node.left)
        print(node.data)
        self.in_order(node.right)

    def tree_height(self, node: Node, height=0):
        # base case
        if node is None:
            return height
        else:
            # get height of the most left and right and get the side with most depth
            return max(self.tree_height(node.left, height + 1), self.tree_height(node.right, height + 1))

    # bfs traversal
    def level_search(self, root):
        if not root:
            return root

        # queue to traverse through the tree
        queue = [root]
        while queue:
            # get current level of tree
            child = queue.pop(0)
            print(f"{child.data}")
            # check if there is a child on left side to traverse through
            if child.left is not None:
                queue.append(child.left)
            # check if there is a child on right side to traverse through
            if child.right is not None:
                queue.append(child.right)

    def depth_search(self, root):
        if not root:
            return root

        if root.left:
            self.depth_search(root.left)

        print(f"{root.data}")

        if root.right:
            self.depth_search(root.right)

    def print_leaves(self, root):
        # base case
        if not root:
            return root
        # it is a leaf is there is nothing to left and right of the node
        if root.left is None and root.right is None:
            print(root.data)
        # if there is a node on left of current move to left
        if root.left:
            self.print_leaves(root.left)
        if root.right:
            self.print_leaves(root.right)

    def insert_node(self, root: Node, data: int):
        if root is None:
            root = Node(data)
            return root

        if data < root.data:
            root.left = self.insert_node(root.left, data)
        elif data > root.data:
            root.right = self.insert_node(root.right, data)
        return root

    def make_tree(self, elements: list):
        root_node = Node(1)
        for element in elements:
            self.insert_bst(root_node, element)

        return root_node
