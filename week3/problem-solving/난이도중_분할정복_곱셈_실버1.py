# 문제: 분할정복 - 곱셈 (백준 실버1)
# 링크: https://www.acmicpc.net/problem/1629
# AI 사용 횟수:
# AI 사용 방법:
# 목표 시간:
# 실제 시간:

# 1. 초기 접근
# 시간초가 0.5라서 시간복잡도 절반 잡아야 할 듯?
# 그리고 저거 int의 최대값만큼이면 복사를 엄청 많이 해야 함.
# 이게 내가 알기론 곱하고 나눈 수를 곱하고 나누고... 하면 되는걸로 아는데
# 이게 뭔 규칙이 있었나? 반복되는 경우가 있어서 이걸 뭐 어케 하면 되는건가?
# 5분 고민했는데 전혀 모르겠어서 GPT 힌트 요청 (알고리즘적 사고로 가능함? 걍 수학의 그 특징을 알아야 하나?)
# Exponentiation by Squaring (거듭제곱 분할정복)를 알아야 한다고 함.
# https://en.wikipedia.org/wiki/Exponentiation_by_squaring
# 찾아보니까 그대로 구현하면 될 듯?
# 이걸 몰랐으면 어차피 못 푸는 문제였네, 뭐 수학 사고가 좀 되는 사람이면 몰랐을지도.


# 2. 풀이 전략
#

# 3. 막힌 점 / 실수
# 추가로 모듈러 연산도 했어야 함.
# 그냥 gg 침. 이건 아닌거 같다.
# 답 제출도 안할 예정. 안푼걸로 치지 뭐.

# 4. 최종 코드
import sys
a, b, c = list(map(int, sys.stdin.readline().strip().split()))

# (a * b) % c == ((a % c) * (b % c)) % c

def exp_by_squaring(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        y = exp_by_squaring(x, n // 2)
        return (y * y) % c
    else: # n % 2 == 1:
        y = exp_by_squaring(x, n // 2)
        return (y * y * x) % c

print(exp_by_squaring(a, b))