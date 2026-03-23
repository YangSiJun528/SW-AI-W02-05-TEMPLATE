# 문제: BFS - 미로 탐색 (백준 실버1)
# 링크: https://www.acmicpc.net/problem/2178
# AI 사용 횟수: 3
# AI 사용 방법: dfs로 구현 가능한지, 왜 어려운지 대화
# 목표 시간: 45분
# 실제 시간: 41분 09초

# 1. 초기 접근
# 전형적인 dfs, bfs문제 - 최단거리찾기 유형
# 어차피 다 탐색하는걸 가정해야하니까 뭐든 다 비슷함
# dfs 반복문 햇갈렸으니까 연습해본다는 마인드로 ㄱㄱ
# 근데 이미 도달한 위치를 복구하는 처리를 어떻게 하지? 한번이라도 간게 아니라 경로를 처리해야 하는데
# 아마 내 기억으론 방문했던 위치에 step순서를 두고 그게 본인보다 크면 종료하는 식으로 했던거 같음.
# visited가 도달하는 cost까지 포함하는 느낌.

# 2. 풀이 전략
# 매트릭스 저장
# 00부터 시작해서 접근 가능한 곳으로 이동
# 이동했으면 본인의 누적 cost 적기
# 다음 가능한 이동 지점으로 가기
# 만약 cost가 있는데, 본인보다 작거나 같으면 넘기기
# 크면 cost + 1해서 호출하기 (이러면 무한루프 되는거 아닌가? 근데 여기서 한번 이동하고 나면 이제 차이나서 ㄱㅊ)
# 보니까 cost가 아니라 step으로 하는게 직관적일듯?
# -------------------------
# 괜히 dfs로 풀었음. 이런거 bfs가 훨씬 좋음. dfs도 가능은 한데, 되게 복잡해서 안쓰는게 맞았음. 괜히 dfs 연습으로 써보겠답시고 시간 날렸네;;

# 3. 막힌 점 / 실수
# 유형: [접근법] [구현] [엣지케이스] [최적화]
# [접근법] dfs도로 최단거리 구현이 쉬울줄 알았는데 아니였음.

# 4. 최종 코드
import sys
from collections import deque

input = sys.stdin.readline

len_y, len_x = map(int, input().split())

matrix = [list(input().strip()) for _ in range(len_y)]
visited = [[False] * len_x for _ in range(len_y)]

vector = [(1,0), (0,-1), (0,1), (-1,0)]

queue = deque([(0,0,1)])
visited[0][0] = True

while queue:
    x, y, steps = queue.popleft()
    #print(x, y, steps)
    if y + 1 == len_y and x + 1 == len_x:
        print(steps)
        break
    for v_x, v_y in vector:
        next_x = x + v_x
        next_y = y + v_y
        if 0 <= next_x < len_x and 0 <= next_y < len_y and matrix[next_y][next_x] != '0':
            if not visited[next_y][next_x]:
                queue.append((next_x, next_y, steps+1))
                visited[next_y][next_x] = True
