# we are initializing 100 indexes as None
memo = [None] * 100

counter = 0


def fib(n):
    global counter
    counter += 1
    # if a number is already present in a list, we retrieve it instead of calculating fib of that number
    if memo[n] is not None:
        return memo[n]

    if n == 0 or n == 1:
        return n

    # store the result of recursive fibonacci summation to the list
    memo[n] = fib(n-1) + fib(n-2)

    return memo[n]


print(fib(13))
print('\ncounter:', counter)


# in memoization, if a number is already present in a list, we retrieve it instead of
# calculating whatever that number is
