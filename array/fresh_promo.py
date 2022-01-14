secret_code_list = [['apple', 'apple'], ['banana', 'anything', 'banana']]


def meets_promo(secret_code_list, shopping_cart):
    shopping_cart_idx = 0

    for i, code in enumerate(secret_code_list):
        code_idx = 0
        while shopping_cart_idx < len(shopping_cart) and code_idx < len(code):
            if code[code_idx] == shopping_cart[shopping_cart_idx]:
                code_idx += 1
                shopping_cart_idx += 1
            elif code[code_idx] == "anything":
                code_idx += 1
                shopping_cart_idx += 1
            else:
                code_idx = 0
                shopping_cart_idx += 1
        if shopping_cart_idx >= len(shopping_cart) and (i < len(secret_code_list) - 1 or code_idx < len(code)):
            return False
    return True


print(meets_promo(secret_code_list,
                  ['orange', 'apple', 'apple', 'orange', 'orange', 'banana', 'orange', 'apple', 'banana', 'banana',
                   'apple']))
print(meets_promo(secret_code_list, ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']))
print(meets_promo(secret_code_list, ['apple', 'apple', 'orange', 'orange', 'banana', 'apple', 'banana', 'banana']))
print(meets_promo(secret_code_list, ['banana', 'orange', 'banana', 'apple', 'apple']))
print(meets_promo(secret_code_list, ['apple', 'banana', 'apple', 'banana', 'orange', 'banana']))
print(meets_promo(secret_code_list, ['apple', 'apple', 'apple', 'banana']))
