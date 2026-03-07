# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344
import sys

cnt = int(sys.stdin.readline().strip())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(cnt)]

for i in range(cnt):
    s = matrix[i][1:]
    avg_n = sum(s) / len(s)

    cnt_n = 0
    for ss in s:
        if ss > avg_n:
            cnt_n = cnt_n + 1
    print("%.3f%%" % ((cnt_n / len(s)) * 100))  # 이건 텍스트 포맷하는법 몰라서 찾아봄.