from bisect import bisect_right


def greedy_earliest_finish_372(requests_372):
    """Choose compatible requests in earliest-finish order."""
    ordered_372 = sorted(
        enumerate(requests_372),
        key=lambda item_372: (item_372[1][1], item_372[1][0], item_372[0])
    )
    chosen_372 = []
    last_finish_372 = float("-inf")

    for index_372, request_372 in ordered_372:
        start_372, finish_372, fee_372 = request_372
        if start_372 >= last_finish_372:
            chosen_372.append((index_372, fee_372))
            last_finish_372 = finish_372

    return sum(fee_372 for index_372, fee_372 in chosen_372), [
        index_372 for index_372, fee_372 in chosen_372
    ]


def greedy_highest_fee_372(requests_372):
    """Accept the highest-fee request next when it fits the current schedule."""
    ordered_372 = sorted(
        enumerate(requests_372),
        key=lambda item_372: (-item_372[1][2], item_372[1][1],
                              item_372[1][0], item_372[0])
    )
    chosen_372 = []

    for index_372, request_372 in ordered_372:
        start_372, finish_372, fee_372 = request_372
        fits_372 = all(
            finish_372 <= other_start_372 or other_finish_372 <= start_372
            for other_index_372, (other_start_372, other_finish_372, other_fee_372)
            in chosen_372
        )
        if fits_372:
            chosen_372.append((index_372, request_372))

    chosen_372.sort(key=lambda item_372: (
        item_372[1][0], item_372[1][1], item_372[0]
    ))
    return sum(request_372[2] for index_372, request_372 in chosen_372), [
        index_372 for index_372, request_372 in chosen_372
    ]


def best_schedule_372(requests_372):
    """Find a maximum-fee compatible schedule with weighted interval DP."""
    ordered_372 = sorted(
        enumerate(requests_372),
        key=lambda item_372: (item_372[1][1], item_372[1][0], item_372[0])
    )
    finishes_372 = [request_372[1][1] for request_372 in ordered_372]
    best_fees_372 = [0] * (len(ordered_372) + 1)
    take_372 = [False] * len(ordered_372)
    previous_372 = [0] * len(ordered_372)

    for position_372, (index_372, request_372) in enumerate(ordered_372):
        start_372, finish_372, fee_372 = request_372
        previous_position_372 = bisect_right(
            finishes_372, start_372, 0, position_372
        )
        previous_372[position_372] = previous_position_372
        take_fee_372 = fee_372 + best_fees_372[previous_position_372]
        skip_fee_372 = best_fees_372[position_372]

        if take_fee_372 > skip_fee_372:
            best_fees_372[position_372 + 1] = take_fee_372
            take_372[position_372] = True
        else:
            best_fees_372[position_372 + 1] = skip_fee_372

    chosen_372 = []
    position_372 = len(ordered_372)
    while position_372 > 0:
        request_position_372 = position_372 - 1
        if take_372[request_position_372]:
            chosen_372.append(ordered_372[request_position_372][0])
            position_372 = previous_372[request_position_372]
        else:
            position_372 -= 1

    chosen_372.reverse()
    return best_fees_372[-1], chosen_372


def brute_force_372(requests_372):
    """Check all subsets; intended only for small test inputs (n <= 15)."""
    if len(requests_372) > 15:
        raise ValueError("brute_force_372 supports at most 15 requests")

    best_fee_372 = 0
    best_chosen_372 = []
    request_count_372 = len(requests_372)

    for mask_372 in range(1 << request_count_372):
        chosen_372 = [index_372 for index_372 in range(request_count_372)
                      if mask_372 & (1 << index_372)]
        ordered_372 = sorted(
            chosen_372,
            key=lambda index_372: (requests_372[index_372][0],
                                   requests_372[index_372][1], index_372)
        )
        compatible_372 = all(
            requests_372[ordered_372[position_372 - 1]][1]
            <= requests_372[ordered_372[position_372]][0]
            for position_372 in range(1, len(ordered_372))
        )
        if compatible_372:
            fee_372 = sum(requests_372[index_372][2] for index_372 in chosen_372)
            if fee_372 > best_fee_372:
                best_fee_372 = fee_372
                best_chosen_372 = ordered_372

    return best_fee_372, best_chosen_372


if __name__ == "__main__":
    requests_372 = [
        (9, 12, 3000), (10, 16, 8000), (13, 17, 4000),
        (12, 14, 2500), (16, 18, 2000)
    ]
    print("Requests:", requests_372)
    print("Earliest finish:", greedy_earliest_finish_372(requests_372))
    print("Highest fee:", greedy_highest_fee_372(requests_372))
    print("Dynamic programming:", best_schedule_372(requests_372))
