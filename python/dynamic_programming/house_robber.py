def house_robber(houses):
    if len(houses) == 1:
        return houses[0]

    cache = [None] * len(houses)
    one = _house_robber(houses, 0, len(houses)-2, cache)
    cache = [None] * len(houses)
    two = _house_robber(houses, 1, len(houses)-1, cache)
    return max(one, two)

def _house_robber(houses, start, end, cache):
    if end == start:
        return houses[start]
    if end == start + 1:
        return max(houses[start], houses[start + 1])

    if not cache[end]:
        one = _house_robber(houses, start, end-1, cache)
        two = _house_robber(houses, start, end-2, cache) + houses[end]
        cache[end] = max(one, two)
    return cache[end]







li1 = [2,3]
li2 = [10,3,2,4,7,9,10,15,2,3]

print(house_robber(li1))