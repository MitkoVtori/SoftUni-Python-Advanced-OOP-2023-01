from project.song import Song


class Album:

    def __init__(self, name, *songs):
        self.name = name
        self.published = False
        self.songs = list(songs)

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        elif self.published:
            return "Cannot add songs. Album is published."

        elif song not in self.songs:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

        else:
            return "Song is already in the album."

    def remove_song(self, song_name):
        if song_name not in [song.name for song in self.songs]:
            return "Song is not in the album."

        elif self.published:
            return "Cannot remove songs. Album is published."

        self.songs = [song for song in self.songs if song.name != song_name]
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        songs = '\n'.join([f"== {song.get_info()}" for song in self.songs])
        return f"Album {self.name}\n{songs}"