import sys

def main():
    # Read the number of games played
    n = int(sys.stdin.readline().strip())
    # Read the string representing outcomes
    s = sys.stdin.readline().strip()
    
    # Count the wins for each player
    anton_wins = s.count('A')
    danik_wins = s.count('D')
    
    # Determine and print the result
    if anton_wins > danik_wins:
        print("Anton")
    elif danik_wins > anton_wins:
        print("Danik")
    else:
        print("Friendship")

if __name__ == '__main__':
    main()
