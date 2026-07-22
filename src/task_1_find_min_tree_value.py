from data_structures import AVLTree, BinarySearchTree


def find_min(tree):
    """Return the minimum key in a search tree."""

    current = tree.root

    if current is None:
        return None

    while current.left:
        current = current.left

    return current.key


def test_tree(tree, keys):
    """Fill a tree with keys and print the minimum value."""

    for key in keys:
        tree.insert(key)

    print(tree)
    print("Minimum:", find_min(tree))


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
