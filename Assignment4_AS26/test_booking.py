import random
import unittest

from booking import (
    best_schedule_372,
    brute_force_372,
    greedy_earliest_finish_372,
    greedy_highest_fee_372,
)


class TestBooking_372(unittest.TestCase):
    def check_optimal_372(self, requests_372):
        dynamic_result_372 = best_schedule_372(requests_372)
        brute_result_372 = brute_force_372(requests_372)
        self.assertEqual(dynamic_result_372[0], brute_result_372[0])
        self.assert_compatible_372(requests_372, dynamic_result_372[1])

    def assert_compatible_372(self, requests_372, chosen_372):
        ordered_372 = sorted(chosen_372,
                             key=lambda index_372: requests_372[index_372][0])
        for position_372 in range(1, len(ordered_372)):
            previous_372 = requests_372[ordered_372[position_372 - 1]]
            current_372 = requests_372[ordered_372[position_372]]
            self.assertLessEqual(previous_372[1], current_372[0])

    def check_greedy_result_372(self, requests_372, result_372):
        self.assert_compatible_372(requests_372, result_372[1])
        self.assertEqual(
            result_372[0],
            sum(requests_372[index_372][2] for index_372 in result_372[1])
        )

    def test_no_requests_372(self):
        self.assertEqual(best_schedule_372([]), (0, []))
        self.assertEqual(greedy_earliest_finish_372([]), (0, []))
        self.assertEqual(greedy_highest_fee_372([]), (0, []))

    def test_one_request_372(self):
        self.check_optimal_372([(2, 5, 700)])
        self.assertEqual(best_schedule_372([(2, 5, 700)]), (700, [0]))

    def test_all_overlapping_372(self):
        requests_372 = [(0, 5, 10), (1, 6, 30), (2, 7, 20)]
        self.check_optimal_372(requests_372)
        self.assertEqual(best_schedule_372(requests_372)[0], 30)

    def test_none_overlapping_372(self):
        requests_372 = [(0, 2, 4), (3, 5, 7), (6, 8, 9)]
        self.check_optimal_372(requests_372)
        self.assertEqual(best_schedule_372(requests_372)[0], 20)

    def test_back_to_back_requests_372(self):
        requests_372 = [(9, 12, 3000), (12, 14, 2500), (14, 16, 1800)]
        self.check_optimal_372(requests_372)
        self.assertEqual(best_schedule_372(requests_372), (7300, [0, 1, 2]))

    def test_example_372(self):
        requests_372 = [
            (9, 12, 3000), (10, 16, 8000), (13, 17, 4000),
            (12, 14, 2500), (16, 18, 2000)
        ]
        self.assertEqual(greedy_earliest_finish_372(requests_372),
                         (7500, [0, 3, 4]))
        self.assertEqual(greedy_highest_fee_372(requests_372), (10000, [1, 4]))
        self.assertEqual(best_schedule_372(requests_372), (10000, [1, 4]))
        self.check_optimal_372(requests_372)

    def test_greedy_counterexamples_372(self):
        earliest_requests_372 = [(0, 4, 12), (0, 2, 5), (2, 4, 5)]
        highest_fee_requests_372 = [(0, 3, 10), (0, 1, 6), (1, 3, 6)]
        earliest_result_372 = greedy_earliest_finish_372(earliest_requests_372)
        highest_fee_result_372 = greedy_highest_fee_372(highest_fee_requests_372)
        self.assertEqual(earliest_result_372[0], 10)
        self.assertEqual(highest_fee_result_372[0], 10)
        self.check_greedy_result_372(earliest_requests_372, earliest_result_372)
        self.check_greedy_result_372(highest_fee_requests_372, highest_fee_result_372)

    def test_500_random_inputs_372(self):
        random_generator_372 = random.Random(372)
        for case_372 in range(500):
            requests_372 = []
            for _372 in range(random_generator_372.randint(0, 10)):
                start_372 = random_generator_372.randint(0, 30)
                finish_372 = random_generator_372.randint(start_372 + 1,
                                                           start_372 + 12)
                fee_372 = random_generator_372.randint(1, 10000)
                requests_372.append((start_372, finish_372, fee_372))
            with self.subTest(case_372=case_372):
                self.check_optimal_372(requests_372)

    def test_equal_fees_earliest_finish_is_optimal_372(self):
        random_generator_372 = random.Random(4372)
        for case_372 in range(200):
            requests_372 = []
            for _372 in range(random_generator_372.randint(0, 10)):
                start_372 = random_generator_372.randint(0, 25)
                finish_372 = random_generator_372.randint(start_372 + 1,
                                                           start_372 + 10)
                requests_372.append((start_372, finish_372, 100))
            with self.subTest(case_372=case_372):
                self.assertEqual(
                    greedy_earliest_finish_372(requests_372)[0],
                    best_schedule_372(requests_372)[0]
                )

    def test_brute_force_size_limit_372(self):
        with self.assertRaises(ValueError):
            brute_force_372([(index_372, index_372 + 1, 1)
                             for index_372 in range(16)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
