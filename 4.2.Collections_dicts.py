from sqlalchemy import true

config = {"model": "gtp-4",
          "temparature": 0.7,
          "max_tokens": 1000
          }
print(config)
print(config["model"])
config["stream"] = True
config["user"] = "Sharath"
del config["max_tokens"]
print(config)
for key, value in config.items():
    print(f"{key} : {value}")

print(config.get('notpresent', "Not Found"))

keys = ["Sharath", "Prakash", "Vinay"]
values = ["Python", "Java", "JS"]
print(zip(keys, values))
data = dict(zip(keys, values))
print(data)

for key, value in data.items():
    print(f"{key} : {value}")
