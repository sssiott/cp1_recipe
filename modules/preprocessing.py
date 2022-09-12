def preprocessing(dict):
    import re
    comp = re.compile('.?\d')

    for key, value in dict.items():
        for i in range(len(value)):
            if comp.match(value[i:]) is not None:
                continue
            else:
                dict[key] = value[:i], value[i:]
                break


def load_db(li):
    pass