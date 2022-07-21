def print_name(num_times, name="Hello"):
    if num_times > 0:
        print(name)
        print_name(num_times - 1, name)

print_name(5)