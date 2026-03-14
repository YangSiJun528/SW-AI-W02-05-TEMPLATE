# 문제: 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 링크: https://www.acmicpc.net/problem/9933
# AI 사용 횟수: 0
# AI 사용 방법:
# 목표 시간: 30분
# 실제 시간: 7분 52초

# 1. 초기 접근
# 그냥 해시로 뒤집어서 저장하고 있으면 찾아서 길이랑 중간 값 반환

# 2. 풀이 전략
# 접근대로 ㄱㄱ

# 3. 막힌 점 / 실수
# 회문(palindrome)의 경우 바로 맞은걸로 치는 엣지 케이스가 예시에 있었음에도 생각하지 않고 첫 예시만 보고 구현함.

# 4. 최종 코드
import sys

cnt = int(sys.stdin.readline().strip())
pwds = [sys.stdin.readline().strip() for _ in range(cnt)]

memo = {}

for pwd in pwds:
    if pwd not in memo:
        if pwd in pwd[::-1]:
            break
        else:
            memo[pwd[::-1]] = True # True는 중요하지 않음
    else:
        break

print(f"{len(pwd)} {pwd[(len(pwd)//2)]}")
