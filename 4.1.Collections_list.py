models = ["gpt-4", "claude", "gemini"]
print(models) #['gpt-4', 'claude', 'gemini']
print(models[0]) #gpt-4
print(models[-1]) #gemini
print(models[0:2]) #['gpt-4', 'claude']
print(models[1:]) #['claude', 'gemini']
print(models[:2]) #['gpt-4', 'claude']
models.insert(1, "Mistral")
print(models) #['gpt-4', 'Mistral', 'claude', 'gemini']
models.remove("claude")
print(models) #['gpt-4', 'Mistral', 'gemini']

poped = models.pop(2)  # pop the item at index 2
print(models) #['gpt-4', 'Mistral']
print(poped) #gemini