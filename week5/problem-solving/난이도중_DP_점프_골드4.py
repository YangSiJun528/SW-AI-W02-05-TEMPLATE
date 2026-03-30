# 문제: DP - 점프 (백준 골드4)
# 링크: https://www.acmicpc.net/problem/2253
# AI 사용 횟수:
# AI 사용 방법:
# 목표 시간: 45분
# 실제 시간: 의미없음 - 답보고 다시 푸는거라

# 1. 초기 접근
# 일단 답 보면서 접근
# 점프할 때, k-1, k, k+1로 속도를 높일 수 있음. - (풀이 전략에서 k를 j로 설명)
# 즉 현재 위치 i와 속도 k일 때, 도달 가능한 최소 횟수를 저장해야 함.
# 근데 i는 n+1로 크기 할당 가능하지만, k는 개수가 명확하지 않음. 141로 가능((141+1) * (141/2) = 10011)하다지만, 명확하지 않고,
# 내가 이런걸 문제 풀면서 추측 못하기 때문에 제외함.
# dp = [dict() for _ in range(n + 1)] << 이 방식이 2차원으로 풀 때 아직 나한텐 더 직관적인듯?

# 2. 풀이 전략
# 일단 시작 지점은 dp[1][0] = 0 임
# 앞으로 현재 i에서 다음 지점을 체크하는 식으로 전개하기.
# 모든 dp[i]까지 도달하게한 j를 보고, j-1, j, j+1로 next_i와 next_j를 구하고 dp[next_i][next_j]에 현재 값 + 1을 넣기 (최소값인 경우)
# 단, 엣지 케이스로 j가 0이거나, 설정된 영역 바깥이거나 이동이 불가능한 경우 종료해야 함.

# 3. 막힌 점 / 실수
# 유형: [접근법] [구현] [엣지케이스] [최적화]
#

# 4. 최종 코드
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
blocked = {int(input().strip()) for _ in range(m)}

dp = [dict() for _ in range(n+1)]
dp[1][0] = 0

for i in range(1, n+1):
    if i in blocked:
        continue

    for jump, cnt in dp[i].items():
        for next_j in (jump-1, jump, jump+1):
            if next_j <= 0:
                continue
            next_i = i + next_j
            if next_i in blocked or next_i > n:
                continue
            dp[next_i][next_j] = min(cnt + 1, dp[next_i].get(next_j, 10**6+1)) # get 써서 없으면 최댓값 처리

if dp[n]:
    print(min(dp[n].values()))
else:
    print(-1)
