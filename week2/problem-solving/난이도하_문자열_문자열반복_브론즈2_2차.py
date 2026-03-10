# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675
# ========================
# 풀이 완료까지 걸린 시간: 6분 44초 / 30분
# 스터디모드 GPT 도움 횟수: 0
# 백준 사이트에서 풀었는가?: X -> - 근데 실수 안했으면 바로도 가능했을 듯.
import sys

cnt = int(sys.stdin.readline().strip())
matrix = [list(sys.stdin.readline().split()) for _ in range(cnt)]

for r_cnt, string in matrix:
    for c in string:
        for i in range(int(r_cnt)):
            print(c, end='')
    print()
