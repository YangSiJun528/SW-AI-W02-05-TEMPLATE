import sys

n = int(sys.stdin.readline().strip())
diag_size = 2 * n - 1

used_col = [False] * n
used_diag_rising = [False] * diag_size   # / 방향 (우상향)
used_diag_falling = [False] * diag_size  # \ 방향 (우하향)


def count_queens(row):
    if row == n:
        return 1
    result = 0
    for col in range(n):
        rising_idx = col - row + (n - 1)
        falling_idx = col + row
        if (not used_col[col]
                and not used_diag_rising[rising_idx]
                and not used_diag_falling[falling_idx]):
            used_col[col] = True
            used_diag_rising[rising_idx] = True
            used_diag_falling[falling_idx] = True
            result += count_queens(row + 1)
            used_col[col] = False
            used_diag_rising[rising_idx] = False
            used_diag_falling[falling_idx] = False
    return result

print(count_queens(0))
