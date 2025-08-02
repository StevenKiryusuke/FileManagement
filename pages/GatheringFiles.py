import streamlit as st
import os
import Image_Processing

# Ada 3 choice Gathering Files yaitu 

# 1. Ambil dari Download data karena ini pasti default kalau setiap di file
# 2. Ambil dari server lokal contohnya kayak bikin aplikasi mobile / website kemudian distore ke dalam file
# 3. Ambil dari cloud storage (Paling nyaman ini karena ini mirip seperti GitHub)

# Tapi namanya file image kalau random download itu fix udh harus
# Pake teknik Machine Learning & Computer Vision

# Default data yang akan dipindahkan ke sini (Ini untuk choice 1)
Downloaded_Data = os.path.join(os.path.expanduser("~"), "Downloads")

# Default operating system menggunakan method Expanduser 
st.title("Files from Windows Operating System")

Downloads1, Screenshots2, videos3 = st.columns(3)
# st.write("Downloaded_Data ", os.path(Downloaded_Data))

with Downloads1:
    if st.button("Downloaded Data"): # Take data file from Downloaded Data
        Downloaded_Data = os.path.join(os.path.expanduser("~"), "Downloads")

        for file in os.listdir(Downloaded_Data):
    
            Format_File = file[-4:]

            if Format_File in ".png" or Format_File in ".jpg":
                # st.write("Image File")
                # st.write(os.path.join(Downloaded_Data,file))
        # Image_Processing.Filter_Move_File(Downloaded_Data,Store_data,"C:/Users/USER/Kiryu KaeTamah Yutado/3D_CharacterModel","Sample Image")

        # Image_File_Iter = iter(Image_Datastore)

        # Image_File_Next = next(Image_File_Iter)

                # Parent_Directory = "C:/Users/USER/Kiryu KaeTamah Yutado"
                Parent_Directory = os.path.join(os.path.expanduser("~"), "Kiryu KaeTamah Yutado")
                directory = "Big Data"
                path = os.path.join(Parent_Directory, directory)
                pathExist = os.path.exists(path)

                if not pathExist:
                    os.mkdir(path)
        
                old_file = os.path.join(Downloaded_Data, file)
                destination_file = os.path.join(path, file)

                if not os.path.exists(destination_file):
                    os.rename(old_file, destination_file)
                    # st.write("Moved file to " + directory)
                # else:
                    # st.write("The file is already exists")

            if Format_File in ".mp4" or Format_File in ".mkv":
                # st.write("Video File")
                # st.write(os.path.join(Downloaded_Data,file))

            # Image_File_Iter = iter(Image_Datastore)

            # Image_File_Next = next(Image_File_Iter)

                # Parent_Directory = "C:/Users/USER/Kiryu KaeTamah Yutado"
                Parent_Directory = os.path.join(os.path.expanduser("~"), "Kiryu KaeTamah Yutado")
                directory = "Big Data"
                path = os.path.join(Parent_Directory, directory)
                pathExist = os.path.exists(path)

                if not pathExist:
                    os.mkdir(path)
        
                old_file = os.path.join(Downloaded_Data, file)
                destination_file = os.path.join(path, file)

                if not os.path.exists(destination_file):
                    os.rename(old_file, destination_file)
                    # st.write("Moved file to " + directory)
                # else:
                    # st.write("The file is already exists")

        st.write("Moved all Downloaded files Complete")

with Screenshots2:
    if st.button("Screenshots"):
        Picture = os.path.join(os.path.expanduser("~"), "Pictures")
        Screenshot = os.path.join(Picture, "Screenshots")

    # st.write(Screenshot)

        for file in os.listdir(Screenshot):

            # Parent_Directory = "C:/Users/USER/Kiryu KaeTamah Yutado"
            Parent_Directory = os.path.join(os.path.expanduser("~"), "Kiryu KaeTamah Yutado")
            directory = "Big Data"
            path = os.path.join(Parent_Directory, directory)
            pathExist = os.path.exists(path)

            if not pathExist:
                os.mkdir(path)
        
            old_file = os.path.join(Screenshot, file)
            destination_file = os.path.join(path, file)

            if not os.path.exists(destination_file):
                os.rename(old_file, destination_file)
                # st.write("Moved file to " + directory)
            # else:
                # st.write("The file is already exists")
        st.write("Moved all Images files into Complete")

with videos3:
    if st.button("Videos"):
        Video = os.path.join(os.path.expanduser("~"), "Videos")
        Capture = os.path.join(Video, "Captures")

        for file in os.listdir(Capture):

            # Parent_Directory = "C:/Users/USER/Kiryu KaeTamah Yutado"
            Parent_Directory = os.path.join(os.path.expanduser("~"), "Kiryu KaeTamah Yutado")
            directory = "Big Data"
            path = os.path.join(Parent_Directory, directory)
            pathExist = os.path.exists(path)

            if not pathExist:
                os.mkdir(path)
        
            old_file = os.path.join(Capture, file)
            destination_file = os.path.join(path, file)

            if not os.path.exists(destination_file):
                os.rename(old_file, destination_file)
                # st.write("Moved file to " + directory)
            # else:
                # st.write("The file is already exists")

        st.write("Moved all Video files Complete")
# Sample_Image = "Image Folder"
# Sample_Video = "Video Folder"
# Sample_3D    = "3D Folder"

st.title("Files from Cloud Drive")