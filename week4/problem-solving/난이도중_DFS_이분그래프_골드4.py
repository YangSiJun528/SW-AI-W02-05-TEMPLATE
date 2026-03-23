# 문제: DFS - 이분 그래프 (백준 골드4)
# 링크: https://www.acmicpc.net/problem/1707
# AI 사용 횟수: 1
# AI 사용 방법: 실패 사유 물어봄. (모두 연결된 그래프가 아닐 수 있었음)
# 목표 시간: 45분
# 실제 시간: 36분 53초

# 1. 초기 접근
# 이거 이분 그래프 개념 검색하다가 힌트를 받아버림
# 레벨로 같은걸로 묶을 수 있나본데?
# 왜냐하면 양방향 그래프에서,
# 어떤 정점을 A색으로 칠했다면 그와 인접한 정점들은 모두 B색이어야 함.
# 그리고 그 인접 정점들에 연결된 다른 정점들은 다시 A색이어야 함.
# 즉, 인접한 정점끼리는 항상 서로 다른 색으로만 연결되어야 하므로,
# 탐색하면서 색을 번갈아 칠했을 때 모순이 생기면 이분 그래프가 아님.


# 2. 풀이 전략
# dict로 인접 목록, 상태를 저장
# dfs로 탐색
# visited 처리는 하되, 탐색 시도에서 쓰려는 컬러랑 다르면 실패처리 종료.
# 문제없이 끝나면 True
# 성공 여부 플래그 확인해서 분기 호출

# 3. 막힌 점 / 실수
# 유형: [접근법] [구현] [엣지케이스] [최적화]
# [구현] 뭔가 visited 처리를 최적화해서 append 때 하는게 별로같았음.
#        흐름 상 visited되어도 연결되어 있으면 확인해야 해서 내부로 뺀게 자연스러워 보였음.
#        근데 이게 실패 원인은 아니였고...
# [접근법] 지문에서 모두 연결된 그래프라는 말이 없었으므로 고려했어야 함.

# 4. 최종 코드
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

loop = int(input().strip())

for _ in range(loop):
    is_bg = True
    graph = defaultdict(list)
    cnt_v, cnt_e = map(int, input().split())
    for __ in range(cnt_e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = {}

    for i in range(1, cnt_v + 1): # 지문에 모두 다 연결된 상태라는 말이 없었음.
        if visited.get(i):
            continue
        queue = deque([(i, 1)]) # 번호, 상태
        #visited[1] = 1 # 1과 -1로 구분

        while queue:
            u, state = queue.popleft()
            if visited.get(u):
                if visited[u] != state:
                    is_bg = False
                    break
                continue
            visited[u] = state
            for v in graph[u]:
                queue.append((v, state*-1))

    if is_bg:
        print("YES")
    else:
        print("NO")