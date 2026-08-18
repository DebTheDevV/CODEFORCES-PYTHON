# Read both string inputs
s = input().strip()
t = input().strip()

# Check if s matches the reversed version of t
if s == t[::-1]:
    print("YES")
else:
    print("NO")
