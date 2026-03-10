# ========================
# 풀이 완료까지 걸린 시간: 21분 / 30분
# 스터디모드 GPT 도움 횟수: 0
# 백준 사이트에서 풀었는가?: X

import sys

in_ipv6 = sys.stdin.readline().strip()

arr = []

if "::" in in_ipv6:
    temp = in_ipv6.split("::")

    l_ip = temp[0].split(":")
    r_ip = temp[1].split(":")
    remaining = 8 - (len(l_ip) + len(r_ip))
    arr = l_ip + remaining * ['0000'] + r_ip
else:
    a_ip = in_ipv6.split(":")
    for i in range(len(a_ip)):
        arr.append(a_ip[i])


for i in range(len(arr)):
    remaining = 4 - len(arr[i])
    arr[i] = '0' * remaining + arr[i]

print(":".join(arr))
