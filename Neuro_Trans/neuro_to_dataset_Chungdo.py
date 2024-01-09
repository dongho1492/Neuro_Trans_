import json
import math
from pathlib import Path
import os
# import numpy as np
# import pandas as pd
# import natsort
from tkinter import *
from tkinter import filedialog
import shutil

def is_json_key_present(json, key):
    try:
        buf = json[key]
    except KeyError:
        return False
    except IndexError:
        return False

    return True

def folder_select():
    ## 특정 경로 선택 및 저장
    root = Tk()
    root.withdraw()
    root.folderpath = filedialog.askdirectory(initialdir="./", title="Select Dataset folder")
    folder_path = root.folderpath
    return folder_path

def file_select():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(initialdir="./", title="select JSON file")
    return file_path

def create_folder_after(path):
    try:
        pre_path = os.path.dirname(path)
        path_folder_name = os.path.basename(path)
        after_folder = pre_path + "\\" + path_folder_name + "_Dataset"
        if not os.path.exists(after_folder):
            os.makedirs(after_folder)
    except:
        OSError: print("Error: failed to create the folder")
        
def create_dataset_folder(dataset_folder):
    try:
        # Dataset -> train/valid/test/not_used 생성
        dataset_train = dataset_folder + "\\" + "train"
        dataset_test = dataset_folder + "\\" + "test"
        dataset_valid = dataset_folder + "\\" + "valid"
        dataset_not_used = dataset_folder + "\\" + "not_used"

        os.makedirs(dataset_train)
        os.makedirs(dataset_test)
        os.makedirs(dataset_valid)
        os.makedirs(dataset_not_used)

        # Dataset -> train -> Class 생성
        dataset_train_OK = dataset_train + "\\" + "정상"
        dataset_train_Hair = dataset_train + "\\" + "머리카락"
        dataset_train_Vinil = dataset_train + "\\" + "비닐"
        dataset_train_Sil = dataset_train + "\\" + "실"
        dataset_train_Plant = dataset_train + "\\" + "식물"
        dataset_train_Paper = dataset_train + "\\" + "종이"
        dataset_train_Wood = dataset_train + "\\" + "나무"
        dataset_train_not_used = dataset_train + "\\" + "not_used"
        
        os.makedirs(dataset_train_OK)
        os.makedirs(dataset_train_Hair)
        os.makedirs(dataset_train_Vinil)
        os.makedirs(dataset_train_Sil)
        os.makedirs(dataset_train_Plant)
        os.makedirs(dataset_train_Paper)
        os.makedirs(dataset_train_Wood)
        os.makedirs(dataset_train_not_used)

        # Dataset -> valid -> Class 생성
        dataset_valid_OK = dataset_valid + "\\" + "정상"
        dataset_valid_Hair = dataset_valid + "\\" + "머리카락"
        dataset_valid_Vinil = dataset_valid + "\\" + "비닐"
        dataset_valid_Sil = dataset_valid + "\\" + "실"
        dataset_valid_Plant = dataset_valid + "\\" + "식물"
        dataset_valid_Paper = dataset_valid + "\\" + "종이"
        dataset_valid_Wood = dataset_valid + "\\" + "나무"
        dataset_valid_not_used = dataset_valid + "\\" + "not_used"
        
        os.makedirs(dataset_valid_OK)
        os.makedirs(dataset_valid_Hair)
        os.makedirs(dataset_valid_Vinil)
        os.makedirs(dataset_valid_Sil)
        os.makedirs(dataset_valid_Plant)
        os.makedirs(dataset_valid_Paper)
        os.makedirs(dataset_valid_Wood)
        os.makedirs(dataset_valid_not_used)

        # Dataset -> test -> Class 생성
        dataset_test_OK = dataset_test + "\\" + "정상"
        dataset_test_Hair = dataset_test + "\\" + "머리카락"
        dataset_test_Vinil = dataset_test + "\\" + "비닐"
        dataset_test_Sil = dataset_test + "\\" + "실"
        dataset_test_Plant = dataset_test + "\\" + "식물"
        dataset_test_Paper = dataset_test + "\\" + "종이"
        dataset_test_Wood = dataset_test + "\\" + "나무"
        dataset_test_not_used = dataset_test + "\\" + "not_used"
        
        os.makedirs(dataset_test_OK)
        os.makedirs(dataset_test_Hair)
        os.makedirs(dataset_test_Vinil)
        os.makedirs(dataset_test_Sil)
        os.makedirs(dataset_test_Plant)
        os.makedirs(dataset_test_Paper)
        os.makedirs(dataset_test_Wood)
        os.makedirs(dataset_test_not_used)

        # Dataset -> not_used -> Class 생성
        dataset_not_used_OK = dataset_not_used + "\\" + "정상"
        dataset_not_used_Hair = dataset_not_used + "\\" + "머리카락"
        dataset_not_used_Vinil = dataset_not_used + "\\" + "비닐"
        dataset_not_used_Sil = dataset_not_used + "\\" + "실"
        dataset_not_used_Plant = dataset_not_used + "\\" + "식물"
        dataset_not_used_Paper = dataset_not_used + "\\" + "종이"
        dataset_not_used_Wood = dataset_not_used + "\\" + "나무"
        dataset_not_used_not_used = dataset_not_used + "\\" + "not_used"
        
        os.makedirs(dataset_not_used_OK)
        os.makedirs(dataset_not_used_Hair)
        os.makedirs(dataset_not_used_Vinil)
        os.makedirs(dataset_not_used_Sil)
        os.makedirs(dataset_not_used_Plant)
        os.makedirs(dataset_not_used_Paper)
        os.makedirs(dataset_not_used_Wood)
        os.makedirs(dataset_not_used_not_used)

    except:
        OSError: print("Error: failed to create the folder")



## 특정 경로 선택 및 저장
folder_path = folder_select()
        
# 특정경로에 폴더 만들기
global after_folder
dataset_folder = os.path.dirname(folder_path) + "\\" + os.path.basename(folder_path) + "_Dataset"
create_folder_after(folder_path)
create_dataset_folder(dataset_folder)

file_path = file_select()
with open(file_path, 'rt', encoding='UTF8') as Jsonfile:
            JsonData = json.load(Jsonfile)
            
json.dumps(JsonData, indent=2, ensure_ascii=False)

image_num = 0
flag_image_num = True
while flag_image_num:
# for image_num in range(0,10):
    if is_json_key_present(JsonData['data'], image_num):
        flag_image_num = True
    else:
        flag_image_num = False
        break

    data_fileNmae = JsonData['data'][image_num]['fileName']
    data_set = JsonData['data'][image_num]['set']
    data_classLabel = JsonData['data'][image_num]['classLabel']        
        
    if data_set == "train":
        if data_classLabel == "정상":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "train" + "\\" + "정상"
        elif data_classLabel == "머리카락":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "train" + "\\" + "머리카락"
        elif data_classLabel == "비닐":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "train" + "\\" + "비닐"
        elif data_classLabel == "실":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "train" + "\\" + "실"
        elif data_classLabel == "식물":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "train" + "\\" + "식물"
        elif data_classLabel == "종이":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "train" + "\\" + "종이"
        elif data_classLabel == "나무":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "train" + "\\" + "나무"
        else:
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "train" + "\\" + "not_used"

    elif data_set == "test":
        if data_classLabel == "정상":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "test" + "\\" + "정상"
        elif data_classLabel == "머리카락":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "test" + "\\" + "머리카락"
        elif data_classLabel == "비닐":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "test" + "\\" + "비닐"
        elif data_classLabel == "실":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "test" + "\\" + "실"
        elif data_classLabel == "식물":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "test" + "\\" + "식물"
        elif data_classLabel == "종이":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "test" + "\\" + "종이"
        elif data_classLabel == "나무":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "test" + "\\" + "나무"
        else:
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "test" + "\\" + "not_used"
            
    else : # data_set == "not_used":
        if data_classLabel == "정상":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "not_used" + "\\" + "정상"
        elif data_classLabel == "머리카락":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "not_used" + "\\" + "머리카락"
        elif data_classLabel == "비닐":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "not_used" + "\\" + "비닐"
        elif data_classLabel == "실":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "not_used" + "\\" + "실"
        elif data_classLabel == "식물":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "not_used" + "\\" + "식물"
        elif data_classLabel == "종이":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "not_used" + "\\" + "종이"
        elif data_classLabel == "나무":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "not_used" + "\\" + "나무"
        else:
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "not_used" + "\\" + "not_used"

                
    shutil.copy(source_image_path, destination_folder_path)
    image_num += 1