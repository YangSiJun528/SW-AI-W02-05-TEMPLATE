# 문제: 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 링크: https://www.acmicpc.net/problem/2606
# AI 사용 횟수:
# AI 사용 방법:
# 목표 시간: 30분
# 실제 시간: 13분 27초

# 1. 초기 접근
# 그냥 dfs/bfs로 다 읽으면 되는데,
# cnt값은 시작 위치 제외하고 올리고
# 이미 방문한 곳 안가면 됨.

# 2. 풀이 전략
# dfs/bfs다 되는데 dfs로 풀어볼까 함.

# 3. 막힌 점 / 실수
# 유형: [접근법] [구현] [엣지케이스] [최적화]
#

# 4. 최종 코드
import sys
from collections import defaultdict

input = sys.stdin.readline

total = int(input().strip())
inputs = int(input().strip())
raws = [tuple(map(int, input().split())) for _ in range(inputs)]

#print(raws)

graph = defaultdict(list)
for u, v in raws:
    graph[u].append(v)
    graph[v].append(u)

#print(graph)

stack = [1] # 바이러스는 1번 고정
visited = {1}
cnt = -1 # 본인은 감염시킨 수에서 제외 - 이거 아니면 append할 때 cnt 올려도 됨.

while stack:
    u = stack.pop()
    cnt += 1
    for v in graph[u]:
        if v in visited:
            continue
        else:
            visited.add(v)
            stack.append(v)
print(cnt)