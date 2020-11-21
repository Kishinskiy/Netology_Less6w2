class Album:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.tracks = []

    def get_tracks(self):
        for track in self.tracks:
            print(track)

    def add_track(self, track_name, track_duration):
        song = Track(track_name, track_duration)
        self.tracks.append(song)
        return

    def get_duration(self):
        all_duration = 0
        for track in self.tracks:
            all_duration += track.duration
        return all_duration

    def __info(self):
        print(f'Name group: {self.group}\n'
              f'Name album: {self.name}\n'
              f'Tracks:')
        for track in self.tracks:
            print(f'\t\t{track}')
        return ''

    def __str__(self):
        return str(self.__info())


class Track:
    def __init__(self, name, duration=0):
        self.name = name
        self.duration = duration

    def show(self):
        return self.name, self.duration
        # print(f'{self.name}-{self.duration}min')

    def __str__(self):
        return f'{self.name}-{self.duration}min'

    def __gt__(self, other):
        return isinstance(other, Track) and \
            self.duration > other.duration

    def __lt__(self, other):
        return isinstance(other, Track) and \
            self.duration < other.duration

    def __eq__(self, other):
        return isinstance(other, Track) and \
            self.duration == other.duration


if __name__ == '__main__':
    album1 = Album('Songister', 'Star People')
    album1.add_track('Super Start', 3)
    album1.add_track('Second Station', 2)
    album1.add_track('Nova', 5)

    album2 = Album('Apple', 'Seven Day')
    album2.add_track('I build new World', 3)
    album2.add_track('NEXT', 4)
    album2.add_track('Final Day', 5)

    track1 = Track('First Equals Track', 6)
    track2 = Track('Second Equals Track', 4)

    print(track1 > track2)
    print(track1 < track2)
    print(track1 == track2)

    print(album2)

    print(f'длина альбома {album1.name} = {album1.get_duration()} минут')
    print(f'длина альбома {album2.name} = {album2.get_duration()} минут')
