text = " Hello World "
print(text)
print(text.lstrip())
print(text.rstrip())
print(text.strip())
print(text.strip().replace("Hello", "Hi"))
print(text.split())
print("hello".startswith("he"))
print("ata" in "metadata")
print(",".join(["a", "b", "c"]))

print("|".join(map(str, [1, 2, 3])))

numbers = [1, 2, 3]
result = map(str, numbers)
print(list(result))
