# 문제: 이분탐색 - 수 찾기 (백준 실버4)
# 링크: https://www.acmicpc.net/problem/1920
# AI 사용 횟수:
# AI 사용 방법:
# 목표 시간: 30분
# 실제 시간: 12분 28초

# 1. 초기 접근
# 딱 봐도 이진 탐색이면 잘 풀릴듯 함.
# 근데 정렬이 되어있어야 하는데, 이걸 직접 구현하라는건 아닌거 같지?
# 10^6이니까 nlogn으로 풀이 가능.
# -2^31~2^31 이니까 4byte 자료형으로 풀라는 말이고

# 근데 해시 써도 되긴 함. 이게 더 편한데, 의도는 이진 탐색이니까 그걸로 풀기.

# 2. 풀이 전략
# 정렬은 기본 함수, 이진 탐색으로 찾아서 처리
# 뒤에는 순차적으로 돌면서 이진탐색하면 됨.

# 3. 막힌 점 / 실수
# 이분탐색 조건 <= 인데 <로 잘못 씀.

# 4. 최종 코드
import sys

arr_cnt = int(sys.stdin.readline().strip()) #이거 필요한가?
arr = list(map(int, sys.stdin.readline().split()))
find_cnt = int(sys.stdin.readline().strip()) #이거 필요한가?
find_inputs = list(map(int, sys.stdin.readline().split()))

arr = sorted(arr)

for input in find_inputs:
    l = 0
    r = len(arr)-1
    found = False
    while l <= r:
        cur = (l + r)//2
        if input == arr[cur]:
            found = True
            break
        elif input < arr[cur]:
            r = cur - 1
        else:
            l = cur + 1
    print(1 if found else 0)


