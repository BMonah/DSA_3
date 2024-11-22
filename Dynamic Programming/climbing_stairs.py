'''
You are given an integer n representing the number of steps to reach the top of a staircase.
You can climb with either 1 or 2 steps at a time.
Return the number of distinct ways to climb to the top of the staircase.
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [None] * 32

        def fib(n):
            if memo[n] is not None:
                return memo[n]

            if n == 0 or n == 1:
                return n

            memo[n] = fib(n-1) + fib(n-2)
            return memo[n]
        return fib(n+1)


print(Solution().climbStairs(30))


def climbingStairs(n):
    memo = [None] * 100

    def fibo(n):
        # if the fib of a number is already been calculated,
        # we will return the number and not do the recursive calculations
        if memo[n] != None:
            return memo[n]

        if n == 0 or n == 1:
            return n
        memo[n] = fibo(n-1) + fibo(n-2)

        # now we return the value of n to return the result
        return memo[n]
    return fibo(n+1)


print(climbingStairs(5))
