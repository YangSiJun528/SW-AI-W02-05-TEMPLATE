# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663
# 골드4인줄은 몰랐네, 어렵긴 하더라...
# ========================
# 체스에서 퀸은 주위 8방향 + 대각선 끝까지 이동 가능하다.
# 일단 제목에서 부터 유형이 백트레킹인건 말해줬으니, 브루스포트 + 백트레킹으로 푸는게 맞음.
# 시간 복잡도 계산을 해보고 싶은데 N^2가 계산하려는 칸의 수가 됨.
# N^2을 한 칸씩 돌면서, 선택 가능한 위치를 찾아가면서 트리로 내려가는 구조가 그려짐.
# 이게 브루스 포트라 치면 N^N인데, 아마 백트레킹 쓰니까 N! 정도 될거 같음.
# ------------------------
# 구상
# 1. 매트릭스 만들기
# 2. 둘 수 있는 위치인지 확인하는 함수 만들기 - 굳이 함수 아니여도 될 듯?
# 3. dfs로 돌면서 함수 호출하고 최대값 저장
# ------------------------
# 잘못 만들었음.
# dfs가 아닌거 같음. 계속 막혀서 AI한테 힌트 부탁
# 방향성을 바꿔야 함. 실제로 여러 사례에 대한 시뮬레이션을 돌려보면서 규칙을 구해야 할 듯.
# 그래도 어려워서 책 봄.
# 완전 깔끔한 해결법임. 결국에 다른 방식으로 해보려 해도 이런 식으로 나오는 듯?
# 정답을 보고 든 생각은, 형식 자체는 일반적인 백트레킹인데, 분기 대상을 파악하고 상태를 관리하는게 진짜 어려운 문제였던거 같음. 그림 안그리면 해결 못하고...
# ------------------------
# 정답 보긴 했지만, 다시 안보고 구현 ㄱㄱ

import sys

cnt = int(sys.stdin.readline().strip())

used_x = [False] * cnt
diag_n = (cnt * 2 - 1)  # 대각선의 개수
used_diag_asc = [False] * diag_n  # 수가 커질수록 위에서 아래로 내려가므로
used_diag_desc = [False] * diag_n  # 반대니까 desc


def branch(y):
    total = 0
    for x in range(cnt):
        # 아직 모든 경로에서 안 간 곳이라면?
        if not used_x[x] and not used_diag_asc[y - x + (cnt-1)] and not used_diag_desc[y + x]:
            if y == (cnt-1):  # 끝까지 왔으면 목표를 만족하므로 값 증가
                total += 1
            else:  # 끝이 아니면 또 다른 분기 - 반복하면서 다른 x에 대한 테스트를 수행하므로 복구 필요
                used_x[x] = True
                used_diag_asc[y - x + (cnt-1)] = True
                used_diag_desc[y + x] = True
                total += branch(y + 1)  # Postorder 단계에서 값 합치기
                used_x[x] = False
                used_diag_asc[y - x + (cnt-1)] = False
                used_diag_desc[y + x] = False
        else:  # 이미 간 경우라면 여기서 다음 반복 - 코드 필요없는데 이해를 위해서
            continue
    return total  # 마지막으로 모든 분기 끝나면 값 반환


print(branch(0))

# 실패 1
# 백트래킹 + dfs 문제처럼 접근해서 빡셌음.
# def check_movable_then_point_set_true(matrix, x, y, cnt):
#     if x > cnt-1 or y > cnt-1 or x < 0 or y < 0: # 둘 수 없는 위치
#         return (matrix, x, y, cnt)
#     next_paths = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)] # 상하좌우만
#     for v_x, v_y in [(-1, -1), (-1, 1), (1, -1), (1, 1)]: # 각 대각선 방향으로
#         cur_x = x
#         cur_y = y
#         while x > cnt-1 or y > cnt-1 or x < 0 or y < 0:
#             cur_x += v_x
#             cur_y += v_y
#             next_paths.append((cur_x,cur_y))
#     # 이 시점에서 next_paths는 x,y가 갈 수 있는 모든 경로를 가지고 있음
#     for next_x, next_y in next_paths:
#         if matrix[cur_y][cur_x]:
#             return (matrix, x, y, cnt) # 이미 접근한 경로이므로 - 근데 이거 위 base case랑 합칠 수 있을듯??
#         matrix[cur_y][cur_x] = True # 지나옴 처리
#         check_movable_then_point_set_true(matrix, next_x, next_y, cnt + 1)
#
# for i in range(cnt):
#     for j in range(cnt):
#         matrix = [[False * cnt] for _ in range(cnt)]
#         rs = check_movable_then_point_set_true(matrix, i, j, 0)
#         max_n = max(rs[3], max_n)
