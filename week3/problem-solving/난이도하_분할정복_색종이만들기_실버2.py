# 문제: 분할정복 - 색종이 만들기 (백준 실버2)
# 링크: https://www.acmicpc.net/problem/2630
# AI 사용 횟수: 2
# AI 사용 방법: 클로드한테 구현 실수 물어봄
# 목표 시간: 30분
# 실제 시간: 37분

# 1. 초기 접근
# 일단 한 번에 4개의 분기로 나뉘어지는 재귀로 구현 가능할 듯?
# 이걸 어떻게 4개로 나누는지 공식을 구해야 하고
# 그 범위의 요소가 같은 색인지 확인하고 아니면 계속 분기하면 됨.
# N은 가로/세로 길이인데, 항상 짝수고, 2부터 128까지 커버할 수 있는 함수여야 함.

# 2. 풀이 전략
# 일단 매트릭스를 저장하고, s_y,s_x, e_y,e_x를 호출
# 만약 모든 범위가 동일한 색이면 색상에 따라 (흰, 파)로 숫자 넣어서 반환 - base case
# 올라오면서 값 합치고 리턴된 튜플 값 출력

# 3. 막힌 점 / 실수
# 시작/종료 -  x,y 따로 해서 4가지 조합인데, 그냥 시작,종료로 가능할 줄 알았음.
#   이거 시간 8분정도 남았는데, 시간 넘는건 확정이고, 일정 있어서 중단해야 함. 구현법은 확실하다 생각해서 이어서 쭉 해볼 예정.
# 이거 너무 네이밍이 복잡하고, 2차 배열 다루는게 익숙하지 않아서 AI 도움받아서 해결함. 접근 자체는 틀리진 않았음.

# 4. 최종 코드
import sys

cnt = int(sys.stdin.readline().strip())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(cnt)]

# for m in matrix:
#     print(m)

def folding(matrix, row_start, row_end, col_start, col_end):
    card = [m[row_start:row_end] for m in matrix[col_start:col_end]]
    full_count = len(card) ** 2
    if sum([sum(c) for c in card]) == full_count:
        return (0, 1)
    elif sum([sum(c) for c in card]) == 0:
        return (1, 0)

    mid_r = (row_start + row_end) // 2
    mid_c = (col_start + col_end) // 2

    w1, b1 = folding(matrix, row_start, mid_r, col_start, mid_c)  # 좌상
    w2, b2 = folding(matrix, row_start, mid_r, mid_c, col_end)  # 우상
    w3, b3 = folding(matrix, mid_r, row_end, col_start, mid_c)  # 좌하
    w4, b4 = folding(matrix, mid_r, row_end, mid_c, col_end)  # 우하

    return (w1+w2+w3+w4, b1+b2+b3+b4)

w, b = folding(matrix, 0, cnt, 0, cnt)
print(w)
print(b)


# 구현 확인용 테스트용
# for m in matrix:
#     print(m)
#
# def folding(matrix, s, e):
#     print([m[s:e] for m in matrix[s:e]])
#
# folding(matrix, 0, cnt//2)
