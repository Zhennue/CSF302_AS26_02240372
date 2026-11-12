
import random
import unittest

from closest import closest_pair, closest_pair_brute


class TestClosestPair(unittest.TestCase):

    # Compare both algorithms
    def check_both(self, points):

        brute_result = closest_pair_brute(points)
        divide_result = closest_pair(points)

        self.assertAlmostEqual(
            brute_result[0],
            divide_result[0]
        )

        self.assertEqual(
            brute_result[1:],
            divide_result[1:]
        )

    # Test 1: Exactly two points
    def test_two_points(self):

        points = [(0, 0), (3, 4)]

        result = closest_pair(points)

        self.assertEqual(result, (5.0, 0, 1))

        self.check_both(points)

    # Test 2: Duplicate points
    def test_duplicate_points(self):

        points = [(1, 2), (5, 6), (1, 2)]

        result = closest_pair(points)

        self.assertEqual(result, (0.0, 0, 2))

        self.check_both(points)

    # Test 3: All points on one vertical line
    def test_vertical_line(self):

        points = [
            (5, 1),
            (5, 8),
            (5, 3),
            (5, 10),
            (5, 4)
        ]

        self.check_both(points)

        result = closest_pair(points)

        self.assertEqual(result, (1.0, 2, 4))

    # Test 4: Closest pair across the dividing line
    def test_opposite_sides(self):

        points = [
            (0, 0),
            (10, 10),
            (4, 4),
            (5, 5)
        ]

        self.check_both(points)

        result = closest_pair(points)

        self.assertAlmostEqual(
            result[0],
            2 ** 0.5
        )

        self.assertEqual(result[1:], (2, 3))

    # Test 5: At least 500 random inputs
    def test_500_random_inputs(self):

        random_generator = random.Random(42)

        for _ in range(500):

            number_of_points = random_generator.randint(2, 50)

            points = [
                (
                    random_generator.randint(0, 1000),
                    random_generator.randint(0, 1000)
                )
                for _ in range(number_of_points)
            ]

            with self.subTest(points=points):
                self.check_both(points)

    # Test 6: Invalid input
    def test_invalid_input(self):

        with self.assertRaises(ValueError):
            closest_pair([])

        with self.assertRaises(ValueError):
            closest_pair_brute([(1, 2)])


if __name__ == "__main__":

    unittest.main(verbosity=2)
