# 문제: 이분탐색 - 두 용액 (백준 골드5)
# 링크: https://www.acmicpc.net/problem/2470
# AI 사용 횟수: 2
# AI 사용 방법: 구현방식 힌트 - 런타임 에러 원인 힌트
# 목표 시간: 30분
# 실제 시간: 총 57분 - 30분 초과 + 15분 더 해보고 모르겠어서 힌트

# 1. 초기 접근
# N이 10^5임.
# 근데 최소값 구하는거니까 O(N^2)를 해야하는데 이건 불가능함.
# 그리고 가능한 N의 범위가 매우 큼.
# N의 목록이 제공되므로, 정렬 후 이진탐색으로 가장 합이 0 가까운 값을 찾고, 최소로 찾으면.
# 정렬 nlogn, 탐색 "logn을 N번" 탐색하니까 O(10^5)로 가능할 듯?

# 2. 풀이 전략
# 배열 저장 후 sort
# for로 n 반복
#   재귀로 이분탐색, l, r, n
#       if l,r의 인덱스가 같으면 해당 값이 n의 0에 가장 가깝게 하는 값이므로 최소값 여부 확인 후 처리
#.      n-mid가 0이면 그냥 찾았으니까 종료
#       n-mid가 0보다 작으면 left를 중간으로 이동
#       반대의 경우 right를 중간으로 이동
#       (틀렸음) ~~단, 이 경우 탐색이 아니라 경우를 줄이는거(찾는게 없을 수 있음)므로, mid +- 1씩하지 않아야 함~~

# 3. 막힌 점 / 실수
# 이거 재귀 반환 어케하더라? - 잠깐 햇갈림 - else로 base 아닌 상황에서 함수 호출 결과 리턴해주면 되었는데 까먹음
# mid +- 1씩 해주는게 맞음. mid를 기준으로 검사하니까. 안그러면 l:3, r:4에서 mid = (l+r)//2 하면 무한반복됨.
# 이분탐색 조건에서 i >= r로 넘어가는 경우도 고려했어야 함.
# 지문: "서로 다른 용액을 혼합" <<< 이거 안봤음...
# ----------------------
# 어려워서 GPT 도움 받음. 생각해보니까 그냥 끝에서 중간 될 때까지 옮겨가면서 작업했으면 됨.
# 이럼 이분탐색이 아닌데? 지금 방법도 불가능한건 아닌거 같긴 함.
# 근데 그냥 투포인터로 풀래...
# -------
# rs_min의 기본 값을 최댓값으로 설정해야 했는데, 이 조건을 잘못 적음. (분석을 잘못함)

# 4. 최종 코드
import sys

cnt = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split())) # 음수나 양수로만 된 경우도 있을 것

nums = sorted(nums)

l = 0
r = len(nums)-1
rs_l = None
rs_r = None
rs_min = (10**9 * 2) + 1 # 가능한 최댓값보다 1큼

while l != r:
    if rs_min > abs(nums[l] + nums[r]):
        rs_l = l
        rs_r = r
        rs_min = abs(nums[l] + nums[r])
    if nums[l] + nums[r] == 0:
        break
    elif nums[l] + nums[r] < 0:
        l += 1
    else: # nums[l] + nums[r] > 0:
        r -= 1
print(f"{nums[rs_l]} {nums[rs_r]}")

# 실패 1차
# import sys
#
# cnt = int(sys.stdin.readline().strip())
# nums = list(map(int, sys.stdin.readline().split())) # 음수나 양수로만 된 경우도 있을 것
#
# nums = sorted(nums)
#
# def find(l, r, n):
#     if (r - l) == 1:  # 서로 다른 상태여야만 하므로 인접해있으면 중단
#         return l, r
#     mid = (l+r)//2
#     if n + nums[mid] == 0:
#         return l, r
#     elif n + nums[mid] > 0:
#         return find(l, mid-1, n)
#     else: # n + nums[mid] < 0
#         return find(mid+1, r, n)
# rs_min = None # 따로 초기값 지정하기가 애매
# for num in nums:
#     l, r = find(0, len(nums)-1, num)
#     print(nums[l], nums[r])
#     if not rs_min:
#         rs_min = (nums[l], nums[r])
#     else:
#         if abs(sum(list(rs_min))) > abs(sum([nums[l], nums[r]])): #0에 가까워야 하니까 절댓값.
#             rs_min = (nums[l], nums[r])
#
# #print("--------------")
# print(f"{rs_min[0]} {rs_min[1]}")