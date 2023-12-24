import re
import subprocess
import os

from tube.models import Videos
class VideoServices:
    
    @staticmethod
    def get_pathes_from_result(result):
        # subs_path = re.findall(r'\S+vtt', result.stdout)[0]
        # video_path = re.findall(r'\S+mp4', result.stdout)[0]
        # prev_path = re.findall(r'\S+webp', result.stdout)[0]
        subs_path = re.findall(r'[^media][\S]+', re.findall(r'\S+vtt', result.stdout)[0])[0]
        video_path = re.findall(r'[^media][\S]+', re.findall(r'\S+mp4', result.stdout)[0])[0]
        prev_path = re.findall(r'[^media][\S]+', re.findall(r'\S+webp', result.stdout)[0])[0]
        file_name = re.findall(r'\b\w+\.', video_path)[0][:-1]
        return video_path, prev_path, subs_path, file_name
    
    @staticmethod
    def download_and_create_video(ABSOLUTE_UPLOAD_URL, OUTPUT_FILENAME, url, user):
        if url.startswith('https://www.youtube.com/watch?v='):
            yt_id = re.findall(r'watch\?v=\w+', url)[0].split('=')[1]
            
            try:
                os.makedirs(f'{ABSOLUTE_UPLOAD_URL}{yt_id}')
                command = ['yt-dlp', 
                    '-o', f'{ABSOLUTE_UPLOAD_URL}{yt_id}/{OUTPUT_FILENAME}', 
                    '--restrict-filenames', '--write-thumbnail', 
                    '--write-sub', '--write-auto-sub', 
                    url]
                result = subprocess.run(command, capture_output=True, text=True, check=True)
                video_path, prev_path, subs_path, file_name = VideoServices.get_pathes_from_result(result=result)

                video = Videos.objects.create(
                    video_name=file_name,
                    video_prev=prev_path,
                    video_subs=subs_path,
                    vieo_path=video_path,
                    yt_id=yt_id,
                    yt_url=url
                )
                video.owner.set([user])
                # VideoServices.replace_subs(video)
              
            except FileExistsError:
                video = Videos.objects.get(yt_id=yt_id)
                video.owner.add(user)

            return f'Video named {video.video_name} successfully added.'
           
