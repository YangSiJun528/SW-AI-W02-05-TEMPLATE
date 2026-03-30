# 문제: DP - 동전 2 (백준 골드5)
# 링크: https://www.acmicpc.net/problem/2294
# AI 사용 횟수:
# AI 사용 방법:
# 목표 시간:
# 실제 시간:

# 1. 초기 접근
# 이전에 BFS로 풀었던 문제긴 한데, 풀만한듯?
# 최소갑 구하는 문제
# dp[i]는 dp[i-c] + 1을 하면 됨.
# 아 그냥 동전 문제랑 이거랑 햇갈렸던건가...?
# 근데 둘이 같은 난이도인게 말이 안되지 않나?
# 일단 최소 경우를 말하니까 OK

# 2. 풀이 전략
# dp[i]는 최소로 코인을 사용 가능한 개수
# dp[i] = dp[i-c] + 1 중 가장 작은 값을 할당...
# 이거는 c들이 전체 결과에 문제를 안주므로 i -> coin 중첩 반복문 구조가 가능? -> 아닌가?

# 3. 막힌 점 / 실수
# 유형: [접근법] [구현] [엣지케이스] [최적화]
#

# 4. 최종 코드
import sys

input = sys.stdin.readline

cnt_input, target = map(int, input().split())
coins = [int(input().strip()) for _ in range(cnt_input)]

dp = [10**6+1] * (target+1)

for c in coins:
    if target - c >= 0:
        dp[c] = 1

for i in range(1, target+1):
    for c in coins:
        if i-c > 0:
            dp[i] = min(dp[i], dp[i-c] + 1)

if dp[target] == 10**6+1:
    print(-1)
else:
    print(dp[target])