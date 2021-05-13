import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
import cv2
import sys

def visualize_many_images(filelist, rows=6,cols=6):    
    fig = plt.figure(figsize=(30,30)) # rows*cols 행렬의 i번째 subplot 생성
    rows = rows
    cols = cols
    i = 1

    for filename in filelist:
        if (i > rows*cols):
            break
        img = cv2.imread(filename)
        ax = fig.add_subplot(rows, cols, i)
        ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        ax.set_xlabel(filename.split('/')[-1])
        ax.xaxis.label.set_color('white') #label 이름이 안 보이면  dark mode에서 작업하세요. 
        ax.set_xticks([]), ax.set_yticks([])
        i += 1
    plt.show()