import json
import cv2
import glob
import os


file_path = "C:/Users/kimsu/sample/json/"
json_path ='*.json'
img_path ='*.jpg'
result_path = "C:/Users/kimsu/sample/result/"
a = glob.glob(os.path.join(file_path, json_path))
b = glob.glob(os.path.join(file_path, img_path))

for json_file, img_file in zip(a, b):

    with open(json_file, "r", encoding="UTF-8") as file:
        # print(json_file)

        data = json.load(file)
        xmin = data["labelingInfo"][1]['box']['boundingBox']['Xmin']
        xmax = data["labelingInfo"][1]['box']['boundingBox']['Xmax']
        ymin = data["labelingInfo"][1]['box']['boundingBox']['Ymin']
        ymax = data["labelingInfo"][1]['box']['boundingBox']['Ymax']
        # print(xmin, xmax, ymin, ymax)
        
        img = cv2.imread(img_file)
        result_img = cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (255,0,0), 5)
        # # rgb 이미지 보기
        cv2.imshow('rgb_image', img)
        cv2.waitKey(0) 
        
        # 이미지 저장=> 반복문으로 해야하나?
        cv2.imwrite(os.path.join(result_path,'save_img.jpg'), result_img)