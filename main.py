class Album:
    name = ''
    group = ''
    tracks = []

    def get_tracks(self):
        pass

    def add_track(self):
        pass

    def get_duration(self):
        pass


class Track:
    name = ''
    duration: int = 0

    def show(self):
        return print(f'{self.name}-{self.duration}')


if __name__ == '__main__':
    pass
