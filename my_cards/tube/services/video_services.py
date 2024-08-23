import re


class VideoServices:
    """A class that provides services for video processing."""

    @staticmethod
    def get_pathes_from_result(result):
        """Get the path, file name and subtitles files from the result of
        the yt-dlp command.

        :param result: The result of the yt-dlp command.
        :return: The path to the previous file, the path to the subtitles file
        and the file name.
        :rtype: tuple
        """
        subs_path = re.findall(r'[^media][\S]+',
                               re.findall(r'\S+vtt',
                                          result.stdout)[0])[0]

        prev_path = re.findall(r'[^media][\S]+',
                               re.findall(r'\S+webp',
                                          result.stdout)[0])[0]

        file_name = re.findall(r'\b[\w-]+\.',
                               subs_path)[0][:-1].replace('_', ' ')

        return prev_path, subs_path, file_name
