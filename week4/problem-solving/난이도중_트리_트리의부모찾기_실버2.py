# 문제: 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 링크: https://www.acmicpc.net/problem/11724
# AI 사용 횟수: 2
# AI 사용 방법: 루트 없는 트리 정의 물어봄, defaultlist 복잡한거 사용법 물어봄
# 목표 시간: 45분
# 실제 시간: 39분 12초

# 1. 초기 접근
# 트리: 사이클 없는 연결 그래프
# 루트를 임의로 지정하면 우리가 생각한 트리가 됨
# bfs로 넒게 퍼져가면서 level을 1씩 올리면 각 노드의 레벨을 정할 수 있음
# 또한, 이전 노드의 값을 함께 넘겨주면 부모 데이터도 저장하는 dict를 만들 수 있음.
# -------------
# 풀다보니까 느낀게...
# 근데 굳이 이렇게 안하고 그냥 dfs로 읽으면서 별도 rs dict에 저장하는 식을 의도한듯?
# 파이썬 자체가 좀 쉽게쉽게 복잡한게 가능해서 무식해도 풀리나 싶음

# 2. 풀이 전략
# graph 만들기
# 대신 n : {sub: [], parent=None} 이 기본값임.
# dfs로 1부터 시작하면서 반복, (cur, parent, cur_lv)
# 이후에 n으로 for로 돌면서 부모 출력하기

# 3. 막힌 점 / 실수
# 유형: [접근법] [구현] [엣지케이스] [최적화]
# [접근법] root가 안정해진 트리는 사실 상 graph처럼 처리하는게 올바름.
#        이름을 children으로 짓고, 단방향처럼 처리했는데, (TreeNode 클래스처럼)
#        루트가 정해진 상태에서 dfs로 탐색할 때나 방향을 정할 수 있음.
#        코드 바꾸긴 그래서 대충 끼워 맞춤
# [구현] level 필요 없었음

# 4. 최종 코드
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

# defaultlist는 인자로 생성 함수를 사용함. 즉, 인자없는 lambda를 넘겨줄 수 있음.

cnt = int(input().strip()) # 1번 빼고 입력받으니까

#
graph = defaultdict(lambda: {"to": [], "parent": None})

for _ in range(cnt-1): # 1번은 이미 있음.
    u, v = map(int, input().split())
    graph[u]["to"].append(v)
    graph[v]["to"].append(u)

#print(tree)

queue = deque([(1, None, 0)])
visited = {1}

while queue:
    cur, p, lv = queue.popleft()
    #print(cur)
    graph[cur]["parent"] = p
    for c in graph[cur]["to"]:
        if c in visited:
            continue
        else:
            queue.append((c, cur, lv+1))
            visited.add(c)

#print(tree)
#print("----------")

for i in range(cnt):
    if graph[i + 1]["parent"] is not None:
        print(graph[i + 1]["parent"])
