import json
import cv2
import glob
import os

# glob.glob(path), os.listdir(path) 차이
# glob.glob은 경로명까지 전부 가져옴, os.listdir 파일명만 가져옴
# glob은 풀패스가 아니라 검색을 지정한 폴더로부터 상대경로를 반환

file_path = "C:/Users/kimsu/OneDrive/문서/GitHub/mmdetection_study/sample/json/"
json_path ='*.json'
img_path ='*.jpg'
result_path = "C:/Users/kimsu/OneDrive/문서/GitHub/mmdetection_study/sample/result/"

a = glob.glob(os.path.join(file_path, json_path)) # json 파일 전체 경로
b = glob.glob(os.path.join(file_path, img_path)) # 이미지 파일 전체 경로

# 
for json_file, img_file in zip(a, b):

    with open(json_file, "r", encoding="UTF-8") as file:
        # print(json_file)

        data = json.load(file)
        xmin = data["labelingInfo"][1]['box']['boundingBox']['Xmin']
        xmax = data["labelingInfo"][1]['box']['boundingBox']['Xmax']
        ymin = data["labelingInfo"][1]['box']['boundingBox']['Ymin']
        ymax = data["labelingInfo"][1]['box']['boundingBox']['Ymax']
        print(xmin, xmax, ymin, ymax)
        
        img = cv2.imread(img_file)
        cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (255,0,0), 5)
        # 이미지 보기
        #cv2.imshow('image', img)
        #cv2.waitKey(0) 
        
        # 이미지 저장=> 반복문으로 해야하나?
        # cv2.imwrite(os.path.join(result_path,'save_img_{}.jpg'.format(b)), img)