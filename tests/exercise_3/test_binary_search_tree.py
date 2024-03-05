from unittest import TestCase

from src.exercise_3.binary_search_tree import BinarySearchTree


class TestBinarySearchTree(TestCase):
    def test_maximum_recursive(self):

        tree = BinarySearchTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        tree.insert(2)
        tree.insert(4)
        tree.insert(6)
        tree.insert(8)

        actual = tree.maximum_recursive()
        self.assertEqual(actual, 8)

    def test_maximum_recursive_single_entry(self):

        tree = BinarySearchTree()
        tree.insert(5)

        actual = tree.maximum_recursive()
        self.assertEqual(actual, 5)

    def test_maximum_recursive_on_empty_tree_raises_value_error(self):
        tree = BinarySearchTree()

        self.assertRaises(ValueError, tree.maximum_recursive)

    def test_maximum_iterative(self):
        tree = BinarySearchTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(8)
        tree.insert(2)
        tree.insert(4)
        tree.insert(6)
        tree.insert(9)

        actual = tree.maximum_iterative()
        self.assertEqual(actual, 9)

    def test_maximum_iterative_single_entry(self):
        tree = BinarySearchTree()
        tree.insert(5)

        actual = tree.maximum_iterative()
        self.assertEqual(actual, 5)

    def test_maximum_iterative_raises_value_error_if_empty_tree(self):
        tree = BinarySearchTree()

        self.assertRaises(ValueError, tree.maximum_iterative)

    def test_height_3(self):
        tree = BinarySearchTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        tree.insert(2)
        tree.insert(4)
        tree.insert(6)
        tree.insert(9)

        actual = tree.height()
        self.assertEqual(actual, 3)

    def test_height_4(self):
        tree = BinarySearchTree()
        tree.insert(6)
        tree.insert(4)
        tree.insert(8)
        tree.insert(3)
        tree.insert(5)
        tree.insert(7)
        tree.insert(9)
        tree.insert(1)

        actual = tree.height()
        self.assertEqual(actual, 4)

    def test_height_42(self):
        tree = BinarySearchTree()
        tree.insert(5)
        tree.insert(2)
        tree.insert(7)
        tree.insert(1)
        tree.insert(4)
        tree.insert(6)
        tree.insert(8)
        tree.insert(0)
        tree.insert(9)

        actual = tree.height()
        self.assertEqual(actual, 4)

    def test_height_5(self):
        tree = BinarySearchTree()
        tree.insert(8)
        tree.insert(6)
        tree.insert(10)
        tree.insert(5)
        tree.insert(7)
        tree.insert(9)
        tree.insert(11)
        tree.insert(4)
        tree.insert(12)
        tree.insert(13)

        actual = tree.height()
        self.assertEqual(actual, 5)

    def test_height_52(self):
        tree = BinarySearchTree()
        tree.insert(7)
        tree.insert(5)
        tree.insert(9)
        tree.insert(4)
        tree.insert(6)
        tree.insert(8)
        tree.insert(10)
        tree.insert(3)
        tree.insert(11)
        tree.insert(12)
        tree.insert(-1)

        actual = tree.height()
        self.assertEqual(actual, 5)

    def test_height_single_entry(self):
        tree = BinarySearchTree()
        tree.insert(7)
        actual = tree.height()
        self.assertEqual(actual, 1)

    def test_height_if_empty_tree(self):
        tree = BinarySearchTree()

        actual = tree.height()
        self.assertEqual(actual, 0)

    def test_sum_3(self):
        tree = BinarySearchTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        tree.insert(2)
        tree.insert(4)
        tree.insert(6)
        tree.insert(10)

        actual = tree.sum()
        self.assertEqual(actual, 37)

    def test_sum_4(self):
        tree = BinarySearchTree()
        tree.insert(6)
        tree.insert(4)
        tree.insert(9)
        tree.insert(3)
        tree.insert(5)
        tree.insert(8)
        tree.insert(10)
        tree.insert(2)

        actual = tree.sum()
        self.assertEqual(actual, 47)

    def test_sum_5(self):
        tree = BinarySearchTree()
        tree.insert(7)
        tree.insert(4)
        tree.insert(9)
        tree.insert(3)
        tree.insert(5)
        tree.insert(8)
        tree.insert(10)
        tree.insert(2)
        tree.insert(11)
        tree.insert(12)
        tree.insert(-1)

        actual = tree.sum()
        self.assertEqual(actual, 70)

    def test_sum_single_entry(self):
        tree = BinarySearchTree()
        tree.insert(5)

        actual = tree.sum()
        self.assertEqual(actual, 5)

    def test_sum_if_empty_tree(self):
        tree = BinarySearchTree()

        actual = tree.sum()
        self.assertEqual(actual, 0)

    def test_reverse_order_3(self):
        tree = BinarySearchTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        tree.insert(2)
        tree.insert(4)
        tree.insert(6)
        tree.insert(10)

        actual = tree.reverse_order()
        self.assertEqual(actual, "10, 7, 6, 5, 4, 3, 2, ")

    def test_reverse_order_4(self):
        tree = BinarySearchTree()
        tree.insert(6)
        tree.insert(4)
        tree.insert(9)
        tree.insert(3)
        tree.insert(5)
        tree.insert(8)
        tree.insert(10)
        tree.insert(2)

        actual = tree.reverse_order()
        self.assertEqual(actual, "10, 9, 8, 6, 5, 4, 3, 2, ")

    def test_reverse_order_5(self):
        tree = BinarySearchTree()
        tree.insert(7)
        tree.insert(5)
        tree.insert(9)
        tree.insert(4)
        tree.insert(6)
        tree.insert(8)
        tree.insert(10)
        tree.insert(3)
        tree.insert(11)
        tree.insert(12)
        tree.insert(-1)

        actual = tree.reverse_order()
        self.assertEqual(actual, "12, 11, 10, 9, 8, 7, 6, 5, 4, 3, -1, ")

    def test_reverse_order_single_entry(self):
        tree = BinarySearchTree()
        tree.insert(7)

        actual = tree.reverse_order()
        self.assertEqual(actual, "7, ")

    def test_reverse_order_empty_tree(self):
        tree = BinarySearchTree()
        actual = tree.reverse_order()
        self.assertEqual(actual, "")
