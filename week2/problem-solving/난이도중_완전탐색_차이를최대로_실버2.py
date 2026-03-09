# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819
# 이거 0부터 시작하는 순열 구하고, 그걸 idx라고 치고 처리하면 될 듯?
# 순열 생성 시간복잡도는 보통 O(N * N!)
# 순열 개수가 N!이고, 각 순열마다 길이 N만큼 처리해야 하기 때문.
# 자리수가 짧으면 더 줄어들지만(이건 어케구하는지 까먹음), 여기선 인덱스라 N임.
# ------------------------
# 재귀를 너무 많이 쓴 듯? 하나 끝나면 바로 계산 들어가야 하는게 좋을듯. 메모리 제한 공간 넘어갈거 같음
# 그리고 보니까 순열이 인덱스로 써야하는데 안하고 있었고
# remaining 조건도 잘못되었고
# 최댓값인데 최소값 보고 있었음.
# 문제 정의도 잘못함 --- 아.........
# ------------------------
# 순서를 바꾸는 수열을 만들고 그걸 기반으로 처리한다는 접근법 자체는 올바른거 같음.
# 아 |가 이거 걍 구분자가 아니라 절댓값 구하라는거구나??? 아니문제를자세히안보네왜이럴까
import sys

cnt = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

def permutation(path, remaining):
    if not remaining:
        temp = 0
        for i in range(1, len(path)):
            raw_num = (arr[path[i-1]] - arr[path[i]])
            if raw_num < 0: # abs(raw_num) 써도 가능
                temp -= raw_num
            else:
                temp += raw_num
        return temp
    rs = 0
    for i in range(len(remaining)):
        next_path = path + [remaining[i]]
        next_remaining = remaining[:i] + remaining[i+1:]
        rs = max(permutation(next_path, next_remaining), rs)
    return rs

print(permutation([], list(range(cnt))))


# 실패 2. 문제 정의 잘못함
# def permutation(path, remaining):
#     if not remaining:
#         temp = []
#         if cnt % 2 == 1:
#             path.append(0)  # 처리엔 영향 없는데 값 2개씩 처리하기 편하게 하기 위함 - 이미 순열 구한 상태니까 가공해도 ㄱㅊ
#         for i in range(0, len(path), 2):
#             temp.append(arr[path[i]] - arr[path[i+1]])
#         return sum(temp)
#     rs = 0
#     for i in range(len(remaining)):
#         next_path = path + [remaining[i]]
#         next_remaining = remaining[:i] + remaining[i+1:]
#         rs = max(permutation(next_path, next_remaining), rs)
#     return rs


# 실패 1. 재귀가 너무 깊고, 메모리 문제 발생.
# def permutation(path, remaining):
#     if not remaining:
#         permutations.append(path)
#         return
#     for i in range(len(remaining)):
#         next_path = path + [remaining[i]]
#         next_remaining = remaining[:i + 1] + remaining[i:]
#         permutation(next_path, next_remaining)
#
# permutation([], list(range(cnt)))
#
# rs = 10 ** 8  # 대충 큰 값
# for permutation in permutations:
#     temp = []
#     if cnt % 2 == 0:
#         permutation.append(0)  # 처리엔 영향 없는데 값 2개씩 처리하기 편하게 하기 위함
#     for i in range(0, len(permutation), 2):
#         temp.append(permutation[i] - permutation[i + 1])
#     rs = min(sum(temp), rs)
# print(rs)
