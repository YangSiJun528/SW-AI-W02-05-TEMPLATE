# 문제: 링크드리스트 - 에디터 (백준 실버2)
# 링크: https://www.acmicpc.net/problem/1406
# AI 사용 횟수: 6
# AI 사용 방법: 코드 구현 틀린거 찾기
# 목표 시간: 30분 - 답 알긴 한데, 구현 시간이 좀 걸림.
# 실제 시간: 약 50분

# 1. 초기 접근
# 링크드리스트 안만들어도 되긴 한데, 연습 겸 직접 만들어보기

# 2. 풀이 전략
# 링크드리스트 만들고 풀이
# 하려다가 막혀서 다시

# 3. 막힌 점 / 실수
# 링크드리스트 전체를 만드는게 아니라 응용해서 풀었어야 함.
# get을 통해서 매번 찾으면 문제가 되기 때문임. 그냥 node에 대한 포인터가 있고 prev나 next에 바로 접근할 수 있어야 함.
# 이걸로 시간 많이 날렸고 구현도 잘 못 생각해서 시간 많이 날림

# 조건 명시를 잘 못해서 AI 도움을 많이 받음.
# 링크드리스트 템플릿 외우는 도중이라 그거 복붙하는데 시간 많이 씀.
# 문제 풀다가 멈추고 다시 했는데도 이정도 걸리는게 맞나.

# 4. 최종 코드
import sys

inputs = sys.stdin.readline().strip()
cmd_cnt = int(sys.stdin.readline().strip())
cmds = [sys.stdin.readline().split() for _ in range(cmd_cnt)]


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class LList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.tail.prev = self.head
        self.head.next = self.tail
        self.cur_node = self.tail

    def P_N(self, n):
        ref = self.cur_node
        prev = ref.prev
        new = Node(n)
        new.prev = prev
        new.next = ref
        ref.prev = new
        prev.next = new

    def L(self):
        if self.cur_node.prev != self.head:
            self.cur_node = self.cur_node.prev

    def D(self):
        if self.cur_node.next:
            self.cur_node = self.cur_node.next

    def B(self):
        if self.cur_node.prev == self.head:
            return
        ref = self.cur_node.prev
        next = ref.next
        prev = ref.prev
        next.prev = prev
        prev.next = next
        ref.next = None
        ref.prev = None


llist = LList()

for c in inputs:
    llist.P_N(c)

for cmd in cmds:
    if cmd[0] == 'P':
        llist.P_N(cmd[1])
    elif cmd[0] == 'L':
        llist.L()
    elif cmd[0] == 'D':
        llist.D()
    elif cmd[0] == 'B':
        llist.B()

rs = []
ref = llist.head.next

while ref != llist.tail:
    rs.append(ref.val)
    ref = ref.next

print("".join(rs))


# 잘못 했던 구현
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.prev = None
#         self.next = None
#
#
# class LList:
#     def __init__(self):
#         self.head = Node(None)
#         self.tail = Node(None)
#         self.tail.prev = self.head
#         self.head.next = self.tail
#         self.size = 0
#
#     def _get(self, idx):
#         if idx < (self.size // 2):
#             ref = self.head.next
#             for _ in range(idx):
#                 ref = ref.next
#         else:
#             ref = self.tail
#             for _ in range(self.size - idx):
#                 ref = ref.prev
#         return ref
#
#     def insert_at(self, idx, val):
#         ref = self._get(idx)
#         prev = ref.prev
#         new = Node(val)
#         new.prev = prev
#         new.next = ref
#         ref.prev = new
#         prev.next = new
#         self.size += 1
#
#     def delete_at(self, idx):
#         ref = self._get(idx)
#         next = ref.next
#         prev = ref.prev
#         next.prev = prev
#         prev.next = next
#         ref.next = None
#         ref.prev = None
#         self.size -= 1
#
#     def __len__(self):
#         return self.size
#
#
# cursor = 0
# llist = LList()
#
# for c in inputs:
#     llist.insert_at(cursor, c)
#     cursor += 1
#
# for cmd in cmds:
#     if cmd[0] == 'P':
#         llist.insert_at(cursor, cmd[1])
#         cursor += 1
#     elif cmd[0] == 'L':
#         if cursor > 0:
#             cursor -= 1
#     elif cmd[0] == 'D':
#         if cursor < len(llist):
#             cursor += 1
#     elif cmd[0] == 'B':
#         if cursor > 0:
#             llist.delete_at(cursor - 1)
#             cursor -= 1
#
# rs = []
# ref = llist.head.next
#
# while ref != llist.tail:
#     rs.append(ref.val)
#     ref = ref.next
#
# print("".join(rs))