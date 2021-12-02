import argparse
import os

# python concat.py --dirs "outputs" --music music_sample/2.flac --output output.mp4

# Create the parser
vq_parser = argparse.ArgumentParser(description='concat')

# Add the arguments
vq_parser.add_argument("--dirs", type=str, default="outputs")
vq_parser.add_argument("--music", type=str)
vq_parser.add_argument("--output", type=str, default="output.mp4")
# Execute the parse_args() method
args = vq_parser.parse_args()

mp4_files = [file for file in os.listdir(args.dirs) if file.endswith('.mp4')]
mp4_files.sort()
with open('list-of-files.txt', 'w') as f: 
    for file in mp4_files: 
        file = os.path.join("outputs", file)
        f.write(f"file {file}\n")

os.system('ffmpeg -f concat -safe 0 -i list-of-files.txt -c copy output.ts')

import ffmpeg
video = ffmpeg.input('output.ts')
audio = ffmpeg.input(args.music)
ffmpeg.concat(video, audio, v=1, a=1).output(args.output, strict='-2').run()
