# ========================
# 풀이 완료까지 걸린 시간: 약 50분 (시간 넘음) / 30분
# 스터디모드 GPT 도움 횟수: 4 - 마찬가지로 구현 실수, 백트래킹 for문 안에서 슬라이싱이랑 호출 시작 조건 정의 잘못함.
#                          그냥 이미 알고 있는거라고 생각하고 정의를 빠르게 건너 뛴게 오히려 악영향을 준 듯.
#                          그리고 MAX 값 때매 틀림. 하긴 최대 10^6인데, 10^6+1이면 좀 잘못된거긴 하지.
# 백준 사이트에서 풀었는가?: X
# ========================
import sys

cnt = int(sys.stdin.readline().strip())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(cnt)]

# 갈 수 있는 모든 경로로 가기 - 순열 느낌
# 모든 도시 즉, cnt개수만큼 간 상태에서 돌아오는 값 포함해서 min만 처리하기

MAX = 10 ** 8  # 제약조건보다 큰 수

def backtracking(path, remaining, from_idx):
    cur_idx = path[-1]
    if len(path) == cnt:
        if matrix[cur_idx][from_idx] != 0:  # 갈 수 있으면 비용 계산해서 반환
            return matrix[cur_idx][from_idx]
        else:  # 아니면 가장 큰 값 반환
            return MAX
    min_cost = MAX
    for i in range(len(remaining)):
        next_idx = remaining[i]
        next_path = path + [next_idx]
        next_remaining = remaining[:i] + remaining[i + 1:]
        if matrix[cur_idx][next_idx] != 0:
            next_cost = matrix[cur_idx][next_idx]
            min_cost = min(min_cost, backtracking(next_path, next_remaining, from_idx) + next_cost)
    return min_cost


arr = list(range(cnt))
total_cost = MAX
for i in arr:
    total_cost = min(total_cost, backtracking([i], arr[:i] + arr[i + 1:], i))

print(total_cost)
