import sys

def main():
    # Read the username from standard input
    username = sys.stdin.read().strip()
    
    # Calculate unique characters using a set
    distinct_count = len(set(username))
    
    # Print the result based on parity
    if distinct_count % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

if __name__ == "__main__":
    main()
