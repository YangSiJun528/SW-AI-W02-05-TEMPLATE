# 문제: DP - 평범한 배낭 (백준 골드5)
# 링크: https://www.acmicpc.net/problem/12865
# AI 사용 횟수:
# AI 사용 방법:
# 목표 시간: 45분
# 실제 시간:

# 1. 초기 접근
# 구하는 것: 최대 가치
# 영향 받는 것: 수, 무게
# 분기하는 경우의 수: (현재 상품을 선택 가능하다면) 선택한다 or 선택하지 않는다.

# 2. 풀이 전략
# dp[i][w] = v -> 현재 i까지 왔을 때, w만큼 무게가 남아있는 상태에서의 최대 가치 v
# dp[i-1]의 모든 경우에 수에 대해서 선택한 버전, 선택하지 않은 버전을 기록한다.
# 매 w마다 dp[i][w] = v와 dp[i][new_w] = new_v 가 저장됨.
# 이후 dp[n]의 여러 선택지의 가치 중 가장 높은 수치를 구한다.
# ----------------------------------
# 약간 감을 잡은 점은... 그냥 모든 경우의 수를 전개해가면서 2중 반복문으로 처리한다는거.
# 그리고 dp[n] 중 최소/최대값을 구한다는거? 물론 여러 방법이 있겠지만... 이게 제일 나한텐 이해하기 쉬움
# 물론 2개만 봐서 어떨진 모르겠지만, 뭐 dp[n][m] 존재 여부로도 확인하는 방법도 있긴 할 듯?
# 전반벅인 풀이는 비슷하지 않을까?

# 3. 막힌 점 / 실수
# 유형: [접근법] [구현] [엣지케이스] [최적화]
#

# 4. 최종 코드
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# 읽기 쉽게 1-index를 쓰니까 items도 더미 값 추가
items = [("DUMMY", "D")] + [tuple(map(int, input().split())) for _ in range(N)]

dp = [dict() for _ in range(N + 1)] # 뭐 사실 이거는 내부 배열도 K로 쉽긴 한데, 어려운 경우도 있으니까 dict로 연습하는게 좋은 듯?

dp[0][0] = 0 # 선택 하는지 아닌지를 비교해서 i부터 시작하기 때문에 dp[0][0] = 0

for i in range(1, N + 1): # items를 순회하면서
    weight, value = items[i]
    # i-1에서 가능한 (무게 w, 가치 v) 상태들을 기반으로,
    # i번째에서 가능한 선택지로 전재(물건을 선택/비선택)하여 새로운 상태를 만들고,
    # 같은 방향에 대해서는 최대 가치만 유지한다.
    for w, v in dp[i - 1].items():
        # 담지 않는 경우
        dp[i][w] = max(dp[i].get(w, 0), v)

        # 담는 경우
        new_w = w + weight
        new_v = v + value
        if new_w <= K:
            dp[i][new_w] = max(dp[i].get(new_w, 0), new_v)
    #print(dp[i])
print(max(dp[N].values()))
