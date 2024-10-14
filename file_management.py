import tempfile
import os
import shutil

def save_uploaded_file(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        return tmp_file.name

def cleanup_temp_files(file_paths):
    for path in file_paths:
        try:
            os.remove(path)
        except Exception as e:
            print(f"Error deleting {path}: {e}")

def get_meme_video_paths():
    meme_folder = "assets/meme_videos"
    return [os.path.join(meme_folder, f) for f in os.listdir(meme_folder) if f.endswith('.mp4')]