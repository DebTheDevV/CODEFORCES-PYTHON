import sys

def main():
    # Read input string directly
    s = sys.stdin.read().strip()
    
    # Count occurrences of '4' and '7'
    lucky_count = sum(1 for char in s if char in ('4', '7'))
    
    # Verify if the count itself is a lucky number
    if lucky_count == 4 or lucky_count == 7:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
