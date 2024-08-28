import subprocess
from difflib import SequenceMatcher
import re
import os

import webvtt
from celery import shared_task
from django.contrib.auth.models import User
from django.conf import settings

from .models import Videos
from .services.video_services import VideoServices


@shared_task
def download_and_create_video(ABSOLUTE_UPLOAD_URL,
                              OUTPUT_FILENAME, url,
                              user_id):
    """Download the video from the given URL and create a new video in the
    database. This function is a celery task. It downloads the video from the
    given URL and creates a new video in the database. The video is downloaded
    using the yt-dlp library. The video is saved in the media/videos directory.

    :param ABSOLUTE_UPLOAD_URL: The absolute path to the upload directory.
    :param OUTPUT_FILENAME: The name of the output file.
    :param url: The URL of the video.
    :param user_id: The ID of the User.
    :return: A message that the video was successfully added.
    """
    user = User.objects.get(id=user_id)
    if url.startswith('https://www.youtube.com/watch?v='):
        yt_id = re.findall(r'watch\?v=[\w-]+', url)[0].split('=')[1]
        file_path = f'{ABSOLUTE_UPLOAD_URL}{yt_id}/{OUTPUT_FILENAME}'

        try:
            os.makedirs(f'{ABSOLUTE_UPLOAD_URL}{yt_id}')
            command = ['yt-dlp',
                       '-o', file_path,
                       '--skip-download',
                       '--restrict-filenames', '--write-thumbnail',
                       '--write-sub', '--write-auto-sub', url]

            result = subprocess.run(
                command, capture_output=True, text=True, check=True)
            prev_path, subs_path, file_name, sub_flag = VideoServices.get_pathes_from_result(
                result=result)
            
            if sub_flag:
                create_sbtt(sub_path=subs_path)

            video = Videos.objects.create(
                video_name=file_name,
                video_prev=prev_path,
                video_subs=subs_path,
                yt_id=yt_id,
                yt_url=url
            )
            video.owner.set([user])

        except FileExistsError:
            video = Videos.objects.get(yt_id=yt_id)
            video.owner.add(user)

        return f'Video named {video.video_name} successfully added.'


def create_sbtt(sub_path):
    """Create a new sbtt file from the given vtt file. This function reads the
    vtt file and creates a new sbtt file and saves it in the same directory.

    :param sub_path: The path to the vtt file.
    """
    result = []
    file_path = settings.MEDIA_ABSOLUTE_PATH
    old_string = ''
    result = ['WEBVTT\n']
    for caption in webvtt.read(f'{file_path}{sub_path}'):
        # это и дальше для автоматически сгенерированых сабов от ютуба. говно
        splited_text = caption.text.split('\n')

        if len(splited_text) <= 1:
            break
        if not splited_text[1].strip():
            continue

        new_string = splited_text[0]

        matcher = SequenceMatcher(None, new_string, old_string)

        if matcher.ratio() < 0.5:
            result.extend([caption.start, ' --> ', caption.end,
                          '\n', caption.text, '\n\n'])
        else:
            result.extend([caption.start, ' --> ', caption.end,
                          '\n', splited_text[1], '\n\n'])

        old_string = splited_text[-1]
    else:
        with open(f'{file_path}{sub_path}', 'w+') as file:
            file.writelines(''.join(result))
