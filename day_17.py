# Read input values
k, n, w = map(int, input().split())

# Calculate total cost using the math formula
total_cost = k * (w * (w + 1)) // 2

# Output the borrowed money (returns 0 if total_cost - n is negative)
print(max(0, total_cost - n))

