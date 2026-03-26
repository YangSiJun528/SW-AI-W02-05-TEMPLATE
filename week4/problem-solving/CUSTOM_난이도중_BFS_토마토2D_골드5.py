# 문제: BFS - 토마토 (백준 골드5)
# 링크: https://www.acmicpc.net/problem/7576
# AI 사용 횟수:
# AI 사용 방법:
# 목표 시간: 30분
# 실제 시간: 27분 51초

# 1. 초기 접근
# 그냥 최단거리에 이동 횟수 보여주는 전형적인 bfs 문제
# 모든 경우에서 토마토가 하나 이상 있음. 벽 있음(-1).
# 방향은 상하좌우 4방향
# x,y 길이 다름.
# 시작 위치 고정 아님.
# 모든 값이 다 익었는지? 확인해야 함.

# 2. 풀이 전략
# 모두 익는 경우를 고려해야 함.
# 따라서 총 토마토의 개수와, 방문처리된(익은) 토마토의 개수를 매번 비교하고 증가시켜줘야 함.
# 또한 시작 위치가 고정되어 있지 않으므로 queue에 여러 값이 들어갈 수 있음.
# N도 2 이상이라 딱히 엣지케이스 없음

# 3. 막힌 점 / 실수
# 유형: [접근법] [구현] [엣지케이스] [최적화]
# 없음

# 4. 최종 코드
from collections import deque
import sys

input = sys.stdin.readline

len_x, len_y = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(len_y)]

queue = deque([])
fresh = 0
step = -1
vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for y in range(len_y):
    for x in range(len_x):
        if matrix[y][x] == 0:
            fresh += 1
        elif matrix[y][x] == 1:
            queue.append((x, y, -1))

is_done = False
while queue:
    x,y,cnt = queue.popleft()
    # for m in matrix:
    #     print(m)
    # print("========================")
    if fresh == 0:
        is_done = True
    step = cnt + 1
    for v_x, v_y in vectors:
        next_x = v_x + x
        next_y = v_y + y
        if 0 <= next_x < len_x and 0 <= next_y < len_y and matrix[next_y][next_x] == 0:
            queue.append((next_x, next_y, step))
            matrix[next_y][next_x] = 1
            fresh -= 1

if is_done:
    print(step)
else:
    print(-1)