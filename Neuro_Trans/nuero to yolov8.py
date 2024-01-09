import json
import math
from pathlib import Path
import os

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

        # # Dataset -> train -> Class 생성
        # dataset_train_OK = dataset_train + "\\" + "OK"
        # dataset_train_NG = dataset_train + "\\" + "NG"
        # dataset_train_not_used = dataset_train + "\\" + "not_used"
        
        # os.makedirs(dataset_train_OK)
        # os.makedirs(dataset_train_NG)
        # os.makedirs(dataset_train_not_used)

        # # Dataset -> valid -> Class 생성
        # dataset_valid_OK = dataset_valid + "\\" + "OK"
        # dataset_valid_NG = dataset_valid + "\\" + "NG"
        # dataset_valid_not_used = dataset_valid + "\\" + "not_used"
        
        # os.makedirs(dataset_valid_OK)
        # os.makedirs(dataset_valid_NG)
        # os.makedirs(dataset_valid_not_used)

        # # Dataset -> test -> Class 생성
        # dataset_test_OK = dataset_test + "\\" + "OK"
        # dataset_test_NG = dataset_test + "\\" + "NG"
        # dataset_test_not_used = dataset_test + "\\" + "not_used"
        
        # os.makedirs(dataset_test_OK)
        # os.makedirs(dataset_test_NG)
        # os.makedirs(dataset_test_not_used)

        # Dataset -> not_used -> Class 생성
        dataset_not_used_OK = dataset_not_used + "\\" + "OK"
        dataset_not_used_NG = dataset_not_used + "\\" + "NG"
        dataset_not_used_not_used = dataset_not_used + "\\" + "not_used"
        
        os.makedirs(dataset_not_used_OK)
        os.makedirs(dataset_not_used_NG)
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

## Json 파일 선택
file_path = file_select()
with open(file_path, 'rt', encoding='UTF8') as Jsonfile:
    JsonData = json.load(Jsonfile)

## Json 파일 파씽
json.dumps(JsonData, indent=2, ensure_ascii=False)


## 라벨셋 저장
image_num = 0
flag_image_num = True
while flag_image_num:
    if is_json_key_present(JsonData['data'], image_num):
        flag_image_num = True
    else:
        flag_image_num = False
        break

    JsonFileName = JsonData['data'][image_num]['fileName']
    JsonFileName = Path(JsonFileName).stem
    JsonFileName = JsonFileName + '.txt'
    JsonFilePath = folder_path + '/' + JsonFileName

    ## 데이터셋 이동 
    data_fileNmae = JsonData['data'][image_num]['fileName']
    data_set = JsonData['data'][image_num]['set']

    with open((JsonFilePath),'w') as f:

        label_num = 0
        flag_label_num = True
        while flag_label_num:
            if is_json_key_present(JsonData['data'][image_num]['regionLabel'], label_num):
                flag_label_num = True
            else:
                flag_label_num = False
                break

            ClassName = JsonData['data'][image_num]['regionLabel'][label_num]['className']

            if ClassName == 'NG':
                ClassName = str(0)
            if ClassName == 'OK':
                ClassName = str(1)
            # if ClassName == 'class3':
            #     ClassName = str(2)
            # if ClassName == 'class4':
            #     ClassName = str(3)
            # if ClassName == 'class5':
            #     ClassName = str(4)
            # if ClassName == 'class6':
            #     ClassName = str(5)

            yolo_X = (JsonData['data'][image_num]['regionLabel'][label_num]['x'] + (JsonData['data'][image_num]['regionLabel'][label_num]['width'] / 2)) / JsonData['data'][image_num]['width']
            yolo_Y = (JsonData['data'][image_num]['regionLabel'][label_num]['y'] + (JsonData['data'][image_num]['regionLabel'][label_num]['height'] / 2)) / JsonData['data'][image_num]['height']
            yolo_width = JsonData['data'][image_num]['regionLabel'][label_num]['width'] / JsonData['data'][image_num]['width']
            yolo_height = JsonData['data'][image_num]['regionLabel'][label_num]['height'] / JsonData['data'][image_num]['height']

            yolo_X = round(yolo_X, 6)
            yolo_Y = round(yolo_Y, 6)
            yolo_width = round(yolo_width, 6)
            yolo_height = round(yolo_height, 6)

            yolo_X = format(yolo_X, ".6f")
            yolo_Y = format(yolo_Y, ".6f")
            yolo_width = format(yolo_width, ".6f")
            yolo_height = format(yolo_height, ".6f")

            data = (ClassName + ' ' + str(yolo_X) + ' ' + str(yolo_Y) + ' ' + str(yolo_width) + ' ' + str(yolo_height))

            f.write(data + '\n')

            label_num += 1
            

    ## 데이터셋 이동 
    if data_set == "train":
        source_image_path = folder_path + "\\" + data_fileNmae
        destination_folder_path = dataset_folder + "\\" + "train"

        file_label_txt = Path(data_fileNmae).stem + '.txt'
        before_label_path = folder_path + "\\" + file_label_txt
        destination_label_path = dataset_folder + "\\" + "train"

    elif data_set == "test":
        source_image_path = folder_path + "\\" + data_fileNmae
        destination_folder_path = dataset_folder + "\\" + "test"

        file_label_txt = Path(data_fileNmae).stem + '.txt'
        before_label_path = folder_path + "\\" + file_label_txt
        destination_label_path = dataset_folder + "\\" + "test"

    else:
        source_image_path = folder_path + "\\" + data_fileNmae
        destination_folder_path = dataset_folder + "\\" + "not_used"

        file_label_txt = Path(data_fileNmae).stem + '.txt'
        before_label_path = folder_path + "\\" + file_label_txt
        destination_label_path = dataset_folder + "\\" + "not_used"
        
    shutil.copy(source_image_path, destination_folder_path)
    shutil.copy(before_label_path, destination_label_path)


    image_num += 1