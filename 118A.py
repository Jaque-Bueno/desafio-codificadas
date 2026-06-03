word = input().lower()

result = ""

for char in word:
    if char not in "aoyeui":
        result += "." + char

print(result)
