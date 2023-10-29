from project.song import Song
from typing import List, Tuple


class Album:

    def __init__(self, name: str, *songs: Tuple[Song]):
        self.name = name
        self.songs = songs
        self.published = False
        self.songs: List[Song] = [*songs]

    def add_song(self, song: Song):

        if song.single:

            return f"Cannot add {song.name}. It's a single"

        if self.published:

            return "Cannot add songs. Album is published."

        if song.name in self.songs:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        try:
            song = next(filter(lambda s: s.name == song_name, self.songs))

        except StopIteration:

            return "Song is not in the album."

        if self.published:

            return "Cannot remove songs. Album is published."

        self.songs.remove(song)

        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:

            return f"Album {self.name} is already published."

        self.published = True

        return f"Album {self.name} has been published."

    def details(self):
        # songs = []
        # for song in self.songs:
        #     name = song.name
        #     songs.append(f"== {name}")
        #
        # result = '\n'.join(songs)
        # return f"Album {self.name}\n{result}"

        # result = '\n'.join([f'== {song.name}' for song in self.songs])
        songs = '\n'.join([f"== {song.get_info()}" for song in self.songs])
        return (f"Album {self.name}\n"
                f"{songs}")
