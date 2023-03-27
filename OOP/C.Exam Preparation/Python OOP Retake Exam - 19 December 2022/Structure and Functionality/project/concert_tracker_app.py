from project.band_members.singer import Singer
from project.band_members.guitarist import Guitarist
from project.band_members.drummer import Drummer
from project.concert import Concert
from project.band import Band


class ConcertTrackerApp:

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        valid_musician_types = ["Guitarist", "Drummer", "Singer"]
        if musician_type not in valid_musician_types:
            raise ValueError("Invalid musician type!")

        if name in [x.name for x in self.musicians]:
            raise Exception(f"{name} is already a musician!")

        if musician_type == valid_musician_types[0]:
            musician = Guitarist(name, age)

        if musician_type == valid_musician_types[1]:
            musician = Drummer(name, age)

        if musician_type == valid_musician_types[2]:
            musician = Singer(name, age)

        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if name in [x.name for x in self.bands]:
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        if place in [x.place for x in self.concerts]:
            raise Exception(f"{place} is already registered for {[x.genre for x in self.concerts if x.place == place][0]} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name, band_name):
        if musician_name not in [x.name for x in self.musicians]:
            raise Exception(f"{musician_name} isn't a musician!")

        if band_name not in [x.name for x in self.bands]:
            raise Exception(f"{band_name} isn't a band!")

        band = [x for x in self.bands if x.name == band_name][0]
        musician = [x for x in self.musicians if x.name == musician_name][0]
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name, band_name):
        if band_name not in [x.name for x in self.bands]:
            raise Exception(f"{band_name} isn't a band!")

        if musician_name not in [x.name for x in [x for x in self.bands if x.name == band_name][0].members]:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band = [x for x in self.bands if x.name == band_name][0]
        band.members = [x for x in band.members if x.name != musician_name]
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place, band_name):
        band = [x for x in self.bands if x.name == band_name][0]
        concert = [x for x in self.concerts if x.place == concert_place][0]
        members = band.members
        type_members = [type(x).__name__ for x in band.members]

        if "Guitarist" not in type_members or "Drummer" not in type_members or "Singer" not in type_members:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == "Rock":
            needed_skills = ["play the drums with drumsticks", "sing high pitch notes", "play rock"]

        elif concert.genre == "Metal":
            needed_skills = ["play the drums with drumsticks", "sing low pitch notes", "play metal"]

        elif concert.genre == "Jazz":
            needed_skills = ["play the drums with drum brushes", "sing high pitch notes", "sing low pitch notes", "play jazz"]

        for member in members:
            needed_skills_copy = needed_skills.copy()
            for skill in needed_skills_copy:
                if skill in member.skills:
                    needed_skills.remove(skill)

        if needed_skills:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."

