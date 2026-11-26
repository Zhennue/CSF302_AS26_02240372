
import math


# ------------------------------------------------
# 1. BRUTE FORCE APPROACH
# ------------------------------------------------

def closest_pair_brute_372(points_372, time_limit_372=None):

    n_372 = len(points_372)

    if n_372 < 2:
        raise ValueError("At least 2 points are required")

    best_distance_372 = float("inf")
    best_i_372 = -1
    best_j_372 = -1
    start_time_372 = None

    if time_limit_372 is not None:
        import time
        start_time_372 = time.perf_counter()

    # Compare every point with every other point
    for i_372 in range(n_372):

        for j_372 in range(i_372 + 1, n_372):

            if (time_limit_372 is not None and j_372 % 256 == 0
                    and time.perf_counter() - start_time_372 >= time_limit_372):
                raise TimeoutError("Brute-force time limit reached")

            x1_372, y1_372 = points_372[i_372]
            x2_372, y2_372 = points_372[j_372]

            # Calculate squared distance
            distance_372 = (x1_372 - x2_372) ** 2 + (y1_372 - y2_372) ** 2

            if (distance_372, i_372, j_372) < (best_distance_372, best_i_372, best_j_372):
                best_distance_372 = distance_372
                best_i_372 = i_372
                best_j_372 = j_372

    return (math.sqrt(best_distance_372), best_i_372, best_j_372)


# ------------------------------------------------
# 2. DIVIDE AND CONQUER APPROACH
# ------------------------------------------------

def closest_pair_372(points_372):

    n_372 = len(points_372)

    if n_372 < 2:
        raise ValueError("At least 2 points are required")

    # Store each point together with its original index
    points_list_372 = [
        (point_372[0], point_372[1], i_372)
        for i_372, point_372 in enumerate(points_372)
    ]

    # Handle duplicate points first
    seen_372 = {}

    duplicate_pair_372 = None

    for x_372, y_372, index_372 in points_list_372:

        if (x_372, y_372) in seen_372:

            pair_372 = (seen_372[(x_372, y_372)], index_372)

            if duplicate_pair_372 is None or pair_372 < duplicate_pair_372:
                duplicate_pair_372 = pair_372

        else:
            seen_372[(x_372, y_372)] = index_372

    # Duplicate points have distance zero
    if duplicate_pair_372 is not None:
        return (0.0, duplicate_pair_372[0], duplicate_pair_372[1])

    # Sort points by x-coordinate
    points_x_372 = sorted(
        points_list_372,
        key=lambda p_372: (p_372[0], p_372[1], p_372[2])
    )

    # Sort points by y-coordinate
    points_y_372 = sorted(
        points_list_372,
        key=lambda p_372: (p_372[1], p_372[0], p_372[2])
    )

    # Compare two points using squared distance
    def get_distance_372(p1_372, p2_372):

        return (
            (p1_372[0] - p2_372[0]) ** 2
            + (p1_372[1] - p2_372[1]) ** 2
        )

    # Brute force for small groups
    def brute_small_372(group_372):

        best_372 = (float("inf"), -1, -1)

        for i_372 in range(len(group_372)):

            for j_372 in range(i_372 + 1, len(group_372)):

                p1_372 = group_372[i_372]
                p2_372 = group_372[j_372]

                a_372, b_372 = sorted((p1_372[2], p2_372[2]))

                candidate_372 = (
                    get_distance_372(p1_372, p2_372),
                    a_372,
                    b_372
                )

                if candidate_372 < best_372:
                    best_372 = candidate_372

        return best_372

    # Recursive divide and conquer function
    def solve_372(px_372, py_372):

        n_372 = len(px_372)

        # Base case: solve small groups directly
        if n_372 <= 3:
            return brute_small_372(px_372)

        # Divide the points into two halves
        middle_372 = n_372 // 2

        left_x_372 = px_372[:middle_372]
        right_x_372 = px_372[middle_372:]

        middle_x_372 = right_x_372[0][0]

        # Separate points according to their original indices
        left_indices_372 = {p_372[2] for p_372 in left_x_372}

        left_y_372 = []
        right_y_372 = []

        for p_372 in py_372:

            if p_372[2] in left_indices_372:
                left_y_372.append(p_372)
            else:
                right_y_372.append(p_372)

        # Solve the left and right sides
        left_result_372 = solve_372(left_x_372, left_y_372)
        right_result_372 = solve_372(right_x_372, right_y_372)

        # Select the better result
        best_372 = min(left_result_372, right_result_372)

        best_distance_372 = best_372[0]

        # Create the middle strip
        strip_372 = []

        for p_372 in py_372:

            if (p_372[0] - middle_x_372) ** 2 <= best_distance_372:
                strip_372.append(p_372)

        # Check nearby points in the strip
        for i_372 in range(len(strip_372)):

            for j_372 in range(i_372 + 1, min(i_372 + 8, len(strip_372))):

                # Strip is sorted by y-coordinate
                dy_372 = strip_372[j_372][1] - strip_372[i_372][1]

                if dy_372 * dy_372 > best_distance_372:
                    break

                p1_372 = strip_372[i_372]
                p2_372 = strip_372[j_372]

                a_372, b_372 = sorted((p1_372[2], p2_372[2]))

                candidate_372 = (
                    get_distance_372(p1_372, p2_372),
                    a_372,
                    b_372
                )

                if candidate_372 < best_372:
                    best_372 = candidate_372
                    best_distance_372 = best_372[0]

        return best_372

    # Run the recursive algorithm
    result_372 = solve_372(points_x_372, points_y_372)

    return (math.sqrt(result_372[0]), result_372[1], result_372[2])


# ------------------------------------------------
# 3. SIMPLE EXAMPLE
# ------------------------------------------------

if __name__ == "__main__":

    points_372 = [
        (2, 3),
        (12, 30),
        (40, 50),
        (5, 1),
        (12, 10),
        (3, 4)
    ]

    print("Brute Force Result:")
    print(closest_pair_brute_372(points_372))

    print("\nDivide and Conquer Result:")
    print(closest_pair_372(points_372))
