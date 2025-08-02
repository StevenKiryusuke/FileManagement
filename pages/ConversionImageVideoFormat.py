import streamlit as st
import moviepy.editor as moviepy

AVI_Upload = st.file_uploader("Choose a AVI File : ", type=["avi"])

if AVI_Upload is not None:
    # Video = st.video(AVI_Upload.name)
    # st.write(Video)
    clip = moviepy.VideoFileClip("C:/Users/USER/Downloads/" + AVI_Upload.name)
    st.write("Video Preprocessing")
    clip.write_videofile("C:/Users/USER/Downloads/" + str(AVI_Upload.name).replace(".avi",".mp4"), fps=30, codec="libx264")
    st.write("Video has been converted to MP4 in C:/Users/USER/Downloads/" + str(AVI_Upload.name).replace(".avi",".mp4"))

MKV_Upload = st.file_uploader("Choose a MKV File : ", type=["mkv"])

if MKV_Upload is not None:
    # Video = st.video(AVI_Upload.name)
    # st.write(Video)
    clip = moviepy.VideoFileClip("C:/Users/USER/Downloads/" + MKV_Upload.name)
    st.write("Video Preprocessing")
    clip.write_videofile("C:/Users/USER/Downloads/" + str(MKV_Upload.name).replace(".mkv",".mp4"), fps=30, codec="libx264")
    st.write("Video has been converted to MP4 in C:/Users/USER/Downloads/" + str(MKV_Upload.name).replace(".mkv",".mp4"))

