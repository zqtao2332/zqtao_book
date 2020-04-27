# coding: utf-8
# 
#   This example program shows how to use dlib's implementation of the paper:
#   One Millisecond Face Alignment with an Ensemble of Regression Trees by
#   Vahid Kazemi and Josephine Sullivan, CVPR 2014

import os
import cv2
import dlib
import glob

# 测试部分
# 导入训练好的模型文件

current_path = os.getcwd()
faces_path = current_path + '/testimg'

predictor = dlib.shape_predictor("predictor.dat")

detector = dlib.get_frontal_face_detector()
print("Showing detections and predictions on the images in the faces folder...")
for f in glob.glob(os.path.join(faces_path, "*.jpg")):
    print("Processing file: {}".format(f))
    img = cv2.imread(f)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dets = detector(img2, 1)
    print("Number of faces detected: {}".format(len(dets)))
    for index, face in enumerate(dets):
        print('face {}; left {}; top {}; right {}; bottom {}'.format(index, face.left(), face.top(), face.right(), face.bottom()))

        shape = predictor(img, face)
       
        for index, pt in enumerate(shape.parts()):
            print('Part {}: {}'.format(index, pt))
            pt_pos = (pt.x, pt.y)
            cv2.circle(img, pt_pos, 2, (255, 0, 0), 1)
            
        cv2.namedWindow(f, cv2.WINDOW_AUTOSIZE)
        cv2.imshow(f, img)

cv2.waitKey(0)
cv2.destroyAllWindows()
