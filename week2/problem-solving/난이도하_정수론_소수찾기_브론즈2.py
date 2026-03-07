# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978
import sys
import math

in_cnt = int(sys.stdin.readline().strip())
in_nums = list(map(int, sys.stdin.readline().split()))

rs = 0


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


for num in in_nums:
    if is_prime(num):
        rs += 1

print(rs)