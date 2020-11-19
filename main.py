class Album:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.tracks = []

    def get_tracks(self):
        for track in self.tracks:
            print(track.show())

    def add_track(self, track_name, track_duration):
        song = Track(track_name, track_duration)
        self.tracks.append(song)
        return

    def get_duration(self):
        # for track in self.tracks:
        #     if track.name == track_name:
        #         print(track.duration)
        all_duration = 0
        for track in self.tracks:
            all_duration += track.duration
        return all_duration


class Track:
    def __init__(self, name, duration=0):
        self.name = name
        self.duration = duration

    def show(self):
        print(f'{self.name}-{self.duration}')

if __name__ == '__main__':
    album1 = Album('Songister', 'Star People')
    album1.name = 'New age'
    album1.add_track('Super Start', 3)
    album1.add_track('Second Station', 2)
    album1.add_track('Nova', 5)

    album2 = Album('Apple', 'Seven Day')
    album2.add_track('I build new World', 3)
    album2.add_track('NEXT', 4)
    album2.add_track('Final Day', 5)

    print(f'длина альбома {album1.name} = {album1.get_duration()} минут')
    print(f'длина альбома {album2.name} = {album2.get_duration()} минут')


