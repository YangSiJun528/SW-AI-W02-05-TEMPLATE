# 문제: BFS - 적록색약 (백준 골드5)
# 링크: https://www.acmicpc.net/problem/10026
# AI 사용 횟수:
# AI 사용 방법:
# 목표 시간: 45분
# 실제 시간: 21분 38초

# 1. 초기 접근
# 그냥 섬 문제랑 마찬가지인데,
# 최적화해서 cnt 세면 됨.
# 근데 N 개수가 적어서 탐색할 때 동일한 걸로 볼 조건을 인수로 넣어줘서
# 2번 돌아도 충분할듯?
# (10^2)*4(방향) 개를 탐색함
# 2번 돌아도 시간은 충분함.

# 2. 풀이 전략
# 섬 문제처럼 하되, 동일한 색으로 보는 조건을 다르게 하는 flag나 색 조건을 인수로 넘겨주기.

# 3. 막힌 점 / 실수
# 유형: [접근법] [구현] [엣지케이스] [최적화]
# [구현] i,j로 하니까 매트릭스 x,y 햇갈려서 좀 해맴

# 4. 최종 코드
import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
matrix = [list(input().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
vector = [(1,0), (-1,0), (0,1), (0,-1)]

queue = deque([]) # x,y

rs1 = 0
rs2 = 0

# for m in matrix:
#     print(m)
# print("===================")

for i in range(n):
    for j in range(n):
        #print(matrix[j][i])
        if not visited[j][i]:
            queue.append((i,j))
            visited[j][i] = True
            while queue:
                x, y = queue.popleft()
                for v_x, v_y in vector:
                    next_x = x + v_x
                    next_y = y + v_y
                    if (0 <= next_x < n and 0 <= next_y < n
                            and not visited[next_y][next_x]
                            and matrix[next_y][next_x] == matrix[y][x]):
                        queue.append((next_x, next_y))
                        visited[next_y][next_x] = True
            # for v in visited:
            #     print(v)
            # print("=======")
            rs1 += 1

queue = deque([]) # x,y
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[j][i]:
            queue.append((i,j))
            visited[j][i] = True
            while queue:
                x, y = queue.popleft()
                for v_x, v_y in vector:
                    next_x = x + v_x
                    next_y = y + v_y
                    if (0 <= next_x < n and 0 <= next_y < n
                            and not visited[next_y][next_x]
                            and (
                                    matrix[next_y][next_x] == matrix[y][x] or
                                    (matrix[y][x] in ['R', 'G'] and matrix[next_y][next_x] in ['R', 'G'])
                            )):
                        queue.append((next_x, next_y))
                        visited[next_y][next_x] = True
            rs2 += 1

print(f"{rs1} {rs2}")
