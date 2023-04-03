from project.booths.booth import Booth


class PrivateBooth(Booth):
    price_per_person = 3.50

    def reserve(self, number_of_people: int):
        price = PrivateBooth.price_per_person * number_of_people
        self.price_for_reservation = price
        self.is_reserved = True

