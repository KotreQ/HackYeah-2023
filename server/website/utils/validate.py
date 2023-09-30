class Validator:
    def __init__(self, *conditions):
        self.conditions = conditions

    def __call__(self, value):
        return all([condition(value) for condition in self.conditions])


def eq_type(type_):
    return lambda x: isinstance(x, type_)


def min_len(length):
    return lambda x: len(x) >= length


def max_len(length):
    return lambda x: len(x) <= length


def exact_len(length):
    return lambda x: len(x) == length


def uses_only(value_set):
    return lambda x: all(item in value_set for item in x)


def uses_any(required_set):
    return lambda x: any(required_item in x for required_item in required_set)
