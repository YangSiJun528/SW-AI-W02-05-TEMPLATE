# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562
#nums = [3, 29, 38, 12, 57, 74, 40, 85, 61]
nums = [int(input()) for _ in range(9)]

max_num = 0
cnt = 0
max_cnt = 0

for num in nums:
    cnt = cnt + 1
    if num > max_num:
        max_num = num
        max_cnt = cnt

print(max_num)
print(max_cnt)
