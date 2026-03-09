# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914
# ========================
# https://gist.github.com/YangSiJun528/5e2a7c120bcc1c2e8d4ef3d915cf8e0c
# 이거 쓴 직후 바로 작성.
# 실패 한번 함.
# move 카운트를 세어줘야 하는데 그게 아니라 끝났을 때도 세서 그랬던거 같음.
# 뭐 일단 성공? 인줄 알았는데, 20 넘어가는 경우엔 성능이 빡세서 어쩔 수 없는듯.
# 이건 모르겠어서 찾아보니까 (2**n)-1 이 최소 이동 횟수라고 함. 이러면 20넘어가면 계산 안해도 됨.
# 비트시프트를 쓰면 (n<<1)-1로도 가능.
# 이걸 의도한거 같긴 한데... 알려주려고 하는거면 좋은데...

import sys

num = int(sys.stdin.readline().strip())

def move(from_i, to_i, p_flag):
    if p_flag:
        print(from_i, to_i)
    return 1

def hanoi(n, from_i, temp_i, to_i, p_flag):
    if n == 0:
        return 0

    b_cnt = hanoi(n - 1, from_i, to_i, temp_i, p_flag)
    m_cnt = move(from_i, to_i, p_flag)
    a_cnt = hanoi(n - 1, temp_i, from_i, to_i, p_flag)
    return b_cnt + m_cnt + a_cnt

print((2**num)-1)
if num <= 20:
    hanoi(num, 1, 2, 3, True)

# 실패
# 타임아웃 에러남
# 1개로 줄여야 할 듯?
# # 의미적으론 필요한데, 없어도 됨
# def move(from_i, to_i, p_flag):
#     if p_flag:
#         print(from_i, to_i)
#
#
# def hanoi(n, from_i, temp_i, to_i, cnt, p_flag):
#     if n == 0:
#         return 1
#
#     b_cnt = hanoi(n - 1, from_i, to_i, temp_i, cnt, p_flag)
#     move(from_i, to_i, p_flag)
#     a_cnt = hanoi(n - 1, temp_i, from_i, to_i, cnt, p_flag)
#     return b_cnt + a_cnt
#
# print(hanoi(num, 1, 2, 3, 0, False)-1) # 어째서 -1을 해줘야 하는걸까...
# hanoi(num, 1, 2, 3, 0, True)