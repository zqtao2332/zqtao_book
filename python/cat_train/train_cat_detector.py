# -*- coding: utf-8 -*-
import os
import sys
import glob
import cv2
import dlib

# options用于设置训练的参数和模式
options = dlib.simple_object_detector_training_options()
# 因为脸是左右对称的，我们可以告诉教练训练对称的探测器。这有助于它从培训中获得最大的价值数据。
options.add_left_right_image_flips = True
#支持向量机的C参数，通常默认取为5.自己适当更改参数以达到最好的效果
options.C = 5
# 告诉代码你的计算机有多少个CPU核心用于最快的训练。线程数，你电脑有4核的话就填4
options.num_threads = 4
options.be_verbose = True


# 获取路径
current_path = os.getcwd()
train_folder = current_path + '/train/'
test_folder = current_path + '/test/'
training_xml_path = os.path.join(train_folder, "training.xml")
testing_xml_path = os.path.join(test_folder, "testing.xml")


#执行实际的训练。它将把最后的探测器保存到 detector.svm
dlib.train_simple_object_detector(training_xml_path, "detector.svm", options)



print("")  # Print blank line to create gap from previous output
print("Training accuracy: {}".format(
    dlib.test_simple_object_detector(training_xml_path, "detector.svm")))
# 为了得到一个想法，如果它真的工作，而不过度拟合，需要在没有训练过的图像上运行它
print("Testing accuracy: {}".format(
    dlib.test_simple_object_detector(testing_xml_path, "detector.svm")))





# 加载训练完毕的检测器
detector = dlib.simple_object_detector("detector.svm")


# 测试图片存放
test_folder = current_path + '/testimg/'

for f in glob.glob(test_folder+'*.jpg'):
    print("Processing file: {}".format(f))
    img = cv2.imread(f, cv2.IMREAD_COLOR)
    b, g, r = cv2.split(img)
    img2 = cv2.merge([r, g, b])
    dets = detector(img2)
    print("Number of faces detected: {}".format(len(dets)))
    for index, face in enumerate(dets):
        print('face {}; left {}; top {}; right {}; bottom {}'.format(index, face.left(), face.top(), face.right(), face.bottom()))

        left = face.left()
        top = face.top()
        right = face.right()
        bottom = face.bottom()
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 3)
        cv2.namedWindow(f, cv2.WINDOW_AUTOSIZE)
        cv2.imshow(f, img)

k = cv2.waitKey(0)
cv2.destroyAllWindows()
