import streamlit as st
from PIL import Image
import os
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.preprocessing import image
import cv2
import random
import shutil
import ExcelAlphabetic
import json

Saved_AI_Folder = "C:/Users/USER/Kiryu KaeTamah Yutado/AI/"

def Upload_Image_File(image_file):
   if image_file is not None:
        file_details = {"FileName":image_file.name,"FileType":image_file.type}
        # st.write(file_details)
        img = Image.open(image_file)
        st.image(img)
        # with open(os.path.join(Saved_AI_Folder,image_file.name),"wb") as f: 
        #    f.write(image_file.getbuffer())         
        st.success("Saved File")

def Read_Image_File(image_file):
    if image_file is not None:
        file_details = {"FileName":image_file.name,"FileType":image_file.type}
        return image_file.name
    
def Store_Image_File(Image_file, Image_Datastore):
    for file in os.listdir(Image_file):

        Image_Datastore.append(file)

    if Image_Datastore:
        Image_File_Iter = iter(Image_Datastore)

        Image_File_Next = next(Image_File_Iter)

        Format_Image = Image_File_Next[-4:]
    # Automated the Image in the Default folder (Jadi semua gambar digabungkan / test dulu jangan maen langsung dihapus yang Favorite)
        if (Format_Image in ".jpg" or Format_Image in ".png" or Format_Image in ".JPG" or Format_Image in ".PNG" or Format_Image in ".jpeg" or Format_Image in ".JPEG"):
            img = Image.open(os.path.join(Image_file, Image_File_Next))
            st.image(img)
            # st.write(img)
        elif (Format_Image in ".MP4" or Format_Image in ".mp4" or Format_Image in ".mkv" or Format_Image in ".MKV"):
            # video_file = open(Image_File_Next, 'rb')
            # video_bytes = video_file.read()

            with open(os.path.join(Image_file, Image_File_Next), 'rb') as v:
                st.video(v)
            st.write(v)
    else:
        st.write("There is no more File")

def Filter_Move_File(Image_File, Image_Datastore, Parent_Directory, Store_Filter):

    for file in os.listdir(Image_File):

        Image_Datastore.append(file)

    Image_File_Iter = iter(Image_Datastore)

    Image_File_Next = next(Image_File_Iter)

    directory = Store_Filter
    path = os.path.join(Parent_Directory, directory)
    pathExist = os.path.exists(path)

    if not pathExist:
        os.mkdir(path)
        
    old_file = os.path.join(Image_File, Image_File_Next)
    destination_file = os.path.join(path, Image_File_Next)

    if not os.path.exists(destination_file):
        os.rename(old_file, destination_file)
        st.write("Moved file to " + Store_Filter)
    else:
        st.write("The file is already exists")

def Renamed_Files(parent_path, Rename_file):

    # ExcelAlphabetic.InputColumnsExcelData(Input_Column,Excel)
    Image_Attribute = {}
    # Excel_Data = len(Input_Column.split()) looping trus jadi 1 class method tapi bagaimana cara bisa memprediksi itu attribute diinsert dimana 

    # Excel["A" + str(1)] = "File Key"
    # Excel["B" + str(1)] = "File Name"
    # Excel["C" + str(1)] = "File FormatFile"
    # Excel["D" + str(1)] = "File Location" 
    # Excel["E" + str(1)] = "File height"
    # Excel["F" + str(1)] = "File width"
    # Excel["G" + str(1)] = "File Format"
    # Excel["H" + str(1)] = "File Classification"

    i = 1
    for file_name in range(len(os.listdir(parent_path)) - 1):

        img_format = os.listdir(parent_path)[file_name][-3:]
        source = str(parent_path) + "/" + str(os.listdir(parent_path)[file_name])

        Image_Attribute_Sub = {}

        try:
            Img = Image.open(source)
            pivot = i
        # st.write(source)
            destination = str(parent_path) + "/" + str(Rename_file) + " " + str(i) + "." + str(img_format).lower()
        # st.write(destination)

            if not os.path.exists(destination):
                os.rename(source,destination)

            Image_Attribute_Sub["File Key"] = Rename_file + "_" + str(i)
            Image_Attribute_Sub["File Name"] = Rename_file + " " + str(i)
            Image_Attribute_Sub["File FormatFile"] = str(Rename_file) + " " + str(i) + "." + str(img_format).lower()
            Image_Attribute_Sub["File Location"] = destination 
            Image_Attribute_Sub["File height"] = Img.height
            Image_Attribute_Sub["File width"] = Img.width
            Image_Attribute_Sub["File Format"] = img_format
            Image_Attribute_Sub["File Classification"] = Rename_file
            Image_Attribute_Sub["File Orchestrator Key"] = Rename_file + " File" + str(1)

            Image_Attribute[i] = Image_Attribute_Sub
            i += 1


        except:
            pivot = i
        # st.write(source)
            destination = str(parent_path) + "/" + str(Rename_file) + " " + str(i) + "." + str(img_format).lower()
        # st.write(destination)

            if not os.path.exists(destination):
                os.rename(source,destination)

            Image_Attribute_Sub["File Key"] = Rename_file + "_" + str(i)
            Image_Attribute_Sub["File Name"] = Rename_file + " " + str(i)
            Image_Attribute_Sub["File FormatFile"] = str(Rename_file) + " " + str(i) + "." + str(img_format).lower()
            Image_Attribute_Sub["File Location"] = destination 
            Image_Attribute_Sub["File Format"] = img_format
            Image_Attribute_Sub["File Classification"] = Rename_file
            Image_Attribute_Sub["File Orchestrator Key"] = Rename_file + " File" + str(1)

            Image_Attribute[i] = Image_Attribute_Sub

            i += 1
    
    with open('json_data.json', 'w') as outfile:
        json.dump(Image_Attribute, outfile)
    
    # ada 2 jalan 1 lebih bagus pake database atau dataset, Kayaknya dataset sih tapi pake apa
    Storing_File_Dataset(Rename_file + " File")

def Storing_File_Dataset(Data_Name):

    File_Name = Data_Name + " File"

    if not os.path.exists(File_Name):
        # Create dataset
        st.write("Create Dataset and Store File data")
        Image_orches_file = {}

        Image_orches_file["file_Key"] = File_Name + str(1)
        Image_orches_file["file_name"] = File_Name
        Image_orches_file["Description"] = File_Name + "Data ini isinya adalah file yang distore ke JSON"

        with open('json_data_cloud.json', 'w') as outfile:
            json.dump(Image_orches_file, outfile)
        # file_data["File_Name"].append(new_data)
    else:
        # Overwrite data
        Image_orches_file = json.loads('json_data_cloud.json')
        # file_data["File_Name"].update(new_data)
        st.write("Overwrite File dataset")
        with open('json_data_cloud.json', 'w') as outfile:
            json.dump(Image_orches_file, outfile)

def Auto_Capture_Image_From_Video(Video_File, Create_Folder, Rename_File = ""):

    VideoSource = cv2.VideoCapture(Video_File)

    CurrentImageFrame = 1
    File_Take = ""

    if (Video_File.find("/")):
        Spliter = Video_File.split("/")
        File_Take = Spliter[len(Spliter) - 1]
        
    else:
        File_Take = Video_File

    New_folder = os.path.join("C:/Users/USER/Kiryu KaeTamah Yutado/MachineLearning/Train/",Create_Folder)
    pathExist = os.path.exists(New_folder)
    if not pathExist:
        os.mkdir(New_folder)

    st.write(New_folder)
    while(True):

        ret, frame = VideoSource.read()
        if ret:
            if Rename_File != "":
                Image_name = New_folder + "/" + File_Take.replace(File_Take,Rename_File) + " " + str(CurrentImageFrame) +".png"
                cv2.imwrite(Image_name,frame)
            else:
                Image_name = New_folder + "/" + File_Take.replace(".mp4","") + " " + str(CurrentImageFrame) +".png"
                cv2.imwrite(Image_name,frame)
            CurrentImageFrame += 1
        else:
            break
    
    VideoSource.release()
    cv2.destroyAllWindows()

    st.write("Video Image has been created into Dataset Image in this folder")

