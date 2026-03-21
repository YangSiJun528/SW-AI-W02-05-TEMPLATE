# 문제: 트리 - 상근이의 여행 (백준 실버4)
# 링크: https://www.acmicpc.net/problem/9372
# AI 사용 횟수:
# AI 사용 방법:
# 목표 시간: 30분
# 실제 시간: 30분(1트 실패) - 17분

# 1. 초기 접근
# 인수 자체는 무한루프만 없으면 넉넉할듯?
# 그냥 인수 그대로 받아서 그래프 만들고
# 가능한 모든 경로로 탐색해서 모든 경로 도달한 시점에 cnt를 설정하고
# 그거보다 크면 중단하게 하면 될 듯?
# dfs/bfs 다 상관없는데
# 전역변수 쓰는거 보면 반복문이 나아보여서 bfs로 풀기.
# 인풋 처리를 중간중간에 껴서 처리해야 할 듯.

# 2. 풀이 전략
# 인풋 값 처리하는건 빼고 설명
# max는 대충 엄청 큰 값
# 그래프 정의
# 반복하면서 접근하고 cnt 1씩 증가하며 dfs 탐색
# visited set의 길이가 국가의 수와 같아지면 종료
# 나머지 큐도 다 종료 (그냥 함수 만들고 리턴시켜버리면 될 듯?)
# 엣지 케이스는 없다고 봐도 될거 같은데, 일단 실행해보고 생각 ㄱㄱ

# 3. 막힌 점 / 실수
# 유형: [접근법] [구현] [엣지케이스] [최적화]
# [접근법] 풀다보니까 알았는데, 이거 그냥 dfs로 끝에 닿으면 제일 짦은 접근 법이니까 쉽게 풀 수 있음.
#        이게 뱡향이 있으면 몰라도 없으면 어디서나 시작하던 최소 횟수는 동일할듯?
# [구현]  아마 구현 실수가 좀 있던 듯.
#        이진혁님한테 더 괜찮은 DFS/BFS 코드를 받아서 이걸로 외울듯?

# 4. 최종 코드
import sys
from collections import defaultdict, deque

loop_n = int(sys.stdin.readline().strip())

for _ in range(loop_n):
    cntr_n, airpln_n = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)

    start = None
    for _ in range(airpln_n):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
        start = u # 강 암데나

    #print(graph)

    queue = deque([start])
    visited = {start}

    cnt = 0
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v in visited:
                continue
            else:
                visited.add(v)
                queue.append(v)
                cnt += 1
    print(cnt)