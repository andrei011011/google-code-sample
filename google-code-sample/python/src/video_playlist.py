"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, playlist_title: str):
        self._title = playlist_title
        self._videos = []

    @property
    def title(self) -> str:
        """Returns the title of a Playlist."""
        return self._title

    def add_video(self, video):
        self._videos.append(video)

    def remove_video(self, video):
        self._videos.pop(self._videos.index(video))

    def contains_video(self, video):
        contains_video = False
        for vid in self._videos:
            if vid == video:
                contains_video = True
                break
        return contains_video

    def clear(self):
        self._videos = []


class PlaylistLibrary:
    """A class used to represent a Playlist Library."""

    def __init__(self):
        self.playlist_list = []

    def get_playlist(self, playlist_name):
        for playlist in self.playlist_list:
            if playlist.title.upper() == playlist_name.upper():
                return playlist
        return None

    def delete_playlist(self, playlist):
        self.playlist_list.pop(self.playlist_list.index(playlist))