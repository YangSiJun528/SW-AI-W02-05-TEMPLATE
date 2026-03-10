# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562
# ========================
# 풀이 완료까지 걸린 시간: 4분 30초 / 30분
# 스터디모드 GPT 도움 횟수: 0
import sys

nums = [int(sys.stdin.readline().strip()) for _ in range(9)]

max_n = -1
max_idx = -1
for i in range(9):
    if max_n < nums[i]:
        max_n = nums[i]
        max_idx = i

print(max_n)
print(max_idx + 1)


