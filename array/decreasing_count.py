def decreasing_rating_count(ratings):
    left = 0
    right = 0
    result = 0
    while right < len(ratings):
        if right > 0 and ratings[right] - ratings[right - 1] == -1:
            result += (right - left) + 1
            right += 1
        elif right > 0 and ratings[right] - ratings[right - 1] == 0:
            left = right
            right += 1
        else:
            result += 1
            left = right
            right += 1
    return result

ratings = [4, 3, 5, 4, 3]


print(decreasing_rating_count(ratings))
print(decreasing_rating_count([4,3,2,1]))