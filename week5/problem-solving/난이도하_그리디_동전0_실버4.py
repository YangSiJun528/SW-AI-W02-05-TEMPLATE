# 문제: 그리디 - 동전 0 (백준 실버4)
# 링크: https://www.acmicpc.net/problem/11047
# AI 사용 횟수:
# AI 사용 방법:
# 목표 시간: 15분
# 실제 시간: 6분 4초

# 1. 초기 접근
# 이거는 유명한 유형이라 본 영상에서도 나왔음.
# 큰 동전부터 계산 가능. 왜냐면 배수인 경우를 문제에서 보장하므로.
#

# 2. 풀이 전략
#

# 3. 막힌 점 / 실수
# 유형: [접근법] [구현] [엣지케이스] [최적화]
#

# 4. 최종 코드
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input().strip()) for _ in range(n)]

coins = coins[::-1]

#print(coins)

cnt = 0

for coin in coins:
    n = k // coin
    k = k % coin
    cnt += n

print(cnt)

