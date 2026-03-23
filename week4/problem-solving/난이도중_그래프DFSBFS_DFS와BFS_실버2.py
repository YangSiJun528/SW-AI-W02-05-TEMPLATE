# 문제: 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 링크: https://www.acmicpc.net/problem/1260
# AI 사용 횟수: 1
# AI 사용 방법: DFS 외운 구현이 잘못되었음. 내가 외운게 이상한거 같아서 물어봄.
# 목표 시간: 45분
# 실제 시간: 25분 45초

# 1. 초기 접근
# 그냥 dfs, bfs 만들고 방문 순서대로 출력하면 끝
# 대신 여러 곳에 갈 수 있을 때 하나만 간다는거, 양방향인거만 주의하면 됨

# 2. 풀이 전략
# 그냥 통일성있게 반복문으로 해보기

# 3. 막힌 점 / 실수
# 유형: [접근법] [구현] [엣지케이스] [최적화]
# [구현] DFS 구현을 잘못 외우고 있었음. 왜 이렇게 했는지 모르겠는데, 당연하게 방문하고 나서 visited 확인해야 그 vertex 기준에서 처리되는건데 왜 이렇게 했었지
#       이거 정리해둔거 다시 확인해봐야겠네
#       basic의 dfs_iter도 잘못된거 같고 이러면

# 4. 최종 코드
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

cnt_v, cnt_e, start = map(int, input().split())

graph = defaultdict(list)

for _ in range(cnt_e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

#print(graph)

rs = []
stack = [start]
visited = set()

while stack:
    u = stack.pop()

    if u in visited:
        continue

    visited.add(u)
    rs.append(u)

    for v in sorted(graph[u], reverse=True):
        if v not in visited:
            stack.append(v)
print(" ".join(map(str, rs)))

rs = []
queue = deque([start])
visited = {start}

while queue:
    u = queue.popleft()
    rs.append(u)
    for v in sorted(graph[u]):
        if v in visited:
            continue
        else:
            visited.add(v)
            queue.append(v)

print(" ".join(map(str, rs)))




