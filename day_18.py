# Read input values for n and k
n, k = map(int, input().split())
 
# Perform the operation k times
for _ in range(k):
    if n % 10 == 0:
        n //= 10  # Integer division to remove the last digit
    else:
        n -= 1    # Decrease the number by one
 
# Print the final result
print(n)
