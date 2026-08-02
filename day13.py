import sys

def main():
    # Read integer input from standard input
    x = int(sys.stdin.read().split()[0])
    
    # Calculate the minimum number of steps
    steps = (x + 4) // 5
    
    print(steps)

if __name__ == "__main__":
    main()
