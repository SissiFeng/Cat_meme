import asyncio
from video_processing import create_meme_video
from file_management import get_meme_video_paths

async def process_meme_generation(background, sentences, meme_selector):
    meme_paths = get_meme_video_paths()
    selected_memes = []
    
    for sentence in sentences:
        selected_index = meme_selector.select_meme(sentence, meme_paths)
        selected_memes.append(meme_paths[selected_index])
    
    video = await asyncio.to_thread(create_meme_video, background, selected_memes, sentences)
    
    output_path = "temp/output_meme.mp4"
    video.write_videofile(output_path)
    
    return output_path