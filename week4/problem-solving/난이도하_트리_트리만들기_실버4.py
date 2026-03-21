# 문제: 트리 - 트리 만들기 (백준 실버4)
# 링크: https://www.acmicpc.net/problem/14244
# AI 사용 횟수: 0
# AI 사용 방법: X - 대신 사람 도움 받음
# 목표 시간: 15분
# 실제 시간: 12분 - 의도 파악이 오래걸리네... 이게 하 난이도긴 한데, 15분은 어렵긴 한 듯. 30분으로 늘릴 예정

# 1. 초기 접근
# 이미 55분 쓰고 실패함. 자세한 사고 흐름은 1트_실패1 파일 참고
# n이 2 이상이므로 엣지 케이스는 고려 안해도 됨.

# 2. 풀이 전략
# 재귀를 사용.
# 종료조건: 만약 현재가 cnt 수만큼 같으면 중단
# 만약 현재의 노드 개수가 max_n - max_leaf 이면 반복해서 새 leaf 만들기
# 그렇지 않으면 leaf를 길게? 길이를 유지하기

# 3. 막힌 점 / 실수
# 유형: [접근법] [구현] [엣지케이스] [최적화]
#

# 4. 최종 코드
import sys

max_n, max_leaf = map(int, sys.stdin.readline().split())

def solution(cur_n_cnt, from_n, to_n):
    if cur_n_cnt == max_n - (max_leaf-1): # 왜냐면 이미 leaf가 하나 있으니까
        for i in range(max_n - cur_n_cnt):
            print(f"{from_n} {to_n+i}")
        return
    print(f"{from_n} {to_n}")
    solution(cur_n_cnt+1, to_n, to_n+1)

# n이 2이상이므로 cur_cnt가 2로 처리 가능 - 아니였으면 함수에서 조건문 필요 - 1개면 리프도 1개
solution(1, 0, 1)
