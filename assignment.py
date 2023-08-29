'''## Question

In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.
 
Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal

Test cases:

for 5 days: 14/29
for 10 days: 372/773'''
def one_d_approach(n,m):
        dp = [1] * (m + 1)
        dp[m] = 0
        
        for i in range(1, n + 1):
            missing = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                missing[j] = dp[0] + dp[j + 1]
            missing, dp = dp, missing

        ways = dp[0]  # total number of way to attend classes
        misses_ways = missing[1]  # total number of way to miss last day
        
        return f"for {n} days: {misses_ways}/{ways}"

def two_d_approach(n,m):
        dp=[[0 for i in range(m+1)]for i in range(n+1)]

        for i in range(m):
            dp[0][i] = 1

        for i in range(1, n + 1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i - 1][0] + dp[i - 1][j + 1]

        ways = dp[n][0]  # total number of way to attend classes
        misses_ways = dp[n - 1][1]  # total number of way to miss last day
        
        return f"for {n} days: {misses_ways}/{ways}"

if __name__ == "__main__":
    days = [(5, 4), (10, 4)]
    for n, m in days: # m is number of leaves, n is Nth day
        if n < m or n < 0 or m < 0: # edge cases 
             print("Invalid Inputs")
             break
        print(one_d_approach(n,m))
        print(two_d_approach(n,m)) 