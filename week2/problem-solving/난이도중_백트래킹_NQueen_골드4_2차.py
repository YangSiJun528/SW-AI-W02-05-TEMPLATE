# ========================
# 풀이 완료까지 걸린 시간: 약 50분 (시간 넘음) / 30분
# 스터디모드 GPT 도움 횟수: 1 - 구현 실수 약간 있었음. used_diag_asc 값 구하는거나. y,x가 놓을 위치, 놓은 위치의 역할을 섞어서 한다거나..
# 백준 사이트에서 풀었는가?: X
# 생각: 근데 이게... 이미 해결 방법을 알고 있는 상태에서 문제를 푸는게 의미가 있나? 단순 구현 실수만 많음. 이게 정의를 잘못하고 그런걸 수도 있지만
#       그냥 집중이 잘 안되고, 새로운 유형을 보면서 분석을 더 해봐야 할거 같은데, 애매하게 아는 상태에서 빠르게 시간 제한만 맞출라니까 잘 안되네
#       이것도 힌트 안보고 노가다하면 할 수 있었을거 같긴 함.
# ========================
# 일단 이미 풀이 방법을 알고 있는 상태므로 단순 구현만 하면 됨.
# 크기가 N × N인 체스판 위에 "퀸 N개"를 서로 공격할 수 없게 놓는 문제
# 즉, 한 줄에 하나만 가능하므로 모든 열에 다 해야한다.
# 따라서 path가 n까지 다 가야함.
#   근데 이 문제의 경우 리턴이 아니라 카운트이므로 굳이 path가 아니라 x_idx여도 될 듯?

# 한 칸을 쓰면 그 칸의 y,x는 사용이 불가능해짐.
# 따라서 각 칸에 한 줄씩 하는 식으로 하면 됨.
# 그리고 체크도 True로 해당 선을 사용했는지 하고, 롤백해주면 됨.
import sys

cnt = int(sys.stdin.readline().strip())
diag_cnt = 2 * cnt - 1

used_x = [False] * cnt
used_diag_asc = [False] * diag_cnt  # -> 방향 기준 위에서 아래
used_diag_desc = [False] * diag_cnt  # ->  방향 기준 아래에서 위


def backtracking(x_idx, used_x, used_diag_asc, used_diag_desc):
    if x_idx == cnt: # 인덱스 값을 넘음, 즉 문제 없이 끝까지 온 상태
        return 1
    rs = 0
    for next_y in range(cnt):
        x = x_idx # 놓을 x 위치
        y = next_y # 놓을 y 위치
        if (not used_x[y]
                and not used_diag_asc[y - x + (cnt-1)]
                and not used_diag_desc[y + x]): # 둘 수 있는지 확인
            used_x[y] = True
            used_diag_asc[y - x + (cnt-1)] = True
            used_diag_desc[y + x] = True
            rs += backtracking(x + 1, used_x, used_diag_asc, used_diag_desc) # 맞으면 처리 후 다음으로 넘김
            used_x[y] = False
            used_diag_asc[y - x + (cnt-1)] = False
            used_diag_desc[y + x] = False
    return rs


print(backtracking(0, used_x, used_diag_asc, used_diag_desc))