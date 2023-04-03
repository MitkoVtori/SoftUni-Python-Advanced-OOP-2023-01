from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth


class ChristmasPastryShopApp:

    def __init__(self):
        self.booths = [] # objects
        self.delicacies = [] # objects
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if name in [x.name for x in self.delicacies]:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in ["Gingerbread", "Stolen"]:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        if type_delicacy == "Gingerbread":
            delicacy = Gingerbread(name, price)
        else:
            delicacy = Stolen(name, price)

        self.delicacies.append(delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if booth_number in [x.booth_number for x in self.booths]:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in ["Open Booth", "Private Booth"]:
            raise Exception(f"{type_booth} is not a valid booth!")

        if type_booth == "Open Booth":
            booth = OpenBooth(booth_number, capacity)
        else:
            booth = PrivateBooth(booth_number, capacity)

        self.booths.append(booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        booth = [x for x in self.booths if x.capacity >= number_of_people and not x.is_reserved]
        if not booth:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth = booth[0]
        booth.reserve(number_of_people)

        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        if booth_number not in [x.booth_number for x in self.booths]:
            raise Exception(f"Could not find booth {booth_number}!")

        if delicacy_name not in [x.name for x in self.delicacies]:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth = [x for x in self.booths if x.booth_number == booth_number][0]
        delicacy = [x for x in self.delicacies if x.name == delicacy_name][0]
        booth.delicacy_orders.append(delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = [x for x in self.booths if x.booth_number == booth_number][0]
        bill = booth.price_for_reservation + sum([x.price for x in booth.delicacy_orders])
        self.income += bill

        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

