# 문제: 큐 - 뱀 (백준 골드4)
# 링크: https://www.acmicpc.net/problem/3190
# AI 사용 횟수: 0
# AI 사용 방법: X
# 목표 시간: 30분
# 실제 시간: 1시간 30분 이상 - 포기 후 코드 상당수 날리고 별도 파일에서 2트

# 1. 초기 접근
# 확실히 이게 전략 키워드를 주니까 조금 난이도가 쉬운 경우도 있는듯.
# 걍 y,x 정해가지고 큐에 길이만큼 넣고 뺴면 됨.
# 종료 조건 분석하고...

# 2. 풀이 전략
#   1. matrix 만들기
#   2. 사과 위치 memo하기
#   3. 이동 경로대로 반복하면서 종료조건 확인, 시간 증가, queue하되, 사과 있으면 popleft는 스킵
# 종료조건은
#   1. 벽에 닫거나,
#   2. 본인에 닫거나(이거는 반복문으로 하는데, 느리면 해시로 개선 가능)

# 3. 막힌 점 / 실수
# 걍 입력값 처리가 힘들었음. 16분 걸림;;;
#----------------
# 0부터 시작해야 하는데, 이미 요소가 하나 있는 1부터 시작하게 함. - 다시 보니까 cur_x랑 일치 안해서 실패했을 듯?
# 구현 시 순서를 잘못 생각함. - 이거는 구현 안해보면 상상하기 어렵긴 한데,
# 걍 구현이 빡셈. 1시간 30분 씀.
# 애매했던 부분(꼬리로 이동하면 꼬리 지워지는게 먼저임? 아님 이동하는게 먼저임?) 같은게 지문에 있었음.

# 4. 최종 코드
import sys
from collections import deque

cnt_m = int(sys.stdin.readline().strip())
matrix = [[0]*cnt_m for _ in range(cnt_m)]
cnt_apples = int(sys.stdin.readline().strip())
for _ in range(cnt_apples):
    x, y = sys.stdin.readline().split()
    matrix[int(x)-1][int(y)-1] = 1 # 인덱스니까 -1 처리

# for m in matrix:
#     print(m)

cnt_cmds = int(sys.stdin.readline().strip())
cmds = [sys.stdin.readline().split(' ') for _ in range(cnt_cmds)]
# print(cmds) # 문자에 strip 필요.

# 0: 기본, 1: 사과, 2: 몸

snake = deque([])
cur_x = 0
cur_y = 0
vector = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 앞으로 가면 오른쪽, 뒤로가면 왼쪽으로 꺽기
vector_idx = 0
cnt_frame = 0
cmd_idx = 0

# 처음 하드코딩
matrix[cur_y][cur_x] = 2
snake.append((cur_x, cur_y))
cur_x += 1 # 이동 처리
cnt_frame += 1
while True:
    # 현재 위치 사과 확인
    is_eat = False
    if matrix[cur_y][cur_x] == 1:
        is_eat = True

    # 현재 위치 이동 처리
    matrix[cur_y][cur_x] = 2
    snake.append((cur_x, cur_y))
    cnt_frame += 1

    # === 여기가 출력 지점
    # for m in matrix:
    #     print(m)
    # print(f"cnt_frame: {cnt_frame}")
    # print("=============")

    # 방향 명령어 처리
    if cmd_idx < len(cmds) and cmds[cmd_idx][0] == str(cnt_frame): # 명령어 실행 상태
        cmd = cmds[cmd_idx][1].strip()
        if cmd == 'D':
            vector_idx = 0 if vector_idx == 3 else vector_idx + 1
        else: # cmd == 'L':
            vector_idx = 3 if vector_idx == 0 else vector_idx - 1
        cmd_idx += 1
        #print(f"cmd:{cmd}, vector_idx:{vector_idx}")

    # snake의 tail 지우기
    if not is_eat: # 사과 안 먹었을 때만
        tail_x, tail_y = snake.popleft()
        matrix[tail_y][tail_x] = 0 # 복구 처리

    # 이동 예정 위치 처리
    v_x, x_y = vector[vector_idx]
    cur_x += v_x
    cur_y += x_y

    # 충돌 여부 확인
    if not (0 <= cur_x <= cnt_m-1 and 0 <= cur_y <= cnt_m-1): # 벽이랑 충돌
        cnt_frame += 2
        break
    elif matrix[cur_y][cur_x] == 2: # 본인에 충돌
        cnt_frame += 1
        break
    #print(cur_x, cur_y)

print(cnt_frame)


# v1 실패코드
# import sys
# from collections import deque
#
# cnt_m = int(sys.stdin.readline().strip())
# matrix = [[0]*cnt_m for _ in range(cnt_m)]
# cnt_apples = int(sys.stdin.readline().strip())
# for _ in range(cnt_apples):
#     x, y = sys.stdin.readline().split()
#     matrix[int(y)-1][int(x)-1] = 1 # 인덱스니까 -1 처리
#
# # for m in matrix:
# #     print(m)
#
# cnt_cmds = int(sys.stdin.readline().strip())
# cmds = [sys.stdin.readline().split(' ') for _ in range(cnt_cmds)]
# # print(cmds) # 문자에 strip 필요.
#
# # 0: 기본, 1: 사과, 2: 몸
#
# snake = deque([])
# cur_x = 0
# cur_y = 0
# vector = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 앞으로 가면 오른쪽, 뒤로가면 왼쪽으로 꺽기
# vector_idx = 0
# cnt_frame = 1 # 이미 한 번 움직였다고 치고 시작
# cmd_idx = 0
#
# # 초기 세팅
# matrix[cur_y][cur_x] = 2
# snake.append((0,0))
#
# while True:
#     # snake의 tail 지우기
#     if not matrix[cur_y][cur_x] == 1: # 사과 먹음
#         pass # 어차피 덮어씌워짐
#     else:
#         tail_x, tail_y = snake.popleft()
#         matrix[tail_y][tail_x] = 0 # 복구 처리
#
#     # 명령어 처리
#     if cmds[cmd_idx][0] == str(cnt_frame): # 명령어 실행 상태
#         cmd = cmds[cmd_idx][1].strip()
#         if cmd == 'D':
#             vector_idx = 0 if vector_idx == 3 else vector_idx + 1
#         else: # cmd == 'L':
#             vector_idx = 3 if vector_idx == 0 else vector_idx - 1
#
#     # 이동 예정 위치 처리
#     v_x, x_y = vector[vector_idx]
#     cur_x += v_x
#     cur_y += x_y
#
#     # 충돌 여부 확인
#     if not (0 <= cur_x <= cnt_m-1 and 0 <= cur_y <= cnt_m-1): # 벽이랑 충돌
#         break
#     elif matrix[cur_y][cur_x] == 2: # 본인에 충돌
#         break
#     print(cur_x, cur_y)
#
#     # 이동 처리
#     matrix[cur_y][cur_x] = 2
#     snake.append((cur_x, cur_y))
#     cnt_frame += 1
#
#     for m in matrix:
#         print(m)
#     print(f"cnt_frame: {cnt_frame}")
#     print("=============")
