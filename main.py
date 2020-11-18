class Album:
    name = ''
    group = ''
    tracks = []

    def get_tracks(self):
        for track in self.tracks:
            Track.show(track)

    def add_track(self, track_name, track_duration):
        song = Track(track_name, track_duration)
        self.tracks.append(song)
        return

    def get_duration(self):
        pass


class Track:
    def __init__(self, name, duration=0):
        self.name = name
        self.duration = duration

    def show(self):
        return print(f'{self.name}-{self.duration}')


if __name__ == '__main__':
    Album.add_track(Album(), 'Super', 3, )
    # Album.get_tracks(self)
