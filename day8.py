# Read both inputs and convert them to lowercase
str1 = input().lower()
str2 = input().lower()

# Compare strings and print the corresponding result
if str1 < str2:
    print(-1)
elif str1 > str2:
    print(1)
else:
    print(0)
