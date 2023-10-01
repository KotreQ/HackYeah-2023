class Validator:
    def __init__(self, *conditions):
        self.conditions = conditions

    def __call__(self, value):
        return all([condition(value) for condition in self.conditions])


class ObjectValidator:
    def __init__(self, validators_dict):
        for attr_name, attr_validator in validators_dict.items():
            if not isinstance(attr_name, str):
                raise TypeError(
                    f"attr_name must be a string, instead got: {attr_name!r}"
                )
            if not isinstance(attr_validator, Validator):
                raise TypeError(
                    f"attr_validator must be a Validator, instead got: {attr_validator!r}"
                )
        self.validators_dict = validators_dict

    def __call__(self, obj_value):
        for attr_name, attr_validator in self.validators_dict.items():
            attr_value = getattr(obj_value, attr_name, None)
            if not attr_validator(attr_value):
                return False
        return True


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
