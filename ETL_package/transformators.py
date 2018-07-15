from collections import OrderedDict


def aspiration_transform(aspiration: str) -> int:
    if aspiration.lower() == "turbo":
        return 1  # True

    return 0  # False


def horsepower_transform(horsepower: str) -> float:
    try:
        horsepower = float(horsepower.replace(",", "."))
    except Exception:
        raise ValueError("Incorrect horsepower value %s" % horsepower)

    return horsepower


def engine_location_transform(engine_location: str) -> int:
    engine_location_dict = {
        "front": 1,
        "rear": -1
    }
    result = engine_location_dict.get(engine_location.lower(), 0)
    if not result:
        raise ValueError("Incorrect engine_location value %s" % engine_location)

    return result


def num_of_cylinders_transform(num_of_cylinders: str) -> int:
    transform_table = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "severn": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12
    }

    result = transform_table.get(num_of_cylinders.lower(), None)
    if not result:
        raise ValueError("Incorrect number of cylinders %s" % num_of_cylinders)

    return result


def engine_size_transform(engine_size: str) -> int:
    try:
        return int(engine_size)
    except ValueError:
        raise ValueError("Incorrect engine_size value %s" % engine_size)


def weight_transform(weight: str) -> int:
    try:
        return int(weight)
    except ValueError:
        raise ValueError("Incorrect weight value %s" % weight)


def price_transform(price: str) -> float:
    try:
        float_price = float(price) / 100
        return round(float_price, 2)
    except ValueError:
        raise ValueError("Incorrect price value %s" % price)


def make_transform(make: str) -> str:
    return make.lower()


etl_interface = OrderedDict({})
etl_interface["engine-location"] = engine_location_transform
etl_interface["num-of-cylinders"] = num_of_cylinders_transform
etl_interface["engine-size"] = engine_size_transform
etl_interface["weight"] = weight_transform
etl_interface["horsepower"] = horsepower_transform
etl_interface["aspiration"] = aspiration_transform
etl_interface["price"] = price_transform
etl_interface["make"] = make_transform
