# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157
# ========================
# 풀이 완료까지 걸린 시간: 약 15분? (이것도 시간 놓침;) / 30분
# 스터디모드 GPT 도움 횟수: 0
# 백준 사이트에서 풀었는가?: X -> for문에서 dict.items() 가 필요한걸 까먹음. 실행해서 에러 보고 확인

# 방법 1. 전체 여러번 돌면서 구하기
# 방법 2. 미리 구하고 처리하기 - 가능은 한데 굳이?
# 10^6승이라 굳이 미리 안구해도 될 듯? N번 여러번 돌린다고 문제없어보임
import sys

string = sys.stdin.readline().strip().upper()

counter = {}
for c in string:
    if c not in counter:
        counter[c] = 1
    else:
        counter[c] = counter[c] + 1

max_char = ''
max_cnt = 0
used = False
for char, cnt in counter.items():
    if cnt > max_cnt:
        max_cnt = cnt
        max_char = char
        used = False
    elif cnt == max_cnt:
        used = True

if used:
    print("?")
else:
    print(max_char)
