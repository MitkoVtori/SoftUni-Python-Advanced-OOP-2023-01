class Inventory:

    def __init__(self, *args):
        self.__inventory = {}
        self.__negative_indexes = {}

        for index, item in enumerate(args):
            self.__inventory[index] = item

        for index, item in enumerate(args[::-1]):
            index -= (1 + index + index)
            self.__negative_indexes[index] = item

    def __getitem__(self, index):
        try:
            if index < 0:
                return self.__negative_indexes[index]
            return self.__inventory[index]
        except KeyError:
            raise IndexError("Index out of range!")

    def __get_last_index(self):
        return len(self.__inventory) - 1

    def __append_to_negative_indexes(self, value):
        new_indexes = {-1: value}
        for key, value in self.__negative_indexes.items():
            new_indexes[key-1] = value
        return new_indexes

    def append(self, value):
        index = 1 + self.__get_last_index()
        self.__inventory[index] = value
        self.__negative_indexes = self.__append_to_negative_indexes(value)

    def extend(self, iterable):
        for char in iterable:
            self.append(char)

    def insert(self, index, value):
        if index < 0:
            new_indexes = {}
            for key, v in self.__negative_indexes.items():
                if key == index:
                    new_indexes[index] = value
                if key <= index:
                    new_indexes[key-1] = v
                else:
                    new_indexes[key] = v
            self.__negative_indexes = new_indexes

            num = 0
            new_inventory_indexes = {}
            for value in self.__negative_indexes.values().__reversed__():
                new_inventory_indexes[num] = value
                num += 1
            self.__inventory = new_inventory_indexes
            return None

        new_indexes = {}
        for key, v in self.__inventory.items():
            if key == index:
                new_indexes[index] = value
            if key >= index:
                new_indexes[key+1] = v
            else:
                new_indexes[key] = v
        self.__inventory = new_indexes

        num = -1
        new_negative_indexes = {}
        for value in self.__inventory.values().__reversed__():
            new_negative_indexes[num] = value
            num -= 1
        self.__negative_indexes = new_negative_indexes

    def add_first(self, value):
        return self.insert(0, value)

    def __remove_from_negative_indexes(self, index):
        length = len(self.__negative_indexes)
        length -= index

        if length <= 0:
            raise IndexError("Index out of range!")

        del self.__negative_indexes[-length]

        return self.__update_negative_indexes()

    def __remove_from_inventory(self, index):
        length = len(self.__inventory)
        length -= abs(index)

        if length < 0:
            raise IndexError("Index out of range!")

        del self.__inventory[length]

        return self.__update_inventory_indexes()

    def __update_negative_indexes(self):
        new_indexes = {}
        num = -1
        for key, value in self.__negative_indexes.items():
            new_indexes[num] = value
            num -= 1

        return new_indexes

    def __update_inventory_indexes(self):
        new_indexes = {}
        num = 0
        for key, value in self.__inventory.items():
            key = num
            new_indexes[key] = value
            num += 1

        return new_indexes

    def remove(self, index):
        try:
            if index < 0:
                value = self.__negative_indexes[index]
                del self.__negative_indexes[index]
                self.__negative_indexes = self.__update_negative_indexes()
                self.__inventory = self.__remove_from_inventory(index)
                return value

            value = self.__inventory[index]
            del self.__inventory[index]
            self.__inventory = self.__update_inventory_indexes()
            self.__negative_indexes = self.__remove_from_negative_indexes(index)
            return value

        except KeyError:
            raise IndexError("Index out of range!")

    def clear(self):
        self.__inventory = {}
        self.__negative_indexes = {}

    def pop(self, index=-1):
        return self.remove(index)

    def index(self, value):
        if value in self.__inventory.values():
            for k, v in self.__inventory.items():
                if v == value:
                    return k
        else:
            raise ValueError("Value not found!")

    def get(self, index):
        if index < 0:
            return self.__negative_indexes[index]
        return self.__inventory[index]

    def count(self, value):
        times = 0
        for v in self.__inventory.values():
            if v == value:
                times += 1
        return times

    def reverse(self):
        return Inventory(*self.__inventory.values().__reversed__())

    def copy(self):
        return Inventory(*self.__inventory.values())

    def size(self):
        return len(self.__inventory)

    @staticmethod
    def isnum(element):
        if isinstance(element, int) or isinstance(element, float):
            return True
        return False

    @staticmethod
    def isstring(element):
        if isinstance(element, str):
            return True
        return False

    @staticmethod
    def isbool(element):
        if isinstance(element, bool):
            return True
        return False

    @staticmethod
    def islist(element):
        if isinstance(element, list) or isinstance(element, tuple):
            return True
        return False

    @staticmethod
    def isInventory(obj):
        if isinstance(obj, Inventory):
            return True
        return False

    def sum(self):
        total_sum = 0
        for element in self.__inventory.values():
            if Inventory.isnum(element):
                total_sum += element
            elif Inventory.isstring(element):
                total_sum += len(element)
            elif Inventory.isbool(element):
                continue
            else:
                raise ValueError(f"{element} cannot be summed!")

        return total_sum

    def __dict__(self):
        return self.__inventory

#    def test(self):
#        return self.__inventory

#    def test_2(self):
#        return self.__negative_indexes

    def __str__(self):
        return '[' + ', '.join([str(char) if type(char) != str else f"\'{char}\'" for char in self.__inventory.values()]) + ']'


inventory = Inventory(1, 2, -6, 3, 4, 5, 6, 7, 8, 9, 10, "Gorge", True, False)

print(inventory) # [1, 2, -6, 3, 4, 5, 6, 7, 8, 9, 10, "Gorge", True, False]
print(inventory[3]) # 3
print(inventory[-3]) # Gorge
print()
try:
    print(inventory[:5])
except:
    print("Cannot slice")
print()
try:
    print(inventory[1287])
except:
    pass
print()
inventory.append("Seven")
print(inventory[-1]) # Seven
print()
inventory.extend([[1, 2, 3], [1, 3, 2]])
print(inventory[-1]) # [1, 3, 2]
print()
inventory.insert(3, "8")
print(inventory) # [1, 2, -6, "8", 3, 4, 5, 6, 7, 8, 9, 10, "Gorge", True, False, "Seven", [1, 2, 3], [1, 3, 2]]

inventory.add_first(0)

print(inventory)
# print(inventory.test_2())

print(inventory[0]) # 0

inventory.remove(0)

print(inventory)
# print(inventory.test_2())

print(inventory[0]) # 1

print(inventory.pop()) # [1, 3, 2]

print(inventory)
# print(inventory.test_2())

print(inventory[-1]) # [1, 2, 3]

print(inventory.index(1)) # 0

print(inventory.get(2)) # -6

print(inventory.count("Gorge")) # 1

inventory = Inventory(3, 2, 1)
print(inventory.reverse()) # [1, 2, 3]
print(inventory) # [3, 2, 1]

inventory_copy = inventory.copy()
print(inventory != inventory_copy) # True

inventory_copy.append(1)
print(inventory.size()) # 3

inventory = Inventory(1, "23", 4)
print(inventory.sum()) # 7

print(inventory.__dict__()) # {0: 1, 1: "23", 2: 4}

inventory.clear()
print(inventory) # []
