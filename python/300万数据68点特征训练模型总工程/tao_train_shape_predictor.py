# coding: utf-8
# 
#   This example program shows how to use dlib's implementation of the paper:
#   One Millisecond Face Alignment with an Ensemble of Regression Trees by
#   Vahid Kazemi and Josephine Sullivan, CVPR 2014

import os
import cv2
import dlib
import glob

current_path = os.getcwd()

# 训练部分
# 参数设置
options = dlib.shape_predictor_training_options()
options.oversampling_amount = 300
options.nu = 0.05
options.tree_depth = 2
options.be_verbose = True

# 导入打好了标签的xml文件
training_xml_path = os.path.join(current_path, "training_with_face_landmarks.xml")
# 进行训练，训练好的模型将保存为predictor.dat
dlib.train_shape_predictor(training_xml_path, "predictor.dat", options)
# 打印在训练集中的准确率
print("\nTraining accuracy: {}".format(
    dlib.test_shape_predictor(training_xml_path, "predictor.dat")))

# 导入测试集的xml文件
testing_xml_path = os.path.join(current_path, "testing_with_face_landmarks.xml")
# 打印在测试集中的准确率
print("Testing accuracy: {}".format(
    dlib.test_shape_predictor(testing_xml_path, "predictor.dat")))
