def value_in_list_of_dicts(value_to_find, list_of_dicts):
    for d in list_of_dicts:
        if value_to_find in d.values():
            return True
    return False


def key_in_list_of_dicts(key_to_find, list_of_dicts):
    for d in list_of_dicts:
        if key_to_find in d:
            return True
    return False


def str_to_bool(s):
    if s.lower() in ["true", "1", "t", "y", "yes"]:
        return True
    elif s.lower() in ["false", "0", "f", "n", "no"]:
        return False
    else:
        raise ValueError(f"Invalid truth value: {s}")
