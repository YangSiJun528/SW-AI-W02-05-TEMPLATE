# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971
import sys

cnt = int(sys.stdin.readline().strip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(cnt)]

# [from][to]
# 일단 각 node에서 모든 방향으로 가면 됨.
# 백트레킹 없어도 되지 않나 싶은데, 그러면 N이 10개라서 N^N이면 타임아웃남.
# 최소 비용이라 하나 dfs로 구했으면 스킵 가능해짐.
# 안해서 나쁠거 없으므로 추가.

# 이번에도 n-queen 문제와 비슷한데, 접근 여부를 어떻게 확인할지가 고민임.
# 뭐 근데 접근한 내역 List나 Set 하면 될 듯? 접근한 위치가 n인데,
# 내 위치에 접근 불가능하면 그냥 종료시키고 맞으면 돌아가는 비용 추가해서 계산.

def gogo(graph, remaining, cur_n, start_n):
    if not remaining:
        if graph[cur_n][start_n] == 0:
            return 10**8 # 대충 최댓값
        else:
            return graph[cur_n][start_n]
    min_return = 10**8
    for i in range(len(remaining)):
        next_node = remaining[i]
        next_remaining = remaining[i+1:] + remaining[:i]
        if graph[cur_n][next_node] > 0: # 갈 수 있을 때만
            min_return = min(gogo(graph, next_remaining, next_node, start_n) + graph[cur_n][next_node], min_return)
    return min_return

min_cost = 10**8
for i in range(cnt):
    remaining = list(range(cnt))
    remaining = remaining[i+1:] + remaining[:i]
    cost = gogo(graph, remaining, i, i)
    if cost < min_cost:
        min_cost = cost

print(min_cost)