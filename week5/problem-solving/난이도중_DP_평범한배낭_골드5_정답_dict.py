import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

# dp[i][weight] = 앞의 i개 물건만 사용해서 정확히 weight를 만들었을 때 최대 가치
dp = [dict() for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    w, v = items[i - 1]

    # 1) 안 고르는 경우: 이전 상태 복사
    for weight, value in dp[i - 1].items():
        if weight not in dp[i] or dp[i][weight] < value:
            dp[i][weight] = value

    # 2) 고르는 경우: 이전 상태에서 확장
    for weight, value in dp[i - 1].items():
        new_weight = weight + w
        new_value = value + v

        if new_weight <= K:
            if new_weight not in dp[i] or dp[i][new_weight] < new_value:
                dp[i][new_weight] = new_value

print(max(dp[N].values()))