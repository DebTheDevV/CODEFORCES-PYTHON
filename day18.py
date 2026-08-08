import sys

def solve():
    # Read string from standard input
    s = sys.stdin.read().strip()
    
    # Count uppercase and lowercase characters
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = len(s) - upper_count
    
    # Conditional formatting based on the character counts
    if upper_count > lower_count:
        print(s.upper())
    else:
        print(s.lower())

if __name__ == '__main__':
    solve()
