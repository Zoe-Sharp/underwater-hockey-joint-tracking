# Underwater Hockey Flick Tracking Analysis

This is a program that analyses a video of an athlete performing a 'flick' and compares it to a reference video. 

## Requirements
The following features are required for the input video for a more accurate analysis. 
* Video angle must be taken from a birds eye view
* Athlete must be playing with their right hand 
* Video must be at 60 fps

# Installations 
The following libraries are needed to run this program: 
- [ ] numpy
- [ ] cv2
- [ ] os
- [ ] mediapipe
- [ ] shutil

To do this run the following commands in terminal (for Linux and Mac)
```
npm install numpy
npm install opencv
npm install mediapipe
npm install shutil
npm install os
```
## Adding data
Add your own .mp4 or .avi video files into the 'Input Footage' folder. <br>
There is already some sample data there you can use. 

## Run Locally
Go to project directory.<br>
Install all required libararys.<br>
In `flick_tracking.py` update lines 12 and 13 fro your desired input videos. <br>
Run the following command in terminal:<br>
`python3 flick_tracking.py`<br>

## Output 
You should expect to see two videos shown that have been aligned. Two scores based on the percentage of frames that the athlete is within a 10 degree and 20 degree tolerance will be shown in the terminal. 