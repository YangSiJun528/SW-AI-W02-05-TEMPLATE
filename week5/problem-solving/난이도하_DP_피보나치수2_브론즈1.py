# 문제: DP - 피보나치 수 2 (백준 브론즈 1)
# 링크: https://www.acmicpc.net/problem/2748
# AI 사용 횟수:
# AI 사용 방법:
# 목표 시간: 15분
# 실제 시간: 6분 39초

# 1. 초기 접근
# 그냥 피보나치 푸는건데?
# 아마 지문 보면 바텀업으로 풀길 원하는 듯?

# 2. 풀이 전략
#

# 3. 막힌 점 / 실수
# 유형: [접근법] [구현] [엣지케이스] [최적화]
# [구현] 조기 종료 조건 n <= 2으로 실수, 아니였으면 더 빨리 풀었을 듯?

# 4. 최종 코드
import sys

n = int(sys.stdin.readline().strip())

if n <= 1:
    print(n)
else:
    arr = [0] * (n+1)
    arr[0] = 0
    arr[1] = 1
    arr[2] = 1
    for i in range(3, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    print(arr[n])
