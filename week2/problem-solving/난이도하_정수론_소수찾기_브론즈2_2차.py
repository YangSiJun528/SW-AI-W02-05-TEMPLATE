# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978
# ========================
# 풀이 완료까지 걸린 시간: 17분 16초 / 30분
# 스터디모드 GPT 도움 횟수: 0
# 백준 사이트에서 풀었는가?: X -> 타입에러나 Attribute 에러났어서 디버깅용.
# 주의점: 소수 판별할 때 2 나누는걸 까먹음. 아직 완전하게 외우지 못한 듯?
#        아니면 소수 규칙 생각을 안하고 구현을 외우는게 문제일수도 있고.
import sys

cnt = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2): # math.sqrt() 대체
        if n % i == 0:
            return False
    return True

rs = 0
for num in nums:
    if is_prime(num):
        rs += 1
print(rs)
