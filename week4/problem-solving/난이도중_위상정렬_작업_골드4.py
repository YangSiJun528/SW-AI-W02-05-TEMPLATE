# 문제: 위상정렬 - 작업 (백준 골드4)
# 링크: https://www.acmicpc.net/problem/2056
# AI 사용 횟수: 2
# AI 사용 방법: 접근법이 맞는지 모르겠어서 물어봄. - 50분 넘어서 풀이 요청
# 목표 시간: 45분
# 실제 시간: (실패) 50분

# 1. 초기 접근
# 전형적인 위상정렬 문제
# 지문: 선행 관계라는 게 있어서, 어떤 작업을 수행하기 위해 반드시 먼저 완료되어야 할 작업들이 있다.
# 지문: 선행 관계에 있는 작업이 하나도 없는 작업이 반드시 하나 이상 존재한다.
# 위상정렬 만들면 되는데, 1번 작업은 항상 0임. 근데 다른게 더 있을수도 있어서 확인 필요
# N은 10^4
# -------------
# 인풋값 처리가 좀 중요할듯?
# graph가 만들어지면 indgree만들어서 처리하면 됨.
# 그러면 음... 위상정렬인데, 시간 처리가 필요하네
# 먼저 들어오는걸로 처리하니까, 큐에서 계속 시간을 담아 보내주긴 해야함.
# 그리고 마지막 번호면 끝이니까 바로 출력하면 됨.
# 어차피 단방향(선행 관계)에 방향이 있는 문제니까. visited 처리를 하지말고, cost를 기반으로 처리하면 될 듯?
# -> 그리고 위상정렬의 경우 indegree가 0일때 한번 큐에 넣으니까 visited 처리가 필요없음.

# 2. 풀이 전략
# graph 만들기 - 인풋 받을 때 주의
# indegree도 처리

# 3. 막힌 점 / 실수
# 유형: [접근법] [구현] [엣지케이스] [최적화]
# [구현] 위상정렬 구현이 약간 햇갈려서 만들어둔 구현을 약간 참고함. (심지어 만들어둔 변수명 의미가 반대라 더 햇갈렸음;;)
# [접근법] 구상에서부터 약간 잘못이 있었음. 위상정렬 개념과 시간을 넘겨준다는 걸 어떻게 처리할 지 확질하지 않았던 문제

# 4. 최종 코드
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

cnt_in = int(input().strip())

graph = defaultdict(list)
indegree = defaultdict(lambda: 0)
costs = defaultdict(lambda: 0)
# 가장 이른 시작 지점. D는 A,B,C가 끝나야 하는데, 각각 7,3,1이라면 7이 이전의 cost값이 되어야 함.
# 따라서 indegree[v] == 0 확인 및 큐에 넣는 처리와 무관하게
earliest = defaultdict(lambda: 0)

for i in range(1, cnt_in+1):
    inputs = list(map(int, input().split()))
    cost = inputs[0]
    costs[i] = cost
    if inputs[1] > 0:
        dependencies = inputs[2:2+inputs[1]+1]
        for d in dependencies:
            graph[d].append(i)
            indegree[i] += 1
    else:
        indegree[i] = 0

# print(graph)
# print(indegree)
# print(costs)

queue = deque()
for i in range(1, cnt_in+1):
    if indegree[i] == 0:
        queue.append(i)

rs = 0

while queue:
    num = queue.popleft()
    finish = earliest[num] + costs[num] # earliest[num]: num가 실행될 수 있는 가장 빠른 시간
    rs = max(rs, finish)
    for v in graph[num]:
        earliest[v] = max(earliest[v], finish)
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)

print(rs)

# rs = 0
# while queue:
#     cost, num = queue.popleft()
#     #print(cost, num)
#     cost += costs[num]
#     rs = max(rs, cost)
#     if num == cnt_in:
#         continue
#     for v in graph[num]:
#         indegree[v] -= 1
#         if indegree[v] == 0:
#             queue.append((cost, v))
#
# print(rs)