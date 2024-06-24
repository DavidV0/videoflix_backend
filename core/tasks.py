import os
import subprocess
import logging

logger = logging.getLogger(__name__)

def convert_480p(source):
    logger.info(f"Starting conversion to 480p for {source}")
    ffmpeg_path = '/opt/homebrew/bin/ffmpeg'  # Use the full path to ffmpeg
    new_file_name = source.rsplit('.', 1)[0] + '_480p.mp4'
    cmd = f'"{ffmpeg_path}" -i "{source}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{new_file_name}"'
    run = subprocess.run(cmd, shell=True, capture_output=True, text=True)
  
    return new_file_name

def convert_720p(source):
    logger.info(f"Starting conversion to 720p for {source}")
    ffmpeg_path = '/opt/homebrew/bin/ffmpeg'  # Use the full path to ffmpeg
    new_file_name = source.rsplit('.', 1)[0] + '_720p.mp4'
    cmd = f'"{ffmpeg_path}" -i "{source}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{new_file_name}"'
    run = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    return new_file_name
