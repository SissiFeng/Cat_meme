import streamlit as st
import os
import random
from PIL import Image
import tempfile
from model import MemeSelector
from video_processing import create_meme_video
from file_management import cleanup_temp_files
from async_processing import process_meme_generation
from monitoring import show_resource_usage

# 初始化全局变量
meme_selector = MemeSelector()

def main():
    st.title("Cat Meme Generator")
    
    # 移除背景上传和选择选项
    
    # 文本输入
    user_text = st.text_area("输入你的梗文本（每行一句）", 
                             placeholder="例如：\n当我听到开罐头的声音\n发现主人买了新玩具\n看到隔壁的狗狗被锁在外面")
    
    if st.button("生成猫咪梗图"):
        if not user_text.strip():
            st.warning("请输入一些文本再生成梗图。")
        else:
            with st.spinner("正在生成你的猫咪梗图..."):
                # 随机选择背景
                background = random_background()
                
                # 处理文本
                sentences = user_text.split('\n')
                sentences = [s.strip() for s in sentences if s.strip()]
                
                # 生成视频
                video_path = process_meme_generation(background, sentences, meme_selector)
                
                # 显示预览
                st.video(video_path)
                
                # 提供下载链接
                st.download_button(
                    label="下载梗图视频",
                    data=open(video_path, 'rb').read(),
                    file_name="cat_meme.mp4",
                    mime="video/mp4"
                )
    
    # 显示资源使用情况
    show_resource_usage()

def random_background():
    bg_folder = "assets/backgrounds"
    bg_files = [f for f in os.listdir(bg_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    if not bg_files:
        raise Exception("背景图片文件夹为空")
    return os.path.join(bg_folder, random.choice(bg_files))

if __name__ == "__main__":
    main()