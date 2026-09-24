text = " Hello World "
print("hello".startswith("he"))
print(text)
print(text.strip())
print(text.lstrip())
print(text.rstrip())
print(text.upper())
print(text.lower())
print(text.title())
print(text.replace("Hello", "Hi"))
print("hello".startswith("she"))
print("ata" in "metadata")
print(",".join(["a", "b", "c"]))
print(list(map(str, [4, 2, 3])))
print(",".join(map(str, [4, 2, 3])))

numbers = [1, 2, 3]
result = map(str, numbers)
print(result)
print(list(result))


text = "aaaaabbbbbcccccddddddd"
# Code to remove the Duplicates from the string
print("".join(dict.fromkeys(text)))
#result = ""
#for char in text:
#    if char not in result:
#        result += char
#print(result)

count = {}

for char in text:
    count[char] = count.get(char, 0) + 1

for char, frequency in sorted(count.items(), key=lambda x: x[1], reverse=True):
    print(char, frequency)