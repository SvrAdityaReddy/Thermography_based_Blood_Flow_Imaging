import cv2
import os
import numpy as np

cap=cv2.VideoCapture('ftna.mp4')
count=0

while(cap.isOpened()):
    ret,frame=cap.read()
    if(ret==True):
        cv2.imwrite("frame_"+str(count)+".jpg",frame)
        count=count+1
    else:
        break

cap.release()
cv2.destroyAllWindows()

np_img=[]

for i in range(0,640):
    np_img.append([])
    for j in range(0,480):
        np_img[i].append([])

for i in range(0,count):
    img=cv2.imread("frame_"+str(i)+".jpg")
    for j in range(0,640):
        for k in range(0,480):
            np_img[j][k].append(img[j][k])

np_img=np.array(np_img, dtype=complex)

# print(np_img.shape)

z=0.002
k=0.33
c=3780
p=1057
X=k/(c*p)
f=0.01

phase=np.exp(z*np.sqrt(np.pi*f/X)*(1+1j))

for i in range(0,640):
    for j in range(0,480):
        np_img[i][j]=np.fft.fft(np_img[i][j])*phase

for i in range(0,640):
    for j in range(0,480):
        np_img[i][j]=np.fft.ifft(np_img[i][j])

print(np_img)

img=[]
frame_array=[]

for i in range(0,count):
    for j in range(0,640):
        img.append([])
        for k in range(0,480):
            img[j].append(np_img[j][k][i])
    img=np.uint8(img)
    print(img)
    cv2.imwrite("b_frame_"+str(i)+".jpg",img)
    frame_array.append(img)
    img=[]

fps=3
out=cv2.VideoWriter("b_ft.avi",cv2.VideoWriter_fourcc(*'DIVX'),fps,(480,640))

for i in range(len(frame_array)):
    out.write(frame_array[i])

out.release()