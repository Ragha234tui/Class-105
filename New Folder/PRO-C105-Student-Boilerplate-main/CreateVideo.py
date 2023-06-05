import os
import cv2


path = "D:/USER/Desktop/Python Programm/Class 105/OPK"

OPK = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        OPK.append(file_name)
        
print(len(OPK))
count = len(OPK)

frame=cv2.imread(OPK[0])
height,width,channels=frame.shape 
size=(width,height)
print(size)

out=cv2.VideoWriter("FriendShip Day.mp4",cv2.VideoWriter_fourcc(*"DIVX"),5,size)
for i in range(0,count -1):
    frame=cv2.imread(OPK[i])
    out.write(frame)
out.release()
print('DONE')    
 