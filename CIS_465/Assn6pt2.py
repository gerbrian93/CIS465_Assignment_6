import cv2
import numpy as np
from playsound import playsound
import moviepy.editor
from pydub import AudioSegment
import sys

# extracting audio from video with moviepy
vid = moviepy.editor.VideoFileClip('Videos\Testvideo.avi')
audio = vid.audio
audio.write_audiofile('Audio\Testvidaudio17_34sec.mp3')

# audio segemnt with pydub
aud = AudioSegment.from_file('Testvidaudio17_34sec.mp3')
#  define subclips of audio
first_3_seconds = aud[:3000]
middle = aud[3000:14000]
last_3_seconds = aud[-3000:]
#  increase and decrease decibles of clips
beginning = first_3_seconds + 10
end = last_3_seconds + 5
#  concatenate the audios together
output = beginning + middle + end
#  export to Audio folder
output.export("Audio\LoudnQuiet.mp3", format="mp3")

aud2 = AudioSegment.from_mp3("Audio\LoudnQuiet.mp3")
# first second of video and remainder of video
first_sec = aud2[:1000]
remaining = aud2[-16000:]
# reduce the decible of the first second by 100. Since it is not 100db the output should be silence.
reduceVol = first_sec - 100
# concatenate audio segments
out = reduceVol + remaining
out.export("Audio\FirstsecSilent.mp3", format="mp3")


# OVERLAYING AUDIO CLIP
aclip1 = AudioSegment.from_file("Audio\FirstsecSilent.mp3")
aclip2 = AudioSegment.from_file("Audio\it.wav")
out2 = aclip1.overlay(aclip2, position=3000)
out2.export("Audio\Finaloutput.mp3", format="mp3")
