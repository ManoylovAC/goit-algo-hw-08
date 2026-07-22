class AVLNode:
    """Node of an AVL tree."""

    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        result = "\t" * level + prefix + str(self.key) + "\n"

        if self.left:
            result += self.left.__str__(level + 1, "L--- ")

        if self.right:
            result += self.right.__str__(level + 1, "R--- ")

        return result


class AVLTree:
    """AVL Tree implementation."""

    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root) if self.root else "Empty AVL Tree"

    # ==========================================================
    # Public methods

    def insert(self, key):
        """Insert a key into the AVL tree."""

        def insert_node(root):
            if root is None:
                return AVLNode(key)

            if key < root.key:
                root.left = insert_node(root.left)
            elif key > root.key:
                root.right = insert_node(root.right)
            else:
                return root

            root.height = 1 + max(
                self.get_height(root.left),
                self.get_height(root.right),
            )

            balance = self.get_balance(root)

            # Left Left
            if balance > 1 and key < root.left.key:
                return self.right_rotate(root)

            # Left Right
            if balance > 1 and key > root.left.key:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

            # Right Right
            if balance < -1 and key > root.right.key:
                return self.left_rotate(root)

            # Right Left
            if balance < -1 and key < root.right.key:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

            return root

        self.root = insert_node(self.root)

    def delete(self, key):
        """Delete a key from the AVL tree."""

        def delete_node(root):
            if root is None:
                return root

            if key < root.key:
                root.left = delete_node(root.left)

            elif key > root.key:
                root.right = delete_node(root.right)

            else:
                if root.left is None:
                    return root.right

                if root.right is None:
                    return root.left

                successor = self.min_value_node(root.right)
                root.key = successor.key
                root.right = delete_node(root.right)

            if root is None:
                return root

            root.height = 1 + max(
                self.get_height(root.left),
                self.get_height(root.right),
            )

            balance = self.get_balance(root)

            # Left Left
            if balance > 1 and self.get_balance(root.left) >= 0:
                return self.right_rotate(root)

            # Left Right
            if balance > 1 and self.get_balance(root.left) < 0:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

            # Right Right
            if balance < -1 and self.get_balance(root.right) <= 0:
                return self.left_rotate(root)

            # Right Left
            if balance < -1 and self.get_balance(root.right) > 0:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

            return root

        self.root = delete_node(self.root)

    def search(self, key):
        """Search for a key in the tree."""

        def search_node(root):
            if root is None or root.key == key:
                return root

            if key < root.key:
                return search_node(root.left)

            return search_node(root.right)

        return search_node(self.root)

    # ==========================================================
    # Helper methods

    @staticmethod
    def get_height(node):
        return node.height if node else 0

    def get_balance(self, node):
        if node is None:
            return 0

        return (self.get_height(node.left)  - self.get_height(node.right))

    @staticmethod
    def min_value_node(node):
        while node.left:
            node = node.left

        return node

    def left_rotate(self, node):
        new_root = node.right
        subtree = new_root.left

        new_root.left = node
        node.right = subtree

        node.height = 1 + max(
            self.get_height(node.left),
            self.get_height(node.right),
        )

        new_root.height = 1 + max(
            self.get_height(new_root.left),
            self.get_height(new_root.right),
        )

        return new_root

    def right_rotate(self, node):
        new_root = node.left
        subtree = new_root.right

        new_root.right = node
        node.left = subtree

        node.height = 1 + max(
            self.get_height(node.left),
            self.get_height(node.right),
        )

        new_root.height = 1 + max(
            self.get_height(new_root.left),
            self.get_height(new_root.right),
        )

        return new_root


if __name__ == "__main__":
    avl_tree = AVLTree()

    print("========= AVL TREE =========")
    for key in [10, 20, 30, 25, 28, 27, -1]:
        avl_tree.insert(key)

    print(avl_tree)

    print("\n========= Search =========")
    print(avl_tree.search(28))
    print(avl_tree.search(100))

    print("\n========= Delete =========", end="")
    for key in [10]:
        avl_tree.delete(key)
        print(f"\nDeleted: {key}")
        print(avl_tree)
