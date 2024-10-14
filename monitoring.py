import psutil
import streamlit as st

def show_resource_usage():
    st.subheader("Resource Usage")
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    
    st.progress(cpu_percent / 100, text=f"CPU Usage: {cpu_percent}%")
    st.progress(memory_percent / 100, text=f"Memory Usage: {memory_percent}%")