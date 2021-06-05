import glob
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import cv2
import albumentations as A
import os

class prepare:
    def __init__(self, filepath, N):
        self.filepath = filepath
        self.img_name = self.filepath.split('/')[-1][:-4]
        self.N = N
    
    def blur_image(self):
        transform = A.Compose([
            A.Blur(blur_limit=14, p=1),
            A.GaussianBlur(blur_limit=(5,11),p=1),
            A.MedianBlur(blur_limit=11,p=1),
            A.MotionBlur(p=0.1),
        ])
        image = cv2.imread(self.filepath)
        os.makedirs('./X/'+self.img_name)
        for i in range (self.N):
            transformed = transform(image=image)
            transformed_image = transformed["image"]
            cv2.imwrite('./X/'+self.img_name+'/'+str(i)+'.jpg',transformed_image)
        print("Blur transform completed")
    
    def load_y(self):
        image = cv2.imread(self.filepath)
        data = np.expand_dims(image, axis=0)
        data_ = data
        for i in range(1, self.N):
            data = np.concatenate((data,data_), axis=0)
        return data
    
    def load_x(self):
        image = cv2.imread('./X/'+self.img_name+'/0.jpg')
        data = np.expand_dims(image, axis=0)
        for i in range(1, self.N):
            image = cv2.imread('./X/'+self.img_name+'/'+str(i)+'.jpg')
            data_ = np.expand_dims(image, axis=0)
            data = np.concatenate((data,data_), axis=0)
        return data
    
    def split(self, x, y, split_size=0.2):
        x_train = x[int(self.N*split_size):]
        y_train = y[int(self.N*split_size):]
        x_validation = x[:int(self.N*split_size)]
        y_validation = y[:int(self.N*split_size)]
        return x_train, y_train, x_validation, y_validation
    
    