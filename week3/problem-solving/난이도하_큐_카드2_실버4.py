# 문제: 큐 - 카드2 (백준 실버4)
# 링크: https://www.acmicpc.net/problem/2164
# AI 사용 횟수:
# AI 사용 방법:
# 목표 시간: 30분
# 실제 시간: 5분 37초

# 1. 초기 접근
# 선입선출로 처리하면 됨. 하나 버리도 하나 뒤에 넣는걸 반복하면 됨.
# deque 사용 필요

# 2. 풀이 전략
# 그대로 사용

# 3. 막힌 점 / 실수
# 종료 조건에 대한 고민 없이 접근했음. 쉬운 문제가 상관없었지만, 이런 습관은 버리는게 좋은데...

# 4. 최종 코드
import sys
from collections import deque

num = int(sys.stdin.readline().strip())

q = deque(list(range(1, num + 1)))
cnt = 0

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())
    cnt += 1

print(q.popleft())