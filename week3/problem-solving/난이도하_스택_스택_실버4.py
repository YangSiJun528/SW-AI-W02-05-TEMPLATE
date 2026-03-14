# 문제: 스택 - 스택 (백준 실버 4)
# 링크: https://www.acmicpc.net/problem/10828
# AI 사용 횟수: 0
# AI 사용 방법: 사용안함
# 목표 시간: 30분
# 실제 시간: 6분 38초

# 1. 초기 접근
# 단순 스택인데, 입력에 따라 동작을 수행하면 됨. 2중 배열로 받아서 처리하면 됨.

# 2. 풀이 전략
# 접근 그대로 작업

# 3. 막힌 점 / 실수
# cnt를 int로 변환하는걸 까먹음.

# 4. 최종 코드
import sys

cnt = int(sys.stdin.readline().strip())
cmds = [sys.stdin.readline().split() for _ in range(cnt)]

stack = []

for cmd in cmds:
    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print('-1')
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if stack:
            print('0')
        else:
            print('1')
    elif cmd[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print('-1')