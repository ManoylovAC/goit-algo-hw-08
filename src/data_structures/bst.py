class Node:
    """Node of a Binary Search Tree."""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        result = "\t" * level + prefix + str(self.key) + "\n"

        if self.left:
            result += self.left.__str__(level + 1, "L--- ")

        if self.right:
            result += self.right.__str__(level + 1, "R--- ")

        return result


class BinarySearchTree:
    """Binary Search Tree implementation."""

    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root) if self.root else "Empty Binary Search Tree"

    # ==========================================================
    # Public methods

    def insert(self, key):
        """Insert a key into the tree."""

        def insert_node(root):
            if root is None:
                return Node(key)

            if key < root.key:
                root.left = insert_node(root.left)
            else:
                root.right = insert_node(root.right)

            return root

        self.root = insert_node(self.root)

    def search(self, key):
        """Search for a key."""

        def search_node(root):
            if root is None or root.key == key:
                return root

            if key < root.key:
                return search_node(root.left)

            return search_node(root.right)

        return search_node(self.root)

    def delete(self, key):
        """Delete a key from the tree."""

        def delete_node(root, key):
            if root is None:
                return root

            if key < root.key:
                root.left = delete_node(root.left, key)

            elif key > root.key:
                root.right = delete_node(root.right, key)

            else:
                if root.left is None:
                    return root.right

                if root.right is None:
                    return root.left

                successor = self.min_value_node(root.right)
                root.key = successor.key
                root.right = delete_node(root.right, successor.key)

            return root

        self.root = delete_node(self.root, key)

    # ==========================================================
    # Helper methods

    @staticmethod
    def min_value_node(node):
        """Return the node with the smallest key."""

        while node.left:
            node = node.left

        return node


if __name__ == "__main__":
    tree = BinarySearchTree()

    print("========= Insert =========")
    for key in [5, 3, 2, 4, 7, 6, 8]:
        tree.insert(key)

    print(tree)

    print("\n========= Search =========")
    print(tree.search(6))
    print(tree.search(100))

    print("\n========= Delete =========")
    tree.delete(7)
    print(tree)

    tree.delete(5)
    print(tree)
