# Read the initial weights of Limak (a) and Bob (b)
a, b = map(int, input().split())

years = 0

# Loop runs as long as Limak is less than or equal to Bob
while a <= b:
    a *= 3      # Limak's weight triples
    b *= 2      # Bob's weight doubles
    years += 1  # Increment the year counter

# Print the final result
print(years)
