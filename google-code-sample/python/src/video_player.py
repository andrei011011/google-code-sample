"""A video player class."""

from .video_library import VideoLibrary
from video_playlist import Playlist, PlaylistLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._playlist_library = PlaylistLibrary()
        self.is_playing = False
        self.video_playing = None

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos:")
        videos = []
        for video in self._video_library.get_all_videos():
            videos.append(video.info)
        videos.sort()
        for video in videos:
            print(video)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        vid = self._video_library.get_video(video_id)

        if vid is None:
            print('Cannot play video: Video does not exist')
            return

        if vid.flag:
            if vid.reason_for_flag is None:
                print('Cannot play video: Video is currently flagged (reason: Not supplied)')
            else:
                print('Cannot play video: Video is currently flagged (reason: ' + vid.reason_for_flag)
        else:
            if self.is_playing or self.video_playing is not None:
                print('Stopping video: ' + self.video_playing.title)

            self.is_playing = True
            self.video_playing = vid
            print("Playing video: " + vid.title)

    def stop_video(self):
        """Stops the current video."""

        if self.is_playing:
            print('Stopping video: ' + self.video_playing.title)
            self.is_playing = False
            self.video_playing = None
        else:
            if self.video_playing is None:
                print('Cannot stop video: No video is currently playing')
            else:
                print('Stopping video: ' + self.video_playing.title)
                self.video_playing = None

    def play_random_video(self):
        """Plays a random video from the video library."""

        num_videos = len(self._video_library.get_all_videos())
        random_video = self._video_library.get_all_videos()[random.randint(0, num_videos-1)]
        self.play_video(random_video.video_id)

    def pause_video(self):
        """Pauses the current video."""

        if self.is_playing:
            print('Pausing video: ' + self.video_playing.title)
            self.is_playing = False
        else:
            if self.video_playing is None:
                print('Cannot pause video: No video is currently playing')
            else:
                print('Video already paused: ' + self.video_playing.title)

    def continue_video(self):
        """Resumes playing the current video."""

        if self.is_playing:
            print('Cannot continue video: Video is not paused')
        else:
            if self.video_playing is None:
                print('Cannot continue video: No video is currently playing')
            else:
                print('Continuing video: ' + self.video_playing.title)
                self.is_playing = True

    def show_playing(self):
        """Displays video currently playing."""

        if self.is_playing:
            print("Currently playing: " + self.video_playing.info)
        else:
            if self.video_playing is None:
                print('No video is currently playing')
            else:
                print("Currently playing: " + self.video_playing.info + ' - PAUSED')

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        is_name_taken = False
        for name in self._playlist_library.playlist_list:
            if name.title.upper() == playlist_name.upper():
                is_name_taken = True
                break

        if is_name_taken:
            print('Cannot create playlist: A playlist with the same name already exists')
        else:
            playlist = Playlist(playlist_name)
            self._playlist_library.playlist_list.append(playlist)
            print('Successfully created new playlist: ' + playlist.title)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        playlist = self._playlist_library.get_playlist(playlist_name)
        if playlist is None:
            print('Cannot add video to ' + playlist_name + ': Playlist does not exist')
        else:
            video = self._video_library.get_video(video_id)
            if playlist.contains_video(video):
                print('Cannot add video to ' + playlist_name + ': Video already added')
            else:
                if video is None:
                    print('Cannot add video to ' + playlist_name + ': Video does not exist')
                else:
                    playlist.add_video(video)
                    print('Added video to ' + playlist_name + ': ' + video.title)

    def show_all_playlists(self):
        """Display all playlists."""

        if self._playlist_library.playlist_list:
            print('Showing all playlists:')
            playlist_title_list = []
            for playlist in self._playlist_library.playlist_list:
                playlist_title_list.append(playlist.title)
            playlist_title_list.sort()
            for playlist in playlist_title_list:
                print(playlist)
        else:
            print('No playlists exist yet')

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist = self._playlist_library.get_playlist(playlist_name)
        if playlist is None:
            print('Cannot show playlist another_playlist: Playlist does not exist')
        else:
            print('Showing playlist: ' + playlist_name)
            if playlist._videos:
                for video in playlist._videos:
                    print(video.info)
            else:
                print('No videos here yet')

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        playlist = self._playlist_library.get_playlist(playlist_name)
        if playlist is None:
            print('Cannot remove video from ' + playlist_name + ': Playlist does not exist')
        else:
            video = self._video_library.get_video(video_id)
            if playlist.contains_video(video):
                playlist.remove_video(video)
                print('Removed video from ' + playlist_name + ': ' + video.title)
            else:
                if video is None:
                    print('Cannot remove video from ' + playlist_name + ': Video does not exist')
                else:
                    print('Cannot remove video from ' + playlist_name + ': Video is not in playlist')

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist = self._playlist_library.get_playlist(playlist_name)
        if playlist is None:
            print('Cannot clear playlist ' + playlist_name + ': Playlist does not exist')
        else:
            print('Successfully removed all videos from ' + playlist_name)
            playlist.clear()

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist = self._playlist_library.get_playlist(playlist_name)
        if playlist is None:
            print('Cannot delete playlist ' + playlist_name + ': Playlist does not exist')
        else:
            print('Deleted playlist: ' + playlist_name)
            self._playlist_library.delete_playlist(playlist)

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        found_videos = []
        video_list = self._video_library.get_all_videos()
        for video in video_list:
            if search_term.upper() in video.title.upper():
                found_videos.append(video)
        if found_videos:
            print('Here are the results for ' + search_term + ':')
            found_videos.sort(key=lambda x: x.info, reverse=False)
            for i in range(1, len(found_videos) + 1):
                print(str(i) + ') ' + found_videos[i-1].info)
            print('Would you like to play any of the above? If yes, specify the number of the video.')
            print('If your answer is not a valid number, we will assume it\'s a no.')
            answer = input()
            try:
                self.play_video(found_videos[int(answer)-1].video_id)
            except:
                pass
        else:
            print('No search results for ' + search_term)

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        found_videos = []
        video_list = self._video_library.get_all_videos()
        for video in video_list:
            has_tag = False
            for tag in video.tags:
                if video_tag.upper() == tag.upper():
                    has_tag = True
            if has_tag:
                found_videos.append(video)
        if found_videos:
            print('Here are the results for ' + video_tag + ':')
            found_videos.sort(key=lambda x: x.info, reverse=False)
            for i in range(1, len(found_videos) + 1):
                print(str(i) + ') ' + found_videos[i - 1].info)
            print('Would you like to play any of the above? If yes, specify the number of the video.')
            print('If your answer is not a valid number, we will assume it\'s a no.')
            answer = input()
            try:
                self.play_video(found_videos[int(answer) - 1].video_id)
            except:
                pass
        else:
            print('No search results for ' + video_tag)

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        video = self._video_library.get_video(video_id)
        if video is None:
            print('Cannot flag video: Video does not exist')
        else:
            if video.flag is None:
                if flag_reason == '':
                    print('Successfully flagged video: ' + video.title + ' (reason: Not supplied)')
                    video.flag = True
                else:
                    print('Successfully flagged video: ' + video.title + ' (reason: ' + flag_reason + ')')
                    video.flag = True
                    video.reason_for_flag = flag_reason
            else:
                print('Cannot flag video: Video is already flagged')

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
