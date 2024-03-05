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
        self.tail = None
        if elements:
            for element in elements:
                self.add(element)

    def add(self, element: int) -> None:
        """Adds an element to the end of the list."""
        # Create a new node with the given data
        new_node = Node(element)

        if self.head is None:
            # If the list is empty, set the new node as both head and tail
            self.head = new_node
            self.tail = new_node

        else:
            # Otherwise, add the new node to the end of the list
            self.tail.next = new_node
            self.tail = new_node
        
    def get(self, index: int) -> int:
        """Returns the element at the specified position in this list. If the index
        exceeds the length of the list, returns the last element. You can assume that
        the index is non-negative and that at least one element is in the list."""
        counter = 0
        current = self.head
        # Traverse the list to find the element at the given index
        while current:
            if counter == index:
                return current.value
            current = current.next
            counter += 1
        return self.tail.value

    def get_length(self) -> int:
        """Returns the number of elements in this list. An empty list has length 0."""
        counter = 0
        current = self.head
        # Traverse the list to count the number of elements
        while current:
            counter += 1
            current = current.next

        return counter

    def add_all(self, elements: List[int]) -> None:
        """Adds all the elements of the specified array to the end of the list. The
        order of the elements in the array should be preserved."""
        for element in elements:
            self.add(element)
        

    def to_string(self) -> str:
        """Returns a string representation of the list. The elements are comma
        separated ("1,2,3,4,5") without a trailing comma and space. An empty list
        is represented by an empty string."""
        current = self.head
        result = ""
        # Traverse the list to create the string representation
        while current:
            result += str(current.value)
            current = current.next
            if current:
                result += ","
        return result

    def find(self, element: int) -> int:
        """Returns the index of the first occurrence of the specified element in this
        list or -1 of this list does not contain the element."""
        counter = 0
        current = self.head
        # Traverse the list to find the index of the first occurrence of the element
        while current:
            if current.value == element:
                return counter
            current = current.next
            counter += 1
        return -1

    def find_last(self, element: int) -> int:
        """Returns the index of the last occurrence of the specified element in this
        list or -1 if this list does not contain the element."""
        counter = 0
        last_index = -1
        current = self.head
        # Traverse the list to find the index of the last occurrence of the element
        while current:
            if current.value == element:
                last_index = counter
            current = current.next
            counter += 1

        return last_index

    def remove(self, index: int) -> None:
        """Removes the element at the specified position in this list. If the index
        exceeds the length of the list or is negative, does nothing. Take care of the
        case where the list is empty."""

        # empty case or invalid index
        if self.head is None or index < 0:
            return

        # remove first element
        if index == 0:
            # If the first element is to be removed, update the head
            self.head = self.head.next
            # check if the list is empty
            if self.head is None:
                self.tail = None
            return
        
        # remove non first element
        counter = 0
        current = self.head
        # Traverse the list to find the element at the given index

        while current.next:  # Ensuring current.next exists simplifies logic for accessing current.next.next
            if counter == index - 1:
                if current.next.next:
                    current.next = current.next.next
                else:  # Removing the last element
                    current.next = None
                    self.tail = current  # Update the tail
                return
            current = current.next
            counter += 1
        return


    def remove_first_occurrence(self, element: int) -> None:
        """Removes the first occurrence of the specified element from this list, if it
        is present. If the list does not contain the element, it is unchanged."""
        current = self.head
        previous = None
        # Traverse the list to find the first occurrence of the element
        while current:
            if current.value == element:
                # If the element is found, remove it from the list
                if previous:
                    previous.next = current.next
                    # If removing the last element, update the tail
                    if previous.next is None:
                        self.tail = previous
                else:
                    self.head = current.next
                    # If the list becomes empty, update the tail to None
                    if self.head is None:
                        self.tail = None
                return
            previous = current
            current = current.next
        

    def remove_last_occurrence(self, element: int) -> None:
        """Removes the last occurrence of the specified element from this list, if it
        is present. If the list does not contain the element, it is unchanged."""
        current = self.head
        previous = None
        last = None

        # Traverse the list to find the last occurrence of the element
        while current:
            if current.value == element:
                last = (previous, current)
            previous = current
            current = current.next

        if last:
            last_occurrence_prev, last_occurrence = last
            # If the last occurrence is the first element
            if last_occurrence_prev is None:
                self.head = last_occurrence.next
                # If the list becomes empty, update the tail to None
                if self.head is None:
                    self.tail = None
            else:
                last_occurrence_prev.next = last_occurrence.next
                # If removing the last element, update the tail
                if last_occurrence_prev.next is None:
                    self.tail = last_occurrence_prev
                return
        
            


    def sort(self) -> None:
        """Sorts the list in ascending numerical order by using any sorting algorithm.
        This list instance is modified."""
        if self.head is None:
            return
        

        current = self.head
        # Traverse the list to sort it
        while current:
            next = current.next
            # Employ the bubble sort algorithm
            while next:
                if current.value > next.value:
                    current.value, next.value = next.value, current.value
                next = next.next
            current = current.next
        