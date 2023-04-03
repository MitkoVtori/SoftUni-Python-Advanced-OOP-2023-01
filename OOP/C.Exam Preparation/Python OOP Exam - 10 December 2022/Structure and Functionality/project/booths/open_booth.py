from project.booths.booth import Booth


class OpenBooth(Booth):
    price_per_person = 2.50

    def reserve(self, number_of_people: int):
        price = OpenBooth.price_per_person * number_of_people
        self.price_for_reservation = price
        self.is_reserved = True

