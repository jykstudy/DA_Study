def solution(n):
    MOD = 1000000007
    
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 0
    dp[2] = 3
    
    for i in range(4, n + 1, 2):
        dp[i] = (dp[i - 2] * 4 - dp[i - 4]) % MOD
    
    return dp[n]