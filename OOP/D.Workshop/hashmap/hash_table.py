class HashTable:

    def __init__(self):
        self.__max_capacity = 4
        self.__keys = [None] * self.__max_capacity
        self.__values = [None] * self.__max_capacity

    def __getitem__(self, key):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            raise KeyError(f"\"{key}\" key not found!")

    def __setitem__(self, key, value):
        if key in self.__keys:
            index = self.__keys.index(key)
            self.__values[index] = value
            return

        if len(self) == self.__max_capacity:
            self.__resize()

        index = self.__calc_index(key)
        index = self.__get_index(index)

        self.__keys[index] = key
        self.__values[index] = value

    def __calc_index(self, key):
        return sum(ord(c) for c in key) % self.__max_capacity

    def __get_index(self, index):
        if index == self.__max_capacity:
            index = 0

        if self.__keys[index] is None:
            return index

        return self.__get_index(index + 1)

    def __resize(self):
        self.__keys = self.__keys + [None] * self.__max_capacity
        self.__values = self.__values + [None] * self.__max_capacity
        self.__max_capacity *= 2

    def __len__(self):
        return len([k for k in self.__keys if k is not None])

    def add(self, key, value):
        self[key] = value

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def get_representation(self):
        print("{", end="")

        for i in range(self.__max_capacity):
            key = self.__keys[i]

            if key is not None:
                print(f"{key}: {self.__values[i]},", end=" ")

        print("}")


table = HashTable()

table["name"] = "Peter"
table["name"] = "Dimitar"
table["age"] = 16
table["is_pet_owner"] = True
table["is_driver"] = False

table.add("a", "A")

print(table.get("b", "This is not a valid key"))

table.get_representation()

print(table)
print(table.get("name"))
print(table["age"])
print(len(table))
