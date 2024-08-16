"""Pre commit hook for updating version of frappe app"""


def add_one(number):
    """Adds one

    Args:
        number (_type_): _description_

    Returns:
        _type_: _description_
    """
    return number + 1


result = add_one(100)
print(result)
