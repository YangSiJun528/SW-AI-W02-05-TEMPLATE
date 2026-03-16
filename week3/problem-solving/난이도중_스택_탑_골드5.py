# 문제: 스택 - 탑 (백준 골드5)
# 링크: https://www.acmicpc.net/problem/2493
# AI 사용 횟수: 0
# AI 사용 방법: X
# 목표 시간: 30분
# 실제 시간: 25분 29초 - 1트 성공 ㅅㅅㅅㅅ

# 1. 초기 접근
# 높이는 int, n은 10^5 * 5인데, nlogn으로 풀라는 소리.
# 그냥 단순하게 뒤에서부터 가능한걸 찾는 브루스포트는 최악의 경우 n^2가 될 수 있음.
# 다른 대안이 필요.
# 스택 혹은 큐를 사용하여 풀 수 있는가? 스택 문제니까 이거랑 묶어서 생각해보자
# 부딪히지 않은 상태라면 항상 이전보다 낮은 위치일 것.
# 따라서 어딘가에 부딪힌다면, 처음에 추가된 건 부딪히지만, 이전에 추가된건 더 낮아서 안부딪힐 수 있음.
# 따라서 stack peek하다가 안 부딪힐때까지 복구하면 됨.

# 2. 풀이 전략
# 결과 출력할 배열 선언 - rs라고 부름
# stack 선언
# 역순으로 읽기
# 만약 stack에서 peek했는데 더 높은 위치면 pop하면서 rs에 값 넣기

# 3. 막힌 점 / 실수
# 딱히 없음

# 4. 최종 코드
import sys

cnt = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))

stack = []
rs = [0] * cnt

for i in range(len(nums)-1, -1, -1):
    #print(i)
    while stack and stack[-1][0] < nums[i]: # 스택 맨 위꺼랑 부딪히면
        num, idx = stack.pop()
        rs[idx] = i + 1 # 탑 번호라 idx에서 1 추가
    stack.append((nums[i], i))

print(" ".join(map(str, rs)))

