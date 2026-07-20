import sys
 
def solve():
    # Read all lines from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    x = 0
    
    # Process each statement
    for i in range(1, n + 1):
        if '+' in input_data[i]:
            x += 1
        else:
            x -= 1
            
    print(x)
 
if __name__ == '__main__':
    solve()