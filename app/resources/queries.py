def insert_query(name: str, size: int, calories: int) -> str:
    # "My name is {}, I'm {}".format("John",36)
    return "INSERT INTO foodtable (food, serving_size, calories) VALUES (\'{}\', {}, {});".format(str(name), int(size), int(calories))


selectAllFromFoodTable = "SELECT * FROM foodtable"
