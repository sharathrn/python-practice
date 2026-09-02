from sqlalchemy import false, true

config = {"model": "gtp-4",
          "temparature": 0.7,
          "max_tokens": 1000,
          "environment": {"dev": True, "prod": False},
          }
# print(config)
print(config["model"])
config["stream"] = True
config["user"] = "Sharath"
print(config)
del config["user"]
print(config)

# for key, value in config.items():
#    print(f"{key}: {value}")

print(config.get('notpresent', "Not Found"))

keys = ["sharath", "prakash", "vinay"]
values = ["Python", "Java", "C++"]
datalist = list(zip(keys, values))
print(datalist)
for key, value in datalist:
    print(f"{key}: {value}")

data = dict(zip(keys, values))
print(data)

for key, value in data.items():
    print(f"{key}: {value}")
