# 문제: 링크드리스트 - 에디터 (백준 실버2)
# 링크: https://www.acmicpc.net/problem/1406
# AI 사용 횟수: 2
# AI 사용 방법: 스터디 모드, 구글링도 좀 함.
# 목표 시간: 15분 (답 알고, 시간 타이머 잘못 재서 줄임.)
# 실제 시간: X - 중간에 몇 시간동안 냅두고 풀어서 중단.

# 1. 초기 접근
# 이거 이시원님 도와주면서 이미 읽어버려가지고 목표 시간 10분 줄이고 보는게 좋을 듯?

# 2. 풀이 전략
# 스택 2개로 커서 왼/오른쪽 표현하거나 양방향 링크드리스트로 구현 가능.

# 3. 막힌 점 / 실수
# Linked List 구현 햇갈려서 GPT 힌트좀 받음. -> 더미 헤드/테일 노드를 쓸 때 조건 검사 쓰는법. 객체는 `__eq__()` 안바꾸면 동일 참조만 포함한다 함.
# Linked List 구현 실수 - 더미가 구현이 편하긴 한데... 약간 햇갈림.
# 메서드에 인자에 self 쓰는거, 본인 함수 호출에 self 붙이는거
# enumerate 사용법 햇갈려서 구글링

# 4. 최종 코드
# import sys
#
# inputs = sys.stdin.readline().strip()
# cmd_cnt = int(sys.stdin.readline().strip())
# cmds = [sys.stdin.readline().slice() for _ in range()]
#
#
# class Node:
#     def __init__(val):
#         self.val = val
#         self.prev = prev
#         self.next = next
#
#
# class LList:
#     def __init__():
#         # 더미 세팅 - 검사 편하게 하기 위함.
#         self.head = Node(None)
#         self.tail = Node(None)
#
#         self.head.next = self.tail
#         self.tail.prev = self.head
#
#     def insert_at(idx, val):
#         new_node = Node(val)
#
#         cur = _get(idx)
#
#         new_node.next = cur
#         new_node.prev = cur.prev
#
#         cur.prev.next = new_node
#         cur.prev = new_node
#
#     def del_at(idx):
#         cur = _get(idx)
#
#         cur.prev.next = cur.next
#         cur.next.prev = cur.prev
#
#         # 없어도 외부에서 접근 못해서 GC 대상이지만 명확하게
#         cur.prev = None
#         cur.next = None
#
#     def _get(idx):
#         cur = self.head.next  # head는 더미므로 next부터 시작
#         for _ in range(idx):
#             cur = cur.next
#         return cur
#
#
# llist = LList()
#
# for i, c in enumerate(inputs):
#     insert_at(i, c)
#
# cursur_idx = i  # 파이썬에선 i는 for 바깥에서도 접근 가능
#
# for cmd in cmds:
#     if cmd[0] == 'P':
#
#
