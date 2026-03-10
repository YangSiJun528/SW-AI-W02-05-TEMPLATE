# ========================
# 풀이 완료까지 걸린 시간: 약 40분 (시간 넘음) / 30분
# 스터디모드 GPT 도움 횟수: 1 - 구현 실수 약간 있었음. 
# 백준 사이트에서 풀었는가?: X
# ========================
import sys

in_cnt = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))


def permutation(path, remaining):
    if len(path) == len(arr):
        return [path[:]]
    rs = []
    for i in range(len(remaining)):
        next_path = path + [remaining[i]]
        next_remaining = remaining[:i] + remaining[i + 1:]
        rs.extend(permutation(next_path, next_remaining))
    return rs


idx_sets = permutation([], list(range(in_cnt)))
#print(idx_sets)

max_n = 0
for idx_set in idx_sets:
    temp = 0
    for i in range(len(idx_set) - 1):
        temp += abs(arr[idx_set[i]] - arr[idx_set[i + 1]])
    max_n = max(max_n, temp)
print(max_n)

