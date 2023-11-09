#omsairam omsairam omsairam omsairam omsairam omsairam omsairam omsairam omsairam

from gtts import gTTS
import os
from pydub import AudioSegment
import moviepy.editor as mpy
import subprocess
from mutagen.mp3 import MP3
import math
import cv2
import glob
import ffmpeg
from pydub import AudioSegment

def addAudio(audioSource, videoSource, savePath):
    subprocess.run(f'ffmpeg -y -i "{videoSource}" -i "{audioSource}" -c copy "{savePath}"')

def get_text(file):

    text = []
    with open(file, 'r') as f:
        for row in f:
            text.append(row.strip().split())
    return text
def generate_audio(text, i):
    language = 'en'
    speech = gTTS(text = str(text), tld = "ca", lang = language, slow = False)
    name = "audio" + str(i) + ".mp3"
    speech.save(name)

    root = name
    velocidad_X = 1.3 # No puede estar por debajo de 1.0
    sound = AudioSegment.from_file(root)
    so = sound.speedup(velocidad_X, 150, 25)
    
    aud = MP3(root)
    len1 = aud.info.length - 0.5
    print(len1)
    fin = so[:len1]

    
    so.export(name, format = 'mp3')



    return name

def get_audio_files(text):
    audio_files = []
    for i in range(len(text)):
        if (len(text[i]) > 0):
            txt = " ".join(text[i])
            name = generate_audio(txt, i)
            audio_files.append((txt, name))
    return audio_files


def convert(lst):
    return ' '.join(lst)

def make_vids(files):
    frame_count = 0
    num = 0
    for (t, a) in files:
        audio = mpy.AudioFileClip(a)
        aud = MP3(a)
        len1 = aud.info.length
        #60 frames per second
        frames = math.ceil(90* len1)

        x = 0
        num += 1



        for i in range(frames):
            f = "images/frame" +  str(frame_count) + ".jpg"
            frame_count += 1
            img = cv2.imread(f)
            h, w, c = img.shape

            # font
            font = cv2.FONT_HERSHEY_DUPLEX
            # org
            # fontScale
            fontScale = 2
            # Blue color in BGR
            color = (255, 255, 255)
            # Line thickness of 2 px
            thickness = 2


            print(t)
            tlst = t.split()
            print(tlst)
            first = []
            second = []
            print(type(tlst))
            half = len(tlst)/2

            for i in range(len(tlst)):
                if i < half:
                    first.append(tlst[i])
                else:
                    second.append(tlst[i])

            strf = convert(first)
            strs = convert(second)


            org = (int(w/2) - 500, int(h/2) - 100)

            image = cv2.putText(img, strf, org, font,
                                fontScale, color, thickness, cv2.LINE_AA)


            org = (int(w/2) - 500, int(h/2))
            image = cv2.putText(image, strs, org, font,
                                fontScale, color, thickness, cv2.LINE_AA)


            height, width, layers = image.shape




            if x == 0:
                file = "video/video_name" + str(num) + ".mp4"
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                video = cv2.VideoWriter(file, fourcc, 90, (width, height))
                x += 1
            video.write(image)

        video.release()
        video1 = mpy.VideoFileClip(file)
        fin = "output" + str(num) + ".mp4"
        final_video = video1.set_audio(audio)

        final_video.write_videofile(fin,
                                    fps=90,
                                    codec='libx264',
                                    audio_codec='aac',
                                    temp_audiofile='temp-audio.m4a',
                                    remove_temp=True
                                    )
    return num



def concat(num):
    vids = []

    for i in range(num):
        file = "output" + str(i+1) + ".mp4"
        vids.append(mpy.VideoFileClip(file, audio = True))

    # list of video files
    files = vids

    # eparate video and audio, then flat the array
    final_clip = mpy.concatenate_videoclips(vids)
    final_clip.to_videofile("output.mp4", fps=90, remove_temp=False)

    video1 = mpy.VideoFileClip("output.mp4")
    audio = mpy.AudioFileClip("outputTEMP_MPY_wvf_snd.mp3")

    final_video = video1.set_audio(audio)

    final_video.write_videofile("final_outputREAL.mp4",
                                fps=90,
                                codec='libx264',
                                audio_codec='aac',
                                temp_audiofile='temp-audio.m4a',
                                remove_temp=True
                                )


if __name__ == "__main__":
    text = get_text("demofile.txt")
    files = get_audio_files(text)
    num = make_vids(files)
    concat(num)

















