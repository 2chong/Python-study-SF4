'''
https://school.programmers.co.kr/learn/courses/30/lessons/12902

DP 쓰는 문제.
난 항상 DP를 못하겠음 감이 아예 안잡힘
아니 이 점화식을 어케 만드는거지 진자
겨우 이해했네
'''

def solution(n):
    MOD = 1_000_000_007

    if n % 2 == 1:
        return 0

    dp = [0] * (n + 1)
    dp[0] = 1
    if n >= 2:
        dp[2] = 3

    prefix = dp[0] 

    for k in range(4, n + 1, 2):
        dp[k] = (3 * dp[k - 2] + 2 * prefix) % MOD
        prefix = (prefix + dp[k - 2]) % MOD

    return dp[n]
