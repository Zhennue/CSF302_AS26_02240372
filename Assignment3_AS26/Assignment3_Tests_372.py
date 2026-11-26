import random
import unittest

from Assignment3_Sorts_372 import quicksort_basic_372, quicksort_improved_372


class TestQuicksort_372(unittest.TestCase):
    def check_sort_372(self, values_372):
        expected_372 = sorted(values_372)
        basic_result_372 = values_372.copy()
        improved_result_372 = values_372.copy()

        quicksort_basic_372(basic_result_372)
        quicksort_improved_372(improved_result_372, seed_372=372)

        self.assertEqual(basic_result_372, expected_372)
        self.assertEqual(improved_result_372, expected_372)

    def test_empty_list_372(self):
        self.check_sort_372([])

    def test_single_element_372(self):
        self.check_sort_372([7])

    def test_all_equal_372(self):
        self.check_sort_372([5] * 30)

    def test_already_sorted_372(self):
        self.check_sort_372(list(range(25)))

    def test_reverse_sorted_372(self):
        self.check_sort_372(list(range(24, -1, -1)))

    def test_negative_numbers_372(self):
        self.check_sort_372([0, -8, 4, -3, 2, -8])

    def test_500_random_lists_372(self):
        random_generator_372 = random.Random(372)
        for case_372 in range(500):
            size_372 = random_generator_372.randint(0, 100)
            values_372 = [
                random_generator_372.randint(-1000, 1000)
                for _372 in range(size_372)
            ]
            with self.subTest(case_372=case_372):
                self.check_sort_372(values_372)

    def test_improved_rejects_invalid_cutoff_372(self):
        with self.assertRaises(ValueError):
            quicksort_improved_372([1, 2], cutoff_372=0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
