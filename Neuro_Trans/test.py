# import json
import math
from pathlib import Path
import os
import cv2
import matplotlib.pyplot as plt
import json
import natsort


def is_json_key_present(json, key):
    try:
        buf = json[key]
    except KeyError:
        return False
    except IndexError:
        return False

    return True


JsonFilePath = 'test01.json'
with open(JsonFilePath, 'r') as JF:
    JsonData = json.load(JF)
print(JsonData)

folder_path = os.getcwd() + '\\mark_to_neuro_imgtxt'
os.chdir(folder_path)
folder_files = os.listdir(folder_path)
folder_files = natsort.natsorted(folder_files)

folder_files_count = 0
for file in folder_files:
    if folder_files_count >= len(folder_files)/2-1:
        break
    if '.bmp' in file or '.jpg' in file or '.jpeg' in file or '.png' in file:
        Imagefile = file
        Txtfile = os.path.splitext(Imagefile)[0] + '.txt'
    elif '.txt' in file:
        continue

    img = cv2.imread(Imagefile, cv2.IMREAD_GRAYSCALE)
    img_height, img_width = img.shape

    Imagefile = os.path.splitext(file)[0] + '.png'

    JsonData['data'].append({
        "fileName": Imagefile,
        "set": "",
        "classLabel": "",
        "regionLabel": [
        ],
        "retestset": 0,
        "rotation_angle": 0,
        "width": img_width,
        "height": img_height
    })

    LineCount = 0
    flag_image_num = True
    while True:
        with open(Txtfile, 'r', encoding='UTF8') as FT:
            line = FT.readlines()
            if is_json_key_present(line, LineCount):
                flag_image_num = True
            else:
                flag_image_num = False
                break


            line[LineCount] = line[LineCount].strip()
            line[LineCount] = line[LineCount].split(' ')
            yolo_c = line[LineCount][0]
            yolo_x = line[LineCount][1]
            yolo_y = line[LineCount][2]
            yolo_w = line[LineCount][3]
            yolo_h = line[LineCount][4]

            print(yolo_c, yolo_x, yolo_y, yolo_w, yolo_h)

            if yolo_c == '1':
                Neuro_classname = "class1"
            elif yolo_c == '0':
                Neuro_classname = "class0"

            Neuro_X = (float(yolo_x) * img_width) - (float(yolo_w) * img_width / 2)
            Neuro_X = int(Neuro_X)
            print(Neuro_X)

            Neuro_Y = (float(yolo_y) * img_height) - (float(yolo_h) * img_height / 2)
            Neuro_Y = int(Neuro_Y)
            print(Neuro_Y)

            Neuro_W = float(yolo_w) * img_width
            Neuro_W = int(Neuro_W)
            print(Neuro_W)

            Neuro_H = float(yolo_h) * img_height
            Neuro_H = int(Neuro_H)
            print(Neuro_H)


            JsonData['data'][folder_files_count]['regionLabel'].append({
                  "className": Neuro_classname,
                  "type": "Rect",
                  "x": Neuro_X,
                  "y": Neuro_Y,
                  "width": Neuro_W,
                  "height": Neuro_H
            })

            JsonFilePath = 'C:\\Users\\nse3d\\PycharmProjects\\BasicProject\\test01.json'
            with open(JsonFilePath, 'w') as outfile:
                json.dump(JsonData, outfile)

        LineCount += 1
    folder_files_count += 1
