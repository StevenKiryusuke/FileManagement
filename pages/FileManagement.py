import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import os
import Image_Processing
import cv2

st.title("Data Engineering Tasks File Management App")

if st.button("Back"):
    switch_page("Home")

Saved_Game_Folder = "C:/Users/USER/Kiryu KaeTamah Yutado/Game/TCG/"
Data_Source = "C:/Users/USER/Kiryu KaeTamah Yutado/Big Data"

def Upload_Image_File(image_file):
   if image_file is not None:
        file_details = {"FileName":image_file.name,"FileType":image_file.type}
        # st.write(file_details)
        img = Image.open(image_file)
        st.image(img)
        with open(os.path.join(Saved_Game_Folder,image_file.name),"wb") as f: 
            f.write(image_file.getbuffer())         
        st.success("Saved File")

Image_file = []

parent_dir = "C:/Users/USER/Kiryu KaeTamah Yutado/Important File/"
Base_file = 'C:/Users/USER/Kiryu KaeTamah Yutado/Big Data/'

if st.button("Take Image", key="Take Image"): # Default folder classification Type

    st.write("Take data")

    # if Image_file:
    Image_Processing.Store_Image_File(Base_file,Image_file)

st.write('This is the default folder data')

Favorite25, Favorite49, Favorite75, JunkFiles, ImportantFile75 = st.columns(5)

with Favorite25:
    if st.button("Favorite 25", key="fav25"):

        Image_Processing.Filter_Move_File(Base_file,Image_file,parent_dir, "Favorite 25")

with Favorite49:

    if st.button("Favorite 49", key="fav49"):

        Image_Processing.Filter_Move_File(Base_file,Image_file,parent_dir, "Favorite 49")

with Favorite75:
    if st.button("Favorite 75", key="fav75"):

        Image_Processing.Filter_Move_File(Base_file,Image_file,parent_dir, "Favorite 75")

with JunkFiles:
    if st.button("Junk Files", key="JunkFiles"):

        Image_Processing.Filter_Move_File(Base_file,Image_file,parent_dir, "Junk Files Favorite 0")

with ImportantFile75:
    if st.button("Important File 75", key="essentialfile75"):

        Image_Processing.Filter_Move_File(Base_file,Image_file,parent_dir, "Important File 75")
        

# Want to create a new folder for 3D Texture
        
# st.write('Making new folder for 3D Asset file')

# storing_Folder = ''

# New_Folder = st.text_input("Create a new Folder for 3D Asset : ")

# if st.button('Create Folder'):
#    st.button(New_Folder)

#    storing_Folder = New_Folder

# if st.button(storing_Folder, key=storing_Folder):

#    Image_Processing.Filter_Move_File(Base_file,Image_file,parent_dir, storing_Folder)