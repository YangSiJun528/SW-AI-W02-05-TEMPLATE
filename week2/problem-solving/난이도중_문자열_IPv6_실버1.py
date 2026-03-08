# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107
# 딱히 시간 제한 없고 그냥 단순한 풀이 문제
# 문자열 다루는거라 관련 문법 사용법을 알면 풀 수 있음
import sys

arr = sys.stdin.readline().strip()
rs = []

if "::" in arr:
    cut = arr.split("::")
    l = cut[0].split(":")
    r = cut[1].split(":")

    len_l = len(l)
    len_r = len(r)

    i = 8 - (len_l + len_r)
    rs = l + i * ["0000"] + r
else:
    rs = arr.split(":")

for i in range(8):
    missed = 4 - len(rs[i])
    rs[i] =  '0' * missed + rs[i]

print(':'.join(rs))