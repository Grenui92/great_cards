import re
import subprocess
import os

from tube.models import Videos
class VideoServices:
    
    @staticmethod
    def get_pathes_from_result(result):
        try:
            video_path = re.findall(r'[^media][\S]+', re.findall(r'\S+\.webm', result.stdout)[0])[0]
        except IndexError:
            video_path = re.findall(r'[^media][\S]+', re.findall(r'\S+\.mp4', result.stdout)[0])[0]
            
        subs_path = re.findall(r'[^media][\S]+', re.findall(r'\S+vtt', result.stdout)[0])[0]    
        prev_path = re.findall(r'[^media][\S]+', re.findall(r'\S+webp', result.stdout)[0])[0]
        file_name = re.findall(r'\b[\w-]+\.', video_path)[0][:-1].replace('_', ' ')
        return video_path, prev_path, subs_path, file_name
    

           
