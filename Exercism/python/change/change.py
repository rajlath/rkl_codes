def find_minimum_coins(total_change, coins):
    if total_change < min(coins) and total_change > 0:
        raise ValueError("Invalid change")
    if total_change == 0:
        return []
    maybe = {c:[c] for c in coins}
    while total_change not in maybe:
        new_change = {}
        for m in maybe:
            for c in coins:
                if m + c  in maybe:continue
                new_change[m + c] = maybe[m] + [c]
        if not any(m < total_change for m in new_change)    :
            raise ValueError("Invalid Change")
        maybe.update(new_change)
    return list(sorted(maybe[total_change]))


print(find_minimum_coins(999, [1, 2, 5, 10, 20, 50, 100]))

