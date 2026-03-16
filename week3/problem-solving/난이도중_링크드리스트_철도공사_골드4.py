# 문제: 링크드리스트 - 철도 공사 (백준 골드4)
# 링크: https://www.acmicpc.net/problem/23309
# AI 사용 횟수: 1
# AI 사용 방법: 시간에러나서 접근법 확인
# 목표 시간: 30분
# 실제 시간: 1시간 20분

# 1. 초기 접근
# 이거 미리 푼 사람이 pypy로만 가능하다고 함.
# https://www.acmicpc.net/board/view/83348 를 보니까.
# 근데 이게 링크드리스트 문제이긴 한데, 시가나복잡도가 괜찮나?
# 뭐 추가 연산 횟수가 10^6이라 무조건 링크드리스트긴 함. 이거보다 더 빠르게 할 수도 없을거고.
# 뭐 해봐야 인덱스 접근을 쉽게 하기 위해 해시로 노드 링크하기?
# 이거 해야할거 같기도 하고... 이동 비효율이 너무 클 듯?
# 메모리 공간이 넉넉하기도 하니까 이걸로 속도 개선해야 할 거 같은데

# 2. 풀이 전략
# 일단 양뱡향 노드 필요
# 고유 번호로 O(1) 가능하게 해시맵 사용
# 클래스로 추상화한다는 식으로 가는게 나을 듯?

# 3. 막힌 점 / 실수
# 원형 구조인 점을 고려하지 않음.
# 해결하고 실행하니가 메모리 에러
# 아마 dict를 쓴게 원인이지 않을까... - 사실 위 링크에서 이 내용을 봤던거 같음.
# 시간 초과 왜 나는거
# ---
# 클래스 기반 링크드리스트를 버려야 함.
# 바꾸기 귀찮은데...

# 4. 최종 코드
import sys

_, cmd_cnt = list(map(int, sys.stdin.readline().split()))
subways = list(map(int, sys.stdin.readline().split()))
cmds = [list(sys.stdin.readline().split()) for _ in range(cmd_cnt)]

m_prev = [-1] * (10**6 + 1)
m_next = [-1] * (10**6 + 1)


class Subways:
    def BN(self, i, j):
        prev = i
        next = m_next[i]
        print(m_next[i])
        new_node = j
        m_prev[j] = prev
        m_next[j] = next
        m_next[prev] = new_node
        m_prev[next] = new_node

    def BP(self, i, j):
        prev = m_prev[i]
        next = i  # 곧 next 되니까?
        print(m_prev[i])
        new_node = j
        m_prev[new_node] = prev
        m_next[new_node] = next
        m_next[prev] = new_node
        m_prev[next] = new_node

    def CN(self, i):
        prev = i
        del_node = m_next[i]
        next = m_next[m_next[i]]
        print(del_node)
        m_next[prev] = next
        m_prev[next] = prev

    def CP(self, i):
        prev = m_prev[m_prev[i]]
        del_node = m_prev[i]
        next = i
        print(del_node)
        m_next[prev] = next
        m_prev[next] = prev

LL_subways = Subways()

ref = subways[0]
for idx in range(1, len(subways)):
    new = subways[idx]
    m_next[ref] = new
    m_prev[new] = ref
    ref = m_next[ref]
m_next[ref] = subways[0]
m_prev[subways[0]] = ref

for cmd in cmds:
    if cmd[0] == 'BN':
        LL_subways.BN(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'BP':
        LL_subways.BP(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'CN':
        LL_subways.CN(int(cmd[1]))
    else:  # cmd[0] == 'CP':
        LL_subways.CP(int(cmd[1]))

# 1차 실패
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#         self.prev = None
#
#
# class Subways:
#     def __init__(self):
#         self.memo = [None] * (10**6 + 1)
#         self.head = None
#         # 초기 세팅을 아래에서 함.
#         # self.head.next = self.tail
#         # self.tail.prev = self.head
#
#     def BN(self, node, j):
#         prev = node
#         next = node.next
#         print(next.val)
#         new_node = Node(j)
#         new_node.prev = prev
#         new_node.next = next
#         prev.next = new_node
#         next.prev = new_node
#         self.memo[int(j)] = new_node
#
#     def BP(self, node, j):
#         prev = node.prev
#         next = node  # 곧 next 되니까?
#         print(prev.val)
#         new_node = Node(j)
#         new_node.prev = prev
#         new_node.next = next
#         prev.next = new_node
#         next.prev = new_node
#         self.memo[int(j)] = new_node
#
#     def CN(self, node):
#         prev = node
#         del_node = node.next
#         next = node.next.next
#         print(del_node.val)
#         prev.next = next
#         next.prev = prev
#         del_node.next = None
#         del_node.prev = None
#         self.memo[int(del_node.val)] = None
#
#     def CP(self, node):
#         prev = node.prev.prev
#         del_node = node.prev
#         next = node
#         print(del_node.val)
#         prev.next = next
#         next.prev = prev
#         del_node.next = None
#         del_node.prev = None
#         self.memo[int(del_node.val)] = None
#
#
# LL_subways = Subways()
# LL_subways.head = Node(subways[0])
# LL_subways.memo[int(subways[0])] = LL_subways.head
#
# ref = LL_subways.head
# for idx in range(1, len(subways)):
#     new = Node(subways[idx])
#     ref.next = new
#     new.prev = ref
#     LL_subways.memo[int(subways[idx])] = new
#     ref = ref.next
# ref.next = LL_subways.head
# LL_subways.head.prev = ref
#
# for cmd in cmds:
#     if cmd[0] == 'BN':
#         LL_subways.BN(LL_subways.memo[int(cmd[1])], cmd[2])
#     elif cmd[0] == 'BP':
#         LL_subways.BP(LL_subways.memo[int(cmd[1])], cmd[2])
#     elif cmd[0] == 'CN':
#         LL_subways.CN(LL_subways.memo[int(cmd[1])])
#     else:  # cmd[0] == 'CP':
#         LL_subways.CP(LL_subways.memo[int(cmd[1])])
