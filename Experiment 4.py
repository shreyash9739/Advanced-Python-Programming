def fibonacci_tabulation(n):
    if n < 0:
        raise ValueError("Number must be non-negative")

    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def fibonacci_memoization(n, memo=None):
    if n < 0:
        raise ValueError("Number must be non-negative")

    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = (
        fibonacci_memoization(n - 1, memo)
        + fibonacci_memoization(n - 2, memo)
    )

    return memo[n]
