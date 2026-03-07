# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157
import sys

string = sys.stdin.readline().strip().upper()

memo = {}
m = (0, '')

for c in string:
    if c not in memo:
        memo[c] = 1
    else:
        memo[c] += 1

    if memo[c] > m[0]:
        m = (memo[c], c)

if list(memo.values()).count(m[0]) > 1:
    print('?')
else:
    print(str(m[1]).upper())