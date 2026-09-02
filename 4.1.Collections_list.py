models = ["gpt-4", "claude", "gemini"]
print(models)
print(models.append("llama"))
print(models)
print(models.insert(1, "mistral"))
print(models)
print(models[1:3])  # slice: items at index 1 and 2
models.remove("claude")
print(models)

poped = models.pop(3)  # pop the item at index 3
print(models)
print(poped)
