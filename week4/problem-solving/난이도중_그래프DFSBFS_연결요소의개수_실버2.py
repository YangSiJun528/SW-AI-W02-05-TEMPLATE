# 문제: 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 링크: https://www.acmicpc.net/problem/11724
# AI 사용 횟수: 0
# AI 사용 방법: X
# 목표 시간: 45분
# 실제 시간: 23분 00초

# 1. 초기 접근
# 이거 그냥 간단하게 연결 요소(연결 안된 그래프들) 개수를 세면 됨
# 그냥 dfs로 재귀로 전체 수만큼 도는데,
# 방문했던거면 넘어가고 아니면 카운트 늘리고 dfs호출하면 됨

# 2. 풀이 전략
#

# 3. 막힌 점 / 실수
# 유형: [접근법] [구현] [엣지케이스] [최적화]
# [구현] 마지막 순회 시 노드 숫자가 0이 아니라 1부터 시작했어야 함.
# [최적화] 재귀 에러나는데 아마 bfs나 dfs_iter로 풀었어야 하지 않나... 일단 setrecursionlimit로 풀이.

# 4. 최종 코드
import sys
from collections import defaultdict

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

cnt_v, cnt_e = map(int, input().split())
graph = defaultdict(list)

for _ in range(cnt_e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = set()

def dfs(u):
    visited.add(u)
    for v in graph[u]:
        if v in visited:
            continue
        else:
            dfs(v)
    return

cnt = 0
for n in range(1, cnt_v+1):
    if n not in visited:
        cnt += 1
        dfs(n)

print(cnt)