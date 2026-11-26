
import random
import unittest

from Assignment2_AS26.Assignment2_ClosestPair import closest_pair_372, closest_pair_brute_372


class TestClosestPair_372(unittest.TestCase):

    # Compare both algorithms
    def check_both_372(self_372, points_372):

        brute_result_372 = closest_pair_brute_372(points_372)
        divide_result_372 = closest_pair_372(points_372)

        self_372.assertAlmostEqual(
            brute_result_372[0],
            divide_result_372[0]
        )

        self_372.assertEqual(
            brute_result_372[1:],
            divide_result_372[1:]
        )

    # Test 1: Exactly two points
    def test_two_points_372(self_372):

        points_372 = [(0, 0), (3, 4)]

        result_372 = closest_pair_372(points_372)

        self_372.assertEqual(result_372, (5.0, 0, 1))

        self_372.check_both_372(points_372)

    # Test 2: Duplicate points
    def test_duplicate_points_372(self_372):

        points_372 = [(1, 2), (5, 6), (1, 2)]

        result_372 = closest_pair_372(points_372)

        self_372.assertEqual(result_372, (0.0, 0, 2))

        self_372.check_both_372(points_372)

    # Test 3: All points on one vertical line
    def test_vertical_line_372(self_372):

        points_372 = [
            (5, 1),
            (5, 8),
            (5, 3),
            (5, 10),
            (5, 4)
        ]

        self_372.check_both_372(points_372)

        result_372 = closest_pair_372(points_372)

        self_372.assertEqual(result_372, (1.0, 2, 4))

    # Test 4: Closest pair across the dividing line
    def test_opposite_sides_372(self_372):

        points_372 = [
            (0, 0),
            (10, 10),
            (4, 4),
            (5, 5)
        ]

        self_372.check_both_372(points_372)

        result_372 = closest_pair_372(points_372)

        self_372.assertAlmostEqual(
            result_372[0],
            2 ** 0.5
        )

        self_372.assertEqual(result_372[1:], (2, 3))

    # Test 5: At least 500 random inputs
    def test_500_random_inputs_372(self_372):

        random_generator_372 = random.Random(42)

        for __372 in range(500):

            number_of_points_372 = random_generator_372.randint(2, 50)

            points_372 = [
                (
                    random_generator_372.randint(0, 1000),
                    random_generator_372.randint(0, 1000)
                )
                for __372 in range(number_of_points_372)
            ]

            with self_372.subTest(points_372=points_372):
                self_372.check_both_372(points_372)

    # Test 6: Invalid input
    def test_invalid_input_372(self_372):

        with self_372.assertRaises(ValueError):
            closest_pair_372([])

        with self_372.assertRaises(ValueError):
            closest_pair_brute_372([(1, 2)])


if __name__ == "__main__":

    unittest.main(verbosity=2)
