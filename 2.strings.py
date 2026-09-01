model = "gpt-4"
temp = 0.7
prompt = f"Using {model} with a temparature of {temp} to generate text"
system_prompt = """
                You are helpfull assistant
                Answer question based on the provided context
                If you dont know say No
               """

print(model)
print(temp)
print(prompt)
print(system_prompt)
