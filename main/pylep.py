import sys
import numpy as np
import cv2
from pylepton import Lepton

z=0.002
k=0.33
c=3780
p=1057
X=k/(c*p)
f=0.01

phase=np.exp(z*np.sqrt(np.pi*f/X)*(1+1j))

def capture_video(phase, device = "/dev/spidev0.0"):
	np.set_printoptions(threshold=np.nan)
	print(phase)
	with Lepton(device) as l:
		m=1
		while(m>0):
			m=m-1
			image_list=[]
			for i in range(0,100):
				a,_ = l.capture()
				a=a/100.0
				image_list.append(a)
				cv2.imwrite("frame_"+str(i)+".jpg",a)

			np_img=np.zeros((60,80,100),dtype=complex)

			for i in range(0,100):
				for j in range(0,60):
					for k in range(0,80):
						np_img[j][k][i]=image_list[i][j][k]

			for i in range(0,60):
				for j in range(0,80):
					np_img[i][j]=np.fft.fft(np_img[i][j])*phase

			for i in range(0,60):
				for j in range(0,80):
					np_img[i][j]=np.fft.ifft(np_img[i][j])

			frame_array=[]

			for i in range(0,100):
				img=np.zeros((60,80),dtype=complex)
				print(img.shape)
				for j in range(0,60):
					for k in range(0,80):
						img[j][k]=np_img[j][k][i]
				# img=np.uint8(img)
				# img=cv2.applyColorMap(img,cv2.COLORMAP_HSV)
				# img=cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
				# img=cv2.cvtColor(img, cv2.COLOR_BGR2Luv)
				# print(img)
				# img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
				# cv2.imwrite(input_file_name+"_b_frame_"+str(i)+".jpg",img)
				frame_array.append(img)
			print(frame_array)
		
			
capture_video(phase)
