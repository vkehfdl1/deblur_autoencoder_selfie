import glob
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import cv2
import albumentations as A
import os
import shutil
from utils import *
import deblur.model as model

class process():
    def __init__(self, N):
        try:
            os.makedirs('./start_to_end_data/'+str(N))
        except:
            pass
        shutil.copy('./cut_img/cut_img'+str(N)+'.jpg', './start_to_end_data/'+str(N)+'/')
        self.original_filepath = './start_to_end_data/'+str(N)+'/cut_img'+str(N)+'.jpg'
        self.N = N
    
    def _transform_data(self):
        transform = A.Compose([
            A.MotionBlur(p=1,blur_limit=(25,30)),
        ])
        image = cv2.imread(self.original_filepath)
        self.original_image = image
        try:
            os.makedirs('./start_to_end_data/'+str(self.N)+'/blurred')
        except:
            pass
        transformed = transform(image=image)
        transformed_image = transformed["image"]
        self.transformed_image = transformed_image
        cv2.imwrite('./start_to_end_data/'+str(self.N)+'/blurred/'+str(self.N)+'.jpg',transformed_image)
        
    def _test_data(self):
        deblur = model.DEBLUR(input_path='./start_to_end_data/'+str(self.N)+'/blurred')
        deblur.build('checkpoint/alldata')
        deblur.test()
    
    def fit(self):
        self._transform_data()
        self._test_data()
        print("process completed")
        
    def visualize(self):
        fig = plt.figure(figsize=(30,10))
        img0 = self.original_image
        img1 = self.transformed_image
        img2 = cv2.imread('./start_to_end_data/'+str(self.N)+'/blurred_res/'+str(self.N)+'.jpg')
        img_list = [img0, img1, img2]
        label = ["Original", "Blurred", "Deblur"]
        for i, img in enumerate(img_list):
            ax = fig.add_subplot(1,3,i+1)
            ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            ax.set_xlabel(label[i])
            ax.xaxis.label.set_color('white') #label 이름이 안 보이면  dark mode에서 작업하세요. 
            ax.set_xticks([]), ax.set_yticks([])
        