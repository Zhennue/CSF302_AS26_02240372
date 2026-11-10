
import math


# ------------------------------------------------
# 1. BRUTE FORCE APPROACH
# ------------------------------------------------

def closest_pair_brute(points):

    n = len(points)

    if n < 2:
        raise ValueError("At least 2 points are required")

    best_distance = float("inf")
    best_i = -1
    best_j = -1

    # Compare every point with every other point
    for i in range(n):

        for j in range(i + 1, n):

            x1, y1 = points[i]
            x2, y2 = points[j]

            # Calculate squared distance
            distance = (x1 - x2) ** 2 + (y1 - y2) ** 2

            if (distance, i, j) < (best_distance, best_i, best_j):
                best_distance = distance
                best_i = i
                best_j = j

    return (math.sqrt(best_distance), best_i, best_j)


# ------------------------------------------------
# 2. DIVIDE AND CONQUER APPROACH
# ------------------------------------------------

def closest_pair(points):

    n = len(points)

    if n < 2:
        raise ValueError("At least 2 points are required")

    # Store each point together with its original index
    points_list = [
        (point[0], point[1], i)
        for i, point in enumerate(points)
    ]

    # Handle duplicate points first
    seen = {}

    duplicate_pair = None

    for x, y, index in points_list:

        if (x, y) in seen:

            pair = (seen[(x, y)], index)

            if duplicate_pair is None or pair < duplicate_pair:
                duplicate_pair = pair

        else:
            seen[(x, y)] = index

    # Duplicate points have distance zero
    if duplicate_pair is not None:
        return (0.0, duplicate_pair[0], duplicate_pair[1])

    # Sort points by x-coordinate
    points_x = sorted(
        points_list,
        key=lambda p: (p[0], p[1], p[2])
    )

    # Sort points by y-coordinate
    points_y = sorted(
        points_list,
        key=lambda p: (p[1], p[0], p[2])
    )

    # Compare two points using squared distance
    def get_distance(p1, p2):

        return (
            (p1[0] - p2[0]) ** 2
            + (p1[1] - p2[1]) ** 2
        )

    # Brute force for small groups
    def brute_small(group):

        best = (float("inf"), -1, -1)

        for i in range(len(group)):

            for j in range(i + 1, len(group)):

                p1 = group[i]
                p2 = group[j]

                a, b = sorted((p1[2], p2[2]))

                candidate = (
                    get_distance(p1, p2),
                    a,
                    b
                )

                if candidate < best:
                    best = candidate

        return best

    # Recursive divide and conquer function
    def solve(px, py):

        n = len(px)

        # Base case: solve small groups directly
        if n <= 3:
            return brute_small(px)

        # Divide the points into two halves
        middle = n // 2

        left_x = px[:middle]
        right_x = px[middle:]

        middle_x = right_x[0][0]

        # Separate points according to their original indices
        left_indices = {p[2] for p in left_x}

        left_y = []
        right_y = []

        for p in py:

            if p[2] in left_indices:
                left_y.append(p)
            else:
                right_y.append(p)

        # Solve the left and right sides
        left_result = solve(left_x, left_y)
        right_result = solve(right_x, right_y)

        # Select the better result
        best = min(left_result, right_result)

        best_distance = best[0]

        # Create the middle strip
        strip = []

        for p in py:

            if (p[0] - middle_x) ** 2 <= best_distance:
                strip.append(p)

        # Check nearby points in the strip
        for i in range(len(strip)):

            for j in range(i + 1, min(i + 8, len(strip))):

                # Strip is sorted by y-coordinate
                dy = strip[j][1] - strip[i][1]

                if dy * dy > best_distance:
                    break

                p1 = strip[i]
                p2 = strip[j]

                a, b = sorted((p1[2], p2[2]))

                candidate = (
                    get_distance(p1, p2),
                    a,
                    b
                )

                if candidate < best:
                    best = candidate
                    best_distance = best[0]

        return best

    # Run the recursive algorithm
    result = solve(points_x, points_y)

    return (math.sqrt(result[0]), result[1], result[2])


# ------------------------------------------------
# 3. SIMPLE EXAMPLE
# ------------------------------------------------

if __name__ == "__main__":

    points = [
        (2, 3),
        (12, 30),
        (40, 50),
        (5, 1),
        (12, 10),
        (3, 4)
    ]

    print("Brute Force Result:")
    print(closest_pair_brute(points))

    print("\nDivide and Conquer Result:")
    print(closest_pair(points))
