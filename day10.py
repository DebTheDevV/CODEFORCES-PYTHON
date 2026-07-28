import sys

def main():
    # Read input string
    s = sys.stdin.read().strip()
    
    # Split by '+', sort the numbers, and join them back with '+'
    numbers = s.split('+')
    numbers.sort()
    
    # Print the sorted result
    print('+'.join(numbers))

if __name__ == '__main__':
    main()
