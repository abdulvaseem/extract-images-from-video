"""pip install cv2"-windows command
sudo pip install cv2 - linux command"""

import cv2

vidcap = cv2.VideoCapture('/content/query /pop.mp4')
count = 0
success = True
fps = int(vidcap.get(cv2.CAP_PROP_FPS))

while success:
    success,image = vidcap.read()
    #print('read a new frame:',success)
    if count%(10*fps) == 0 :
         cv2.imwrite('/content/processing/frame%d.jpg'%count,image)
         #print('successfully written 10th frame')
    count+=1
