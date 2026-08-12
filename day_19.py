def solve():
    n = int(input())
    result = []
    
    for i in range(1, n + 1):
        # Odd layers use "I hate", even layers use "I love"
        if i % 2 != 0:
            result.append("I hate")
        else:
            result.append("I love")
            
        # Connect layers with "that", or end with "it"
        if i < n:
            result.append("that")
        else:
            result.append("it")
            
    print(" ".join(result))

if __name__ == "__main__":
    solve()
