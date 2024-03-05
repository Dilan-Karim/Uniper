from src.exercise_3.binary_node import BinaryNode


class BinarySearchTree:
    """
    Binary Search Tree

    A binary search tree is a binary tree in which each node has a value that is greater
    than the node values in the left subtree, and less than the node values in the right
    subtree. This tree ignores duplicate values.

    The implementation below uses the class BinaryNode.

    Some methods are implemented already, and you ara allowed to change them.

    Exercise: Complete the implementation of the remaining methods.
    """
    def __init__(self):
        self.root = None

    def insert(self, new_number: int) -> None:
        """Inserts a new number in a tree."""

        if self.root is None:
            self.root = BinaryNode(new_number)
        else:
            parent = None
            child = self.root

            while child is not None:
                parent = child
                if new_number < child.element:  # number already in tree
                    child = child.left
                elif new_number > child.element:
                    child = child.right

            if new_number < parent.element:
                parent.left = BinaryNode(new_number)
            else:
                parent.right = BinaryNode(new_number)

    def maximum_recursive(self) -> int:
        """Searches the maximum value in the tree recursively. If the tree is empty, it
        throws a ValueError exception."""
        return -1

    def maximum_iterative(self) -> int:
        """Searches the maximum value in the tree iteratively. If the tree is empty,
        it throws a ValueError exception."""
        return -1

    def height(self) -> int:
        """Calculates the height of the tree. An empty tree has height 0. A tree with
        one node has height 1."""

        return -1

    def sum(self) -> int:
        """Calculates the sum of all the values in the tree. An empty tree has sum 0."""

        return -1

    def reverse_order(self) -> str:
        """Returns a string representation of the tree in descending order. The values
        are comma separated ("12, 8, 2, 0, -1, ") with a trailing comma and a space."""

        return "fail"
