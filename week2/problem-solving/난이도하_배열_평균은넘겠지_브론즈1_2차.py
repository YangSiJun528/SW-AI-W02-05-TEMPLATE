# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344
# ========================
# 풀이 완료까지 걸린 시간: 약 17분? 실수해서 타이머 안킴(구글링 시간 포함) / 30분
# 스터디모드 GPT 도움 횟수: 0
# 백준 사이트에서 풀었는가?: X -> 로직 확인 필요해서
# 구글링함.
#    1. https://firedino.tistory.com/56
#    2. https://soypablo.tistory.com/entry/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%97%90%EC%84%9C-%EA%B0%80%EC%9E%A5-%EC%9E%90%EC%84%B8%ED%95%9C-f-string-%EA%B0%80%EC%9D%B4%EB%93%9C
# 텍스트 포맷에 대한 사용법을 잘 모르겠음. 뭐 코테 시험을 준비하는거면 따로 외우겠지만,
#   일단 대충 f"{값:채울글자 정렬조건 최소채울크기 부동소수점표시}" 이정도만 알아두면 될 듯?
#   없거나 기본 속성을 쓸써면 안써도 됨.
#   예시 1: f"{12.34567:0>10.2f}" -> "0000012.35"
#   예시 2: f"{42:0>5}" -> "00042"
#   예시 3: f"{(0.4*100):0>8.3f}%" -> "0040.000%"
import sys

cnt = int(sys.stdin.readline().strip())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(cnt)]

for arr in matrix:
    std_cnt = arr[0]
    std_arr = arr[1:]
    avg_s = sum(std_arr) / std_cnt
    over_cnt = 0
    for s in std_arr:
        if s > avg_s:
            over_cnt += 1
    print(f"{(over_cnt/std_cnt*100):.3f}%")
