import os
from re import I
from tkinter import Frame
from turtle import width
import cv2
from numpy import size


images = []
path = "./PROC105-V1-actividad-alumno1-main/Images"


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)
print(size)

out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'MPEG'), 5, size)

for i in range(count -1, 0, -1):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()
print("Listo")