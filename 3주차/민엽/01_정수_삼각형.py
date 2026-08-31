def solution(triangle):
    n = len(triangle)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i-1][j]
            elif i == j:
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j]+triangle[i][j],
                               dp[i-1][j-1]+triangle[i][j])
    # print(dp[n-1])
    
    return max(dp[n-1])
