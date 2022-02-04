from typing import List
from math import ceil

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    S.sort()
    S.append(N + 2)
    result = 0
    start = 0
    for occupied_seat in S:
        left_most_occupied_seat = occupied_seat - K
        open_seats = left_most_occupied_seat - start - 1
        if open_seats > 0:
            seats_can_be_occupied = ceil(open_seats / (2 * K))
            result += seats_can_be_occupied
        start = occupied_seat + K
    return result
N = 10
K = 1
M = 2
S = [2, 6]

print(getMaxAdditionalDinersCount(N, K, M, S))


N = 15
K = 2
M = 3
S = [11, 6, 14]

print(getMaxAdditionalDinersCount(N, K, M, S))