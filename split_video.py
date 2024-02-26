import cv2
import numpy as np
import os
import shutil

def splitVideo( video, folderName ):
    capture = cv2.VideoCapture(video) 
    
    # Delete contents of folder 
    try:
        shutil.rmtree(os.path.join('data', folderName))
    except:
        print("Error: Deleting contents of data folder")
    try:
        shutil.rmtree(os.path.join('Output Images', folderName))
    except:
        print("Error: Deleting contents of Output folder")
    try:
        shutil.rmtree(os.path.join('Aligned Athlete Data', folderName))
    except:
        print("Error: Deleting contents of athlete data folder")
    # Create a  folder for the data
    try: 
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        print('Error: Creating directory of data')

    # Create a folder specifically for the video
    try: 
        os.makedirs(os.path.join('data', folderName))
    except OSError:
        print('Error: Creating directory of ' + folderName)

     # Check if camera opened successfully
    if (capture.isOpened()== False): 
      print("Error opening video stream or file")


    currentFrame = 0
    frameCount = 0
    frameNr = 1


    while(True):
        # process frames
        ret, frame = capture.read() 
        
        if ret:
            if  frameCount == 1:
                name = './data/' + folderName + '/frame' + str(frameNr) + '.jpg'
                #print('Creating...' + name)
                cv2.imwrite(name,frame)
                #print(successful)
                frameCount = 0
                frameNr += 1
            else: 
                frameCount += 1 
        else: 
            break

        currentFrame += 1

    capture.release()


