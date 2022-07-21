big_string = "cbabcacabca"
small_string = "abc"

from collections import defaultdict


def find_perm_in_big_string(big_string, small_string):
    small_string_len = len(small_string)
    result = []
    small_map = defaultdict(int)
    for let in small_string:
        small_map[let] += 1

    big_map = defaultdict(int)
    counter = 0

    for idx in range(len(big_string) + 1):
        if counter == small_string_len:
            result.append(big_string[idx - small_string_len: idx])
        if idx == len(big_string):
            break
        let = big_string[idx]
        if idx >= small_string_len:
            to_be_removed_idx = idx - small_string_len
            to_be_removed_let = big_string[to_be_removed_idx]
            if to_be_removed_let in small_map:
                if big_map[to_be_removed_let] > 0:
                    if big_map[to_be_removed_let] <= small_map[to_be_removed_let]:
                        counter -= 1
                    big_map[to_be_removed_let] = big_map[to_be_removed_let] - 1
        if let in small_map:
            small_map_let_count = small_map[let]
            if big_map[let] < small_map_let_count:
                big_map[let] += 1
                counter += 1
            else:
                big_map[let] += 1
        else:
            big_map = defaultdict(int)
            counter = 0
    return result


print(find_perm_in_big_string(big_string, small_string))
