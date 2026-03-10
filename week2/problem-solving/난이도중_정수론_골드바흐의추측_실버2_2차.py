# ========================
# 풀이 완료까지 걸린 시간: 약 40분 (시간 넘음) / 30분
# 스터디모드 GPT 도움 횟수: 1
# 백준 사이트에서 풀었는가?: X
# ========================
# 사실 짝수 n의 경우 n/2인 두 수를 +,- 1씩하면 유지가 되니까. 그걸 primes랑 비교하면 되는거였음.
# 어차피 무조건 있다고 문제에서 설명해주니까 while로 해도 되고, 0, primes[-1] 넘어가는거 체크해도 되고...
# 지금 약간 계속 피곤한 상태라 머리가 안도는데, 투포인터로도 성공은 하긴 했네.
# 일단 성공하긴 했는데 방식이 좀 비효율적이였음. 접근법 자체는 문제 없었고.

import sys

cnt = int(sys.stdin.readline().strip())
nums = [int(sys.stdin.readline().strip()) for _ in range(cnt)]


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5)+1, 2):
        if n % i == 0:
            return False
    return True


primes = []
for n in range(10000):  # 10000은 미리 스킵
    if is_prime(n):
        primes.append(n)

for num in nums:
    l = 0
    target = num // 2
    while primes[l] < target:
        l += 1
    r = l
    if num % 2 == 1: # AI-1 : 이거 인풋이 항상 짝수라 필요 없음
        r += 1
    while r < len(primes) and l >= 0:
        if primes[l] + primes[r] == num:
            print(f"{primes[l]} {primes[r]}")
            break
        elif primes[l] + primes[r] < num:
            r += 1
        else:
            l -= 1
