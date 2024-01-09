import json
import math
from pathlib import Path
import os


def is_json_key_present(json, key):
    try:
        buf = json[key]
    except KeyError:
        return False
    except IndexError:
        return False

    return True

folder_path = os.getcwd()
os.chdir(folder_path)
files = os.listdir(folder_path)

for file in files:
    if '.json' in file:
        with open(file, 'rt', encoding='UTF8') as Jsonfile:
            JsonData = json.load(Jsonfile)
        break
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

    JsonFileName = JsonData['data'][image_num]['fileName']
    JsonFileName = Path(JsonFileName).stem
    JsonFileName = JsonFileName + '.txt'
    JsonFilePath = 'Image/' + JsonFileName

    with open((JsonFilePath),'w') as f:

        label_num = 0
        flag_label_num = True
        while flag_label_num:
        # for label_num in range(0,10):
            if is_json_key_present(JsonData['data'][image_num]['regionLabel'], label_num):
                flag_label_num = True
            else:
                flag_label_num = False
                break

            ClassName = JsonData['data'][image_num]['regionLabel'][label_num]['className']

            if ClassName == 'class1':
                ClassName = str(0)
            if ClassName == 'class2':
                ClassName = str(1)
            if ClassName == 'class3':
                ClassName = str(2)
            if ClassName == 'class4':
                ClassName = str(3)
            if ClassName == 'class5':
                ClassName = str(4)
            if ClassName == 'class6':
                ClassName = str(5)

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

    image_num += 1