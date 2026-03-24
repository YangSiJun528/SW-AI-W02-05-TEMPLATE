# 문제: BFS - A → B (백준 실버2)
# 링크: https://www.acmicpc.net/problem/16953
# AI 사용 횟수:
# AI 사용 방법:
# 목표 시간: 30분
# 실제 시간: 14분 41초

# 1. 초기 접근
# 저번에 풀었던 동전 문제랑 비슷함
# bfs의 특성을 사용하면,
# 연산을 처리한 결과가 특정 값 N일때, N를 방문 처리한다.
# 가장 먼저 도달한 상태가 연산 수가 가장 적으면서 N에 도달한 방법이 되기 때문.
# 이러면 1씩 더한 4랑 / 1더한 2에서 2를 곱한것 중 후자가 3으로 최소값이 된다.

# 2. 풀이 전략

# 3. 막힌 점 / 실수
# 유형: [접근법] [구현] [엣지케이스] [최적화]

# 4. 최종 코드
import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())

queue = deque([(a,1)])
visited = {a}

rs = -1
while queue:
    n, cnt = queue.popleft()
    #print(n, cnt)
    if n == b:
        rs = cnt
        break
    if n*2 <= b:
        queue.append((n*2, cnt+1))
        visited.add(n*2)
    if int(str(n)+'1') <= b:
        queue.append((int(str(n)+'1'), cnt+1))
        visited.add(int(str(n)+'1'))

print(rs)