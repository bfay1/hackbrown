import sys
import os
from youtube_transcript_api import YouTubeTranscriptApi as tran

def get_id(url):

    id = url[url.find('?v=') + 3:]

    if id.find('&') != -1:
        id = id[:id.find('&')]
    
    return id

def get_script(id):
    return ' '.join([i['text'] for i in tran.get_transcript(id)])