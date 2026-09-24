numbers = [1, 2, 3, 4, 5]
print(numbers)
squares = [number**2 for number in numbers]
print(squares)
even = [number for number in numbers if number % 2 == 0]
print(even)

word_lengths = {w: len(w) for w in ["hi", "world"]}
print(word_lengths)
