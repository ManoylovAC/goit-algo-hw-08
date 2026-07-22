from data_structures import AVLTree, BinarySearchTree


def calculate_tree_sum(node):
    """Return the sum of all node values in the tree."""

    if node is None:
        return 0

    return node.key + calculate_tree_sum(node.left) + calculate_tree_sum(node.right)


def test_tree(tree, keys):
    """Fill a tree and print the sum of all node values."""

    for key in keys:
        tree.insert(key)

    print(tree)
    print(f"Sum: {calculate_tree_sum(tree.root)}")


if __name__ == "__main__":
    print("\n======= AVL Tree =======")
    test_tree(
        AVLTree(),
        [40, 20, 60, 10, 30, 50, 70, 5],
    )

    print("\n======= Binary Search Tree =======")
    test_tree(
        BinarySearchTree(),
        [50, 30, 70, 20, 40, 60, 80, 10],
    )
