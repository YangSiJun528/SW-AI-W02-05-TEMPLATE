# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020
# =====================
# 분석, 숫자 당 10^4의 시간 복잡도를 가짐.
# O(N^2) 시간 복잡도까지는 OK
# prime 구하는게 최악의 경우 O(sqrt(N)) 정도
# 모든 prime을 구하려면 (O(N) + O(sqrt(N))) 정도 소요됨.
#   모든 수를 반복하면서 prime 구하는 연산을 수행하므로
# 모든 prime 수에 대해서 다른 후보 수를 구하는 연산은 O(N^2)
# 약간 더 나은 방법이 있을수도? 총 O(N^2)이면 좀 위험한데...
# 일단 시도 ㄱㄱ
# =======================
# 코드 작성하다가 생각난게, 인풋 범위만큼 미리 prime 수 계산하면 더 효율적일듯 - N이 10^4이하라서
# 그리고 가장 가까운 수라서 중간에서 prime 배열을 인덱스 값 2개로 범위 번갈아 늘려가면서 구하면 됨.
# ========================
# 뭔가 더 나은 해결책이 있을거 같아서 AI랑 스터디모드로 이야기하다가 거의 정답이 나와버림...
# 위 방법도 가능하긴 했을 듯? 근데 그냥 prime 표를 만들고, 수 중간에서 +, -하면서 둘 다 소수인 값을 구혀면 됨.

import sys

cnt = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(cnt)]

primes = set([])
for n in range(10000): # 10000은 어차피 소수 아니니까
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.add(n)

for num in arr:
    l = num//2
    r = num//2
    while l >= 0 or r <= num:
        if l in primes and r in primes and l + r == num:
            print(f'{l} {r}')
            break
        r += 1
        l -= 1
