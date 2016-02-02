__author__ = 'yury'

# Credit card numbers can be validated with a process called the Luhn algorithm.
# Simply stated, the Luhn algorithm works like this:

#              1. If the length of the card number is even, pick all the digits with an even index.
#              If the length of the card number is odd, pick all the digits with an odd index.
#              2. Transform each digit like so: if 2*x > 9, then replace x with 2*x - 9;
#              othwerise, replace x with 2*x
#              3. Add up all the numbers.
#              4. If the result is divisable by 10 (withour remainder) then the card number was valid.
# Example:
# true == solution("4408041234567893")

def wrong_solution(card):  # https://github.com/hexlet-codebattle/battle_asserts/issues/314
    result = []
    if len(card) % 2:
        temp = [int(d) for i, d in enumerate(card) if i % 2]
    else:
        temp = [int(d) for i, d in enumerate(card) if not i % 2]
    print(temp)
    for d in temp:
        result += [(2 * d) - 9 if 2 * d > 9 else 2 * d, ]
    return sum(result) % 10 == 0
