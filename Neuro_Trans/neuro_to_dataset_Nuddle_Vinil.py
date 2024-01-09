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
    root.folderpath = filedialog.askdirectory(initialdir="./", title="Open Data folder")
    folder_path = root.folderpath
    return folder_path

def file_select():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(initialdir="./", title="select a file")
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
        dataset_train = dataset_folder + "\\" + "train"
        dataset_test = dataset_folder + "\\" + "test"
        dataset_valid = dataset_folder + "\\" + "valid"
        dataset_not_used = dataset_folder + "\\" + "not_used"

        os.makedirs(dataset_train)
        os.makedirs(dataset_test)
        os.makedirs(dataset_valid)
        os.makedirs(dataset_not_used)

        dataset_train_OK = dataset_train + "\\" + "OK"
        dataset_train_NG = dataset_train + "\\" + "NG"
        dataset_test_OK = dataset_test + "\\" + "OK"
        dataset_test_NG = dataset_test + "\\" + "NG"
        dataset_valid_OK = dataset_valid + "\\" + "OK"
        dataset_valid_NG = dataset_valid + "\\" + "NG"
        dataset_not_used_Empty = dataset_not_used + "\\" + "[]"
        dataset_not_used_OK = dataset_not_used + "\\" + "OK"
        dataset_not_used_NG = dataset_not_used + "\\" + "NG"

        os.makedirs(dataset_train_OK)
        os.makedirs(dataset_train_NG)
        os.makedirs(dataset_test_OK)
        os.makedirs(dataset_test_NG)
        os.makedirs(dataset_valid_OK)
        os.makedirs(dataset_valid_NG)
        os.makedirs(dataset_not_used_Empty)
        os.makedirs(dataset_not_used_OK)
        os.makedirs(dataset_not_used_NG)

            
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
        if data_classLabel == "OK":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "train" + "\\" + "OK"
        elif data_classLabel == "NG":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "train" + "\\" + "NG"
        else:
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "train" + "\\" + "[]"

    elif data_set == "test":
        if data_classLabel == "OK":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "test" + "\\" + "OK"
        elif data_classLabel == "NG":
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "test" + "\\" + "NG"
        else:
            source_image_path = folder_path + "\\" + data_fileNmae
            destination_folder_path = dataset_folder + "\\" + "test" + "\\" + "[]"
            
    elif data_set == "not_used":
            if data_classLabel == "OK":
                source_image_path = folder_path + "\\" + data_fileNmae
                destination_folder_path = dataset_folder + "\\" + "not_used" + "\\" + "OK"
            elif data_classLabel == "NG":
                source_image_path = folder_path + "\\" + data_fileNmae
                destination_folder_path = dataset_folder + "\\" + "not_used" + "\\" + "NG"
            else:
                source_image_path = folder_path + "\\" + data_fileNmae
                destination_folder_path = dataset_folder + "\\" + "not_used" + "\\" + "[]"

                
    shutil.copy(source_image_path, destination_folder_path)
    image_num += 1