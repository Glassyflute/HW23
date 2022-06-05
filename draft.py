if cmd == "sort":
    value = bool(value)
    sorting_key = map(lambda x: x.split(" ")[0].split(".")[0], result)
    result = sorted(result, key=sorting_key, reverse=value)

