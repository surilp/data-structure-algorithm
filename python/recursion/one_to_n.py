def print_one_to_n(num):
    if num > 0:
        print_one_to_n(num-1)
        print(num)

print_one_to_n(5)