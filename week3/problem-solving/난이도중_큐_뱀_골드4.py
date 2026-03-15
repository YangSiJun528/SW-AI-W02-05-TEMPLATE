# 문제: 큐 - 뱀 (백준 골드4)
# 링크: https://www.acmicpc.net/problem/3190
# AI 사용 횟수: 0
# AI 사용 방법: X
# 목표 시간: 30분
# 실제 시간: 18분 48초 - (이전에 1시간 30분동안 했었음. 코드도 재사용했음 감안하기)

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
# 걍 입력값 처리가 힘들었음. 16분 걸림;;;
#----------------
# 0부터 시작해야 하는데, 이미 요소가 하나 있는 1부터 시작하게 함. - 다시 보니까 cur_x랑 일치 안해서 실패했을 듯?
# 구현 시 순서를 잘못 생각함. - 이거는 구현 안해보면 상상하기 어렵긴 한데,
# 걍 구현이 빡셈. 1시간 30분 씀.
# 애매했던 부분(꼬리로 이동하면 꼬리 지워지는게 먼저임? 아님 이동하는게 먼저임?) 같은게 지문에 있었음.
# ---------------

# 3. 막힌 점 / 실수
# 그냥 지문 분석을 못했음. 코드에 그대로 넣으면 되었는데, 그냥 머릿속으로만 생각하고 작업하니까 구현이 꼬이고, 해결하는데 1시간 넘게 씀.
# 지문을 복붙해서 푸니까 20분 안에 품;;; (초기 세팅 시간 생각해서 첨부터 이렇게 했다 치면 40분 이내로 끝났음.)
# 지문 분석을 좀 하긴 했는데, 그냥 풀이가 나오거나 조건이 있으면 복붙해서 그걸 코드로 그대로 구현하도록 하는게 실수 없이 정확한 방법인듯?

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
# 지문: 뱀은 처음에 오른쪽을 향한다.
vector = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 앞으로 가면 오른쪽, 뒤로가면 왼쪽으로 꺽기
cnt_frame = 0
cmd_idx = 0
# 지문: 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다.
vector_idx = 0
snake.append((cur_x, cur_y))

# for m in matrix:
#     print(m)
# print(f"cnt_frame: {cnt_frame}")
# print("=============")

while True:

    # 지문: 뱀은 매 초마다 이동을 하는데...
    cnt_frame += 1

    # [HEAD 이동]

    # 지문: 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    v_x, x_y = vector[vector_idx]
    cur_x += v_x
    cur_y += x_y

    # 지문: 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
    if not (0 <= cur_x <= cnt_m-1 and 0 <= cur_y <= cnt_m-1): # 벽이랑 충돌
        break
    elif matrix[cur_y][cur_x] == 2: # 본인에 충돌
        break

    is_eat = False
    # 순서 상 이동 확정 전에 먼저 확인해야 함
    if matrix[cur_y][cur_x] == 1:
        is_eat = True

    # 충돌 안나면 이동한거 확정
    matrix[cur_y][cur_x] = 2
    snake.append((cur_x, cur_y))

    # [TAIL 이동]

    # 지문: 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    if is_eat:
        pass # 이동 처리 된 상태라 스킵
    else: # 지문: 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
        tail_x, tail_y = snake.popleft()
        matrix[tail_y][tail_x] = 0  # 사과 먹음

    # [이동 완료]

    # for m in matrix:
    #     print(m)
    # print(f"cnt_frame: {cnt_frame}")
    # print(f"snake: {len(snake)}")
    # print("=============")

    # 지문: 뱀의 방향 변환 정보가 주어지는데, ... 게임 시작 시간으로부터 "X초가 끝난 뒤에"
    if cmd_idx < len(cmds) and cmds[cmd_idx][0] == str(cnt_frame): # 명령어 실행 상태
        cmd = cmds[cmd_idx][1].strip()
        if cmd == 'D':
            vector_idx = 0 if vector_idx == 3 else vector_idx + 1
        else: # cmd == 'L':
            vector_idx = 3 if vector_idx == 0 else vector_idx - 1
        cmd_idx += 1
        #print(f"cmd:{cmd}, vector_idx:{vector_idx}")

print(cnt_frame)
