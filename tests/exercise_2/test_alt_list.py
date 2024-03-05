from unittest import TestCase

from src.exercise_2.alt_list import AltList


class TestList(TestCase):
    def test_get_from_single_element_list(self):
        l = AltList()
        l.add(1)

        self.assertEqual(l.get(0), 1)

    def test_get_from_too_big_index(self):

        l = AltList()
        l.add(1)

        self.assertEqual(l.get(10), 1)

    def test_add_adds_at_end(self):

        l = AltList()
        l.add(1)
        l.add(2)
        l.add(3)

        self.assertEqual(l.get(0), 1)
        self.assertEqual(l.get(1), 2)
        self.assertEqual(l.get(2), 3)

    def test_length_of_empty_list(self):

        l = AltList()
        self.assertEqual(l.get_length(), 0)

    def test_length_of_single_element_list(self):

        l = AltList()
        l.add(1)
        self.assertEqual(l.get_length(), 1)

    def test_length(self):

        l = AltList()
        l.add(1)
        l.add(2)
        l.add(3)
        self.assertEqual(l.get_length(), 3)

    def test_list_from_empty_array(self):
        l = AltList([])

        self.assertEqual(l.get_length(), 0)

    def test_list_from_single_entry_array(self):
        l = AltList([1])

        self.assertEqual(l.get_length(), 1)
        self.assertEqual(l.get(0), 1)

    def test_list_from_array(self):
        l = AltList([1, 2, 3])

        self.assertEqual(l.get_length(), 3)
        self.assertEqual(l.get(0), 1)
        self.assertEqual(l.get(1), 2)
        self.assertEqual(l.get(2), 3)

    def test_to_string_on_empty_list(self):
        l = AltList()
        self.assertEqual(l.to_string(), "")

    def test_to_string_on_single_element_list(self):
        l = AltList([1])
        self.assertEqual(l.to_string(), "1")

    def test_to_string(self):
        l = AltList([1, 2, 3])
        self.assertEqual(l.to_string(), "1,2,3")

    def test_find_missing_element_in_empty_list(self):
        l = AltList()
        self.assertEqual(l.find(4), -1)

    def test_find_single_element_list(self):
        l = AltList([1])
        self.assertEqual(l.find(1), 0)

    def test_find_missing_element_in_single_element_list(self):
        l = AltList([1])
        self.assertEqual(l.find(4), -1)

    def test_find(self):
        l = AltList([1, 2, 3])
        self.assertEqual(l.find(1), 0)
        self.assertEqual(l.find(2), 1)
        self.assertEqual(l.find(3), 2)

    def test_find_early(self):
        l = AltList([1, 2, 3, 2, 1, 4, 4])
        self.assertEqual(l.find(1), 0)
        self.assertEqual(l.find(2), 1)
        self.assertEqual(l.find(3), 2)
        self.assertEqual(l.find(4), 5)

    def test_find_last_missing_element(self):
        l = AltList([1, 2, 3])
        self.assertEqual(l.find_last(4), -1)

    def test_find_last_missing_element_in_empty_list(self):
        l = AltList()
        self.assertEqual(l.find_last(4), -1)

    def test_find_last_single_element_list(self):
        l = AltList([1])
        self.assertEqual(l.find_last(1), 0)

    def test_find_last_missing_element_in_single_element_list(self):
        l = AltList([1])
        self.assertEqual(l.find_last(4), -1)

    def test_find_last(self):
        l = AltList([1, 2, 3])
        self.assertEqual(l.find_last(1), 0)
        self.assertEqual(l.find_last(2), 1)
        self.assertEqual(l.find_last(3), 2)

    def test_find_last_late(self):
        l = AltList([1, 2, 3, 2, 1, 4, 4])
        self.assertEqual(l.find_last(1), 4)
        self.assertEqual(l.find_last(2), 3)
        self.assertEqual(l.find_last(3), 2)
        self.assertEqual(l.find_last(4), 6)

    def test_remove_from_empty_list(self):
        l = AltList()
        l.remove(1)
        self.assertEqual(l.get_length(), 0)

    def test_remove_out_of_range(self):
        l = AltList([1, 2, 3])
        l.remove(-1)
        self.assertEqual(l.get_length(), 3)
        self.assertEqual(l.get(0), 1)
        self.assertEqual(l.get(1), 2)
        self.assertEqual(l.get(2), 3)
        l.remove(3)
        self.assertEqual(l.get_length(), 3)
        self.assertEqual(l.get(0), 1)
        self.assertEqual(l.get(1), 2)
        self.assertEqual(l.get(2), 3)

    def test_remove(self):
        l = AltList([1, 2, 3])
        l.remove(1)
        self.assertEqual(l.get_length(), 2)
        self.assertEqual(l.get(0), 1)
        self.assertEqual(l.get(1), 3)
        l.remove(0)
        self.assertEqual(l.get_length(), 1)
        self.assertEqual(l.get(0), 3)
        l.remove(0)
        self.assertEqual(l.get_length(), 0)

    def test_remove_first_occurrence_from_empty_list(self):
        l = AltList()
        l.remove_first_occurrence(1)
        self.assertEqual(l.get_length(), 0)

    def test_remove_first_occurrence_out_of_range(self):
        l = AltList([1, 2, 3])
        l.remove_first_occurrence(-1)
        self.assertEqual(l.get_length(), 3)
        self.assertEqual(l.get(0), 1)
        self.assertEqual(l.get(1), 2)
        self.assertEqual(l.get(2), 3)

    def test_remove_first_occurrence(self):
        l = AltList([1, 5, 3, 4, 3, 4])
        l.remove_first_occurrence(3)
        self.assertEqual(l.get_length(), 5)
        self.assertEqual(l.get(0), 1)
        self.assertEqual(l.get(1), 5)
        self.assertEqual(l.get(2), 4)
        self.assertEqual(l.get(3), 3)
        self.assertEqual(l.get(4), 4)
        l.remove_first_occurrence(3)
        self.assertEqual(l.get_length(), 4)
        self.assertEqual(l.get(0), 1)
        self.assertEqual(l.get(1), 5)
        self.assertEqual(l.get(2), 4)
        self.assertEqual(l.get(3), 4)

    def test_remove_last_occurrence_from_empty_list(self):
        l = AltList()
        l.remove_last_occurrence(1)
        self.assertEqual(l.get_length(), 0)

    def test_remove_last_occurrence_out_of_range(self):
        l = AltList([1, 2, 3])
        l.remove_last_occurrence(-1)
        self.assertEqual(l.get_length(), 3)
        self.assertEqual(l.get(0), 1)
        self.assertEqual(l.get(1), 2)
        self.assertEqual(l.get(2), 3)

    def test_remove_last_occurrence(self):
        l = AltList([1, 5, 3, 4, 3, 4])
        l.remove_last_occurrence(3)
        self.assertEqual(l.get_length(), 5)
        self.assertEqual(l.get(0), 1)
        self.assertEqual(l.get(1), 5)
        self.assertEqual(l.get(2), 3)
        self.assertEqual(l.get(3), 4)
        self.assertEqual(l.get(4), 4)
        l.remove_last_occurrence(4)
        self.assertEqual(l.get_length(), 4)
        self.assertEqual(l.get(0), 1)
        self.assertEqual(l.get(1), 5)
        self.assertEqual(l.get(2), 3)
        self.assertEqual(l.get(3), 4)

    def test_sort_empty_list(self):
        l = AltList()
        l.sort()
        self.assertEqual(l.get_length(), 0)

    def test_sort_single_element_list(self):
        l = AltList([1])
        l.sort()
        self.assertEqual(l.get_length(), 1)
        self.assertEqual(l.get(0), 1)

    def test_sort(self):
        l = AltList([5, 1, 3, 4, 3, 4])
        l.sort()
        self.assertEqual(l.get_length(), 6)
        self.assertEqual(l.get(0), 1)
        self.assertEqual(l.get(1), 3)
        self.assertEqual(l.get(2), 3)
        self.assertEqual(l.get(3), 4)
        self.assertEqual(l.get(4), 4)
        self.assertEqual(l.get(5), 5)
