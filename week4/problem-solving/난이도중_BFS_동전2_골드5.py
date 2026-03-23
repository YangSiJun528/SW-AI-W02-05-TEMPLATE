# 문제: BFS - 동전 2 (백준 골드5)
# 링크: https://www.acmicpc.net/problem/2294
# AI 사용 횟수: 2
# AI 사용 방법: 메모리 초과 접근법 물어봄. 시간 초과 접근법 물어봄
# 목표 시간: 45분
# 실제 시간: 39분 40초

# 1. 초기 접근
# 일단 인풋값 처리 추가
# 이게 왜 dfs지?
# 동전 개수는 10^2인데, 이걸 계속 반복한다 치면 O(v+e)라고 치고 10^2 + (10^2 * 10^2)이고,
# 그걸 각 동전마다 2중으로 반복한다 치면 10^7~10^8 정도 되는건가? -> (2중이 아니라 2승이 되서 걍 못푸는 문제가 되어버림. 판단을 이상하게 했네)
# 충분히 풀리긴 하겠네, 중복 처리 줄어들면 더 그럴거고
# 가치가 같은 동전이 주어질 수 있다고 하는데, 어차피 계속 쓸 수 있으니까 중복 처리는 제거해도 될 듯?
# -----------------------------
# 저게 좀 틀린거 같긴 했음.
# 2중이 아니라 2승이라 시간 초과.
# 중복 처리가 필요했었음. 결국 특정 cost까지 가는 가장 낮은 cnt일때 visited처리해두면 따로 처리해줄 필요없음.
# 이게 트리나 매트릭스 형태로보는 최단시간 문제로 생각하면 이해되는데, 이 관점으로 보는게 어려웠음.

# 2. 풀이 전략
# 인풋 받기
# n 전체 루프 돌면서,
# bfs로 가능한 동전들 다 탐색
# 만약 동전의 크기가 같으면 rs에 min 연산해서 넣기
# rs의 기본값은 -1 (불가능한 경우)

# 3. 막힌 점 / 실수
# 유형: [접근법] [구현] [엣지케이스] [최적화]
# [구현] 일단 성공은 하는데, 메모리 제한에 걸림. 뭐 메모리 많이 쓰긴 하는거 같은데 흠...
#       메모리가 확실히 많이 늘어나는 구조같긴 함
#       모르겠는데... 일단 cnt랑 cost 조기조건 종료 추가함 - 그래도 실패
# [접근법] 소모시간 고려를 전혀 안함. 구상을 잘못했어.
# [접근법] 0원에서 시작하면 for문으로 처리할 필요가 없음.

# 4. 최종 코드
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

# # 근데 k가 10^4까지면 동전이 10^5보다 작거나 같으면 안되는거 아닌가?
# coins = {int(input().strip()) for _ in range(n)}

coins = []

for _ in range(n):
    coin = int(input().strip())
    if coin not in coins and coin <= k:
        coins.append(coin)

rs = -1

queue = deque([(0, 0)])
visited = {}
while queue:
    cost, cnt = queue.popleft()
    if cost == k:
        rs = min(rs, cnt) if rs != -1 else cnt
    for coin in coins:
        if k >= cost+coin and not visited.get(cost+coin):
            queue.append((cost+coin, cnt+1))
            visited[cost+coin] = cnt+1

print(rs)

