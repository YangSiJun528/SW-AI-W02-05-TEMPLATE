# 문제: 그리디 - 잃어버린 괄호 (백준 실버2)
# 링크: https://www.acmicpc.net/problem/1541
# AI 사용 횟수:
# AI 사용 방법:
# 목표 시간: 15분
# 실제 시간: 10분 46초

# 1. 초기 접근
# n(자릿수)이 50.
# 최소로 만들어야 함.
# -가 시작하고 다음 -가 나올때까지 계속 더하는걸로 묶으면
# 크게 묶을 수 있음.
# 이렇게 풀면 될 듯?

# 2. 풀이 전략
# input 처리가 좀 애매한데
# -를 기준으로 먼저 나누고
# 안의 각 수를 합한 후 빼기 연산을 수행하면 됨.
# 앞과 뒤는 항상 숫자이므로 엣지케이스는 없음.

# 3. 막힌 점 / 실수
# 유형: [접근법] [구현] [엣지케이스] [최적화]
#

# 4. 최종 코드
import sys

input = sys.stdin.readline

arr1 = input().split('-')

arr2 = []

for a1 in arr1:
    arr2.append(sum(list(map(int, a1.split('+')))))

rs = arr2[0]

for i in range(1, len(arr2)):
    rs -= arr2[i]

print(rs)