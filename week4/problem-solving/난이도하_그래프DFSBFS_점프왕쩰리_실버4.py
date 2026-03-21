# 문제: 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 링크: https://www.acmicpc.net/problem/16173
# AI 사용 횟수:
# AI 사용 방법:
# 목표 시간: 30분
# 실제 시간: 21분 43초

# 1. 초기 접근
# 이건 좀 쉽지 않을까 싶은데?
# 그냥 해당 지점에서 가능한곳으로 이동하면서 끝 점에 이동할 수 있는지만 보면 됨
# DFS, BFS든 상관없이 걍 풀면 되는거 아닌가?
# 근데 굳이 dfs 써야하나?
# 게임 구역의 크기가 2~3이며는 경우에 수가 몇 안되서 하드코딩도 가능할거 같긴 한데
# 그냥 dfs로 ㄱㄱ

# 2. 풀이 전략
# 매트릭스 만들고 아래/오른쪽으로 이동하면서 끝점 되면 true, 아니면 false반환

# 3. 막힌 점 / 실수
# 유형: [접근법] [구현] [엣지케이스] [최적화]
# [최적화, 구현] 20분정도 지나서 풀었는데 타임아웃 - 먼저 푼 진혁님한테 물어보니까 철도공사처럼 억까 문제는 아니고 혼자서도 가능하다고 함.
#         원인이 뭘까... 아 0이상이라서 0 오면 에러날수도 있겠네, 다음 위치가 동일하면 제외하게 해야겠다.

# 4. 최종 코드
import sys
from collections import deque

input = sys.stdin.readline

cnt = int(input().strip())

matrix = [list(map(int, input().split())) for _ in range(cnt)]

#print(matrix)

queue = deque([(0,0)])

can_win = False
while queue:
    x, y = queue.popleft()
    if x == cnt-1 and y == cnt-1:
        can_win = True
        break
    for vec_x, vec_y in [(0,1), (1,0)]:
        n_x = x + (vec_x * matrix[y][x])
        n_y = y + (vec_y * matrix[y][x])
        if n_x >= cnt or n_y >= cnt or (n_x == x and n_y == y):
            continue
        queue.append((n_x, n_y))

if can_win:
    print("HaruHaru")
else:
    print("Hing")
