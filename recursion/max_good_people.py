def does_contradict(subset, statements):
    for idx, num in enumerate(subset):
        if num == 0:
            continue
        for col_idx in range(len(statements[0])):
            if idx == col_idx:
                continue
            if statements[idx][col_idx] != 2 and statements[idx][col_idx] != subset[col_idx]:
                return True
    return False


def max_good_people(statements):
    n = len(statements)
    result = _get_subsets_helper(n, 0, [], statements, 0)
    return result


def _get_subsets_helper(n, idx, ds, statements, cur_sum):
    if idx == n:
        if not does_contradict(ds, statements):
            return cur_sum
        return 0
    ds.append(0)
    one = _get_subsets_helper(n, idx + 1, ds, statements, cur_sum)
    ds.pop()
    ds.append(1)
    two = _get_subsets_helper(n, idx + 1, ds, statements, cur_sum + 1)
    ds.pop()
    return max(one, two)


statements = [
    [2, 1, 2],
    [1, 2, 2],
    [2, 0, 2],
]

statements2 = [
    [2, 0],
    [0, 2]
]

print(max_good_people(statements))
print(max_good_people(statements2))
