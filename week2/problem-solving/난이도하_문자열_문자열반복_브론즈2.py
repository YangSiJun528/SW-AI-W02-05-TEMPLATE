# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675
import sys

cnt = int(sys.stdin.readline().strip())
matrix = [list(sys.stdin.readline().split()) for _ in range(cnt)]

for i, string in matrix:
    for c in string:
        print(c*int(i), end='')
    print()
