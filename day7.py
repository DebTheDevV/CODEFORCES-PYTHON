import sys

def solve():
    for r in range(5):
        # Read each row line and convert to integers
        row = list(map(int, sys.stdin.readline().split()))
        if 1 in row:
            c = row.index(1)
            # Center is at (2, 2) for 0-based indexing
            moves = abs(r - 2) + abs(c - 2)
            print(moves)
            return

if __name__ == '__main__':
    solve()
