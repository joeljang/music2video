import os

output = 'outputs'

mp4_files = [file for file in os.listdir(output) if file.endswith('.mp4')]
#mp4_files.sort()
with open('list-of-files.txt', 'w') as f: 
    for file in mp4_files: 
        file = output+'/'+file
        f.write(f"file {file}\n")

output_file = "output.ts"
os.system(f'ffmpeg -f concat -safe 0 -i list-of-files.txt -c copy {output_file}')

import ffmpeg
video = ffmpeg.input(output_file)
audio = ffmpeg.input('imagenet_song.mp3')
ffmpeg.concat(video, audio, v=1, a=1).output('output.mp4', strict='-2').run()