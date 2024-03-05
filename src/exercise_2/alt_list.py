from typing import List, Optional

from src.exercise_2.node import Node


class AltList:
    """
    List

    It uses the class Node

    Exercise: Complete the implementation of the methods below:
    """
    def __init__(self, elements: Optional[list] = None):
        """Creates an instance of AltList. If a python 'list' is given as an input, an
        'alt list' is created from it. The order of the elements should be preserved. If
        no elements are input, an empty AltList will be created."""
        self.head = None

    def add(self, element: int) -> None:
        """Adds an element to the end of the list."""

    def get(self, index: int) -> int:
        """Returns the element at the specified position in this list. If the index
        exceeds the length of the list, returns the last element. You can assume that
        the index is non-negative and that at least one element is in the list."""

        return -1

    def get_length(self) -> int:
        """Returns the number of elements in this list. An empty list has length 0."""

        return -1

    def add_all(self, elements: List[int]) -> None:
        """Adds all the elements of the specified array to the end of the list. The
        order of the elements in the array should be preserved."""

    def to_string(self) -> str:
        """Returns a string representation of the list. The elements are comma
        separated ("1,2,3,4,5") without a trailing comma and space. An empty list
        is represented by an empty string."""

        return "fail"

    def find(self, element: int) -> int:
        """Returns the index of the first occurrence of the specified element in this
        list or -1 of this list does not contain the element."""

        return -7

    def find_last(self, element: int) -> int:
        """Returns the index of the last occurrence of the specified element in this
        list or -1 if this list does not contain the element."""

        return -5

    def remove(self, index: int) -> None:
        """Removes the element at the specified position in this list. If the index
        exceeds the length of the list or is negative, does nothing. Take care of the
        case where the list is empty."""

    def remove_first_occurrence(self, element: int) -> None:
        """Removes the first occurrence of the specified element from this list, if it
        is present. If the list does not contain the element, it is unchanged."""

    def remove_last_occurrence(self, element: int) -> None:
        """Removes the last occurrence of the specified element from this list, if it
        is present. If the list does not contain the element, it is unchanged."""

    def sort(self) -> None:
        """Sorts the list in ascending numerical order by using any sorting algorithm.
        This list instance is modified."""
