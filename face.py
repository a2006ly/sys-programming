# -*- coding: utf-8 -*-
# 画像からカスケード分類器を用いて顔認識を行うサンプル
 
import cv2
#http://www.takunoko.com/blog/python%E3%81%A7%E9%81%8A%E3%82%93%E3%81%A7%E3%81%BF%E3%82%8B-part1-opencv%E3%81%A7%E9%A1%94%E8%AA%8D%E8%AD%98/
# サンプル顔認識特徴量ファイル
#cascade_path = "../lib/haarcascades/haarcascade_frontalface_alt.xml"
cascade_path="C:/Users/user/Desktop/workspace/doc/sysp/haarcascade_frontalface_alt.xml"
path="C:/Users/user/Desktop/workspace/doc/sysp/"
image_path = path + "Lenna-300x300.jpg"

 
# これは、BGRの順になっている気がする
color = (255, 255, 255) #白
 
# 画像の読み込み
image = cv2.imread(image_path)
# グレースケール変換
#gray = cv2.cvtColor(image, cv2.cv.CV_BGR2GRAY)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
dst_image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
 
# 分類器を作る?みたいな作業
cascade = cv2.CascadeClassifier(cascade_path)
 
# 顔認識の実行
facerect = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
 
if len(facerect) > 0:
  # 検出した顔を囲む矩形の作成
  for rect in facerect:
    #cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)
     image = image[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]]
else:
  print("no face")


# 認識結果の表示
cv2.imshow("detected.jpg", image)
 
# 何かキーが押されたら終了
while(1):
  if cv2.waitKey(10) > 0:
    break