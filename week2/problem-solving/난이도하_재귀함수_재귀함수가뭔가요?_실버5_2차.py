# 재귀함수 - 재귀함수가 뭔가요? (백준 실버5)
# 문제 링크: https://www.acmicpc.net/problem/17478
# ========================
# 풀이 완료까지 걸린 시간: 6분 50초 / 30분
# 스터디모드 GPT 도움 횟수: 0
# 백준 사이트에서 풀었는가?: X -> 로직 확인 필요해서
# 지금 다시 풀면서 생각해보니, 재귀(or Tree)의 pre-order, post-order에 대한 개념을 소개하는게 의도가 아니였을까 싶음
import sys

cnt = int(sys.stdin.readline().strip())

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")


def recursion(n, max_n):
    print("____" * n, end='')
    print("\"재귀함수가 뭔가요?\"")
    if n == max_n:
        print("____" * n, end='')
        print("\"재귀함수는 자기 자신을 호출하는 함수라네\"")
    else:
        print("____" * n, end='')
        print("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
        print("____" * n, end='')
        print("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        print("____" * n, end='')
        print("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
        recursion(n + 1, max_n)
    print("____" * n, end='')
    print("라고 답변하였지.")

recursion(0, cnt)

