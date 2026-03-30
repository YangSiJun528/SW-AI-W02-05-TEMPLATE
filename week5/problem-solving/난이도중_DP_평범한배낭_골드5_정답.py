# 1차원 dp로 푸는 것도 있는데, 이해하기 어려워서 일단 2차원 먼저 이해하기...

import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # N이 물건 개수, K가 무게 제한, dp[N][K]로 구함.
items = [(0, 0)]  # 1번 인덱스부터 쓰기 위해 더미 추가
# dp[i][j] = 앞의 i개 물건만 봤을 때, 무게 제한이 j인 배낭에 넣을 수 있는 최대 가치

for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))

dp = [[0] * (K + 1) for _ in range(N + 1)] # 최대 가치니까 0을 기본값으로...

for i in range(1, N + 1):
    w, v = items[i]
    for j in range(1, K + 1):
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[N][K])