def Train_Dataset(dataset):
    train_datagen = ImageDataGenerator(
                rescale = 1./255,
                shear_range = 0.2,
                zoom_range = 0.2,
                horizontal_flip=True)

    training_set = train_datagen.flow_from_directory(
                  dataset,# '/content/drive/MyDrive/Dataset Sertifikat/Train',
                  target_size = (150,150),
                  batch_size = 32,
                  class_mode = 'categorical')
    
def Create_Test_Dataset(dataset, place_dataset, test_value):

    Datatest = []

    New_Test_Dataset = "C:/Users/USER/Kiryu KaeTamah Yutado/MachineLearning/Test/" + place_dataset
    pathexist = os.path.exists(New_Test_Dataset)

    if not pathexist:
        os.mkdir(New_Test_Dataset)

    test_data_value = (test_value/100) * len(os.listdir(dataset))

    for file in os.listdir(dataset):

        Datatest.append(file)

    for insert_file in range(int(test_data_value)):
        # save file
        
        Select_random_file = random.choice(Datatest)
        # st.write(Select_random_file)
        # st.write(os.path.join(New_Test_Dataset, Select_random_file))
        shutil.copyfile(os.path.join(dataset,Select_random_file) ,os.path.join(New_Test_Dataset, Select_random_file))
        
        Datatest.remove(Select_random_file)
        
        # Remove list DataTest file
    

def Test_Dataset(dataset):
    test_datagen = ImageDataGenerator(rescale = 1./255)

    test_set = test_datagen.flow_from_directory(
                  dataset, # '/content/drive/MyDrive/Dataset Sertifikat/Test',
                  target_size = (150,150),
                  batch_size = 32,
                  class_mode = 'categorical')

def Basic_CNN(training_set, test_set, epoch):

    cnn = tf.keras.models.Sequential()

    cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation="relu", input_shape=[150,150,3]))
    cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

    cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation="relu"))
    cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

    cnn.add(tf.keras.layers.Flatten())

    cnn.add(tf.keras.layers.Dense(units=128, activation="relu"))

    cnn.add(tf.keras.layers.Dense(units=3, activation="softmax"))

    cnn.compile(optimizer="adam", loss = "categorical_crossentropy", metrics=["accuracy"])

    cnn.fit(x = training_set, validation_data = test_set, epochs = epoch) # 25 epochs is enough

def Prediction(Image_data, cnn):
    test_image = image.load_img(Image_data , target_size=(150,150))
    test_images = image.img_to_array(test_image)
    test_images2 = np.expand_dims(test_images, axis = 0)

    result = cnn.predict(test_images2)
    # training_set.class_indices

    if result[0][0] == 1:
        print("Result : " , result[0][0])
        # print("Sertifikat")
    else:
        print("Result : " , result[0][0])
        # print("Lain-Lain")

def train_CNN_image(dataset):
    data = dataset

    Training_set = Train_Dataset(data)
    
    if len(data) == 0:
        Create_Test_Dataset(data, "Data Test Folder data", 20)

    Test_set = Test_Dataset(data)

    cnn = Basic_CNN(Training_set,Test_set, 25)

    return cnn

def Image_Attribute_Data(dataset):

    image_file = dataset
    if image_file is not None:
        file_details = {"FileId": image_file.id, "FileName":image_file.name,"FileType":image_file.type}
        st.write("File Key ID : ", image_file.id)
        st.write("Filename : ", image_file.name)
        st.write("FileType : ", image_file.type)
        st.write("FileSize : ", image_file.size)
        img = Image.open(image_file)

        st.write("FileKey : " , str(image_file.name) + "_" + str(img.getdata())[23:len(str(img.getdata())) - 1] + str(image_file.id))
        st.write("Filename : ", image_file.name)
        st.write("FileDescription : ", img.format_description)
        st.write("FileType : ", img.format)
        st.write("FileSize : ", img.size)
        for key, value in img.info.items():
            st.write("Image Properties : ", key)
            st.write("Image properties value : ", value)
        # # st.write("")
        return file_details

## 3D models    
