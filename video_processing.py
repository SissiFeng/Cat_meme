import cv2
import numpy as np
from moviepy.editor import VideoFileClip, CompositeVideoClip, TextClip

def remove_green_screen(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    return cv2.bitwise_and(frame, frame, mask=~mask)

def overlay_on_background(frame, background):
    return cv2.addWeighted(frame, 1, background, 0.5, 0)

def create_meme_video(background_path, meme_clip_paths, texts):
    background = VideoFileClip(background_path)
    clips = []
    
    for meme_path, text in zip(meme_clip_paths, texts):
        meme_clip = VideoFileClip(meme_path)
        text_clip = TextClip(text, fontsize=24, color='white')
        text_clip = text_clip.set_pos('bottom').set_duration(meme_clip.duration)
        
        composite_clip = CompositeVideoClip([meme_clip, text_clip])
        clips.append(composite_clip)
    
    final_clip = CompositeVideoClip([background] + clips)
    return final_clip