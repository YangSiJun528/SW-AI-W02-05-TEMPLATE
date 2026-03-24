# 문제: BFS - 쉬운 최단거리 (백준 실버1)
# 링크: https://www.acmicpc.net/problem/14940
# AI 사용 횟수:
# AI 사용 방법:
# 목표 시간: 30분
# 실제 시간: 23분 44초

# 1. 초기 접근
# 목표 지점에서 cnt를 0부터 1씩 늘려가면서 bfs로 탐색
# 최단거리 탐색 조건을 지키면서 visited 처리를 하면 됨
# visited를 2차원 배열로 저장하고 join으로 출력하면 될 듯?

# 2. 풀이 전략

# 3. 막힌 점 / 실수
# 유형: [접근법] [구현] [엣지케이스] [최적화]
# [구현] 지문을 잘 못보고, 가능한데(1인데) 못가는 곳과 원래 못가는 곳을 구분해야 한다는 걸 놓침.
#       예시에는 없었지만 지문에는 있었으므로 잘 봤어야 하는데 쉬운 문제라 생각해서 대충 넘긴게 문제였음.

# 4. 최종 코드
import sys
from collections import deque

input = sys.stdin.readline

len_y, len_x = map(int, input().split())

matrix = [input().split() for _ in range(len_y)]
visited = [[-1]*len_x for _ in range(len_y)]
vector = [(1,0), (0, 1), (-1,0), (0,-1)]

#print(matrix)

start_x = -1
start_y = -1

for i in range(len_y):
    for j in range(len_x):
        if matrix[i][j] == '2':
            start_y = i
            start_x = j

queue = deque([(start_x,start_y,0)])
visited[start_y][start_x] = 0

while queue:
    x, y, cnt = queue.popleft()
    for v_x, v_y in vector:
        next_x = x + v_x
        next_y = y + v_y
        if (0<=next_x<len_x and 0<=next_y<len_y
                and visited[next_y][next_x] == -1
                and matrix[next_y][next_x] != '0'):
            queue.append((next_x, next_y, cnt+1))
            visited[next_y][next_x] = cnt + 1


for y in range(len_y):
    for x in range(len_x):
        if visited[y][x] == -1:
            if matrix[y][x] == '1':
                visited[y][x] = -1
            elif matrix[y][x] == '0':
                visited[y][x] = 0
    print(" ".join(map(str, visited[y])))