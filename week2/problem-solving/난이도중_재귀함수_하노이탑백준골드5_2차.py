# ========================
# 풀이 완료까지 걸린 시간: 약 10분 / 30분
# 스터디모드 GPT 도움 횟수: 0
# 백준 사이트에서 풀었는가?: X
# 생각: 이건 재귀적 사고방식을 사용하면 금방 풀리긴 한다.
# ========================
import sys

n = int(sys.stdin.readline().strip())


def hanoi(n, from_idx, temp_idx, to_idx):
    if n == 0:
        return
    hanoi(n - 1, from_idx, to_idx, temp_idx)
    print(f"{from_idx} {to_idx}") # move - 이제 옮길 수 있음
    hanoi(n - 1, temp_idx, from_idx, to_idx)


print(2 ** n - 1)  # 외운 공식
if n <= 20:
    hanoi(n, 1, 2, 3)
