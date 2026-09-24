def flexible(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")


flexible(1, 2, 3, name="Alice", age=30, city="New York")
