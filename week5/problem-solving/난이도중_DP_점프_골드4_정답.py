import sys

input = sys.stdin.readline

n, m = map(int, input().split())
blocked = {int(input()) for _ in range(m)}

# dp[i] = {last_jump: min_count} # jump 가능 크기만큼 배열 할당 크기를 구하기 어려움.
dp = [dict() for _ in range(n + 1)]
# dp[i][jump] = i번 돌에 마지막 점프 길이가 jump인 상태로 도착했을 때의 최소 점프 수
dp[1][0] = 0   # 1번 돌에서, 직전 점프 길이 0, 사용 점프 수 0

for i in range(1, n + 1):
    if i in blocked:
        continue

    for jump, cnt in dp[i].items(): # 현재 i번 돌에 도착 가능한 모든 상태를 순회
        for njump in (jump - 1, jump, jump + 1): # 다음 점프 길이 후보를 구하기
            if njump <= 0: # 점프 속도가 1 이상이여야 함.
                continue

            ni = i + njump # i에서 다음 점프 크기만큼 더한 다음 이동 위치(ni)를 설정
            if ni > n or ni in blocked: # 범위 밖이나 이동이 불가능한 돌이면 조기 종료
                continue

            if njump not in dp[ni] or dp[ni][njump] > cnt + 1: # 지금 경로가 dp에 저장된 것보다 적으면 재할당 (또는 dp에 해당된 경로가 없거나)
                dp[ni][njump] = cnt + 1

if dp[n]:
    print(min(dp[n].values()))
else:
    print(-1)