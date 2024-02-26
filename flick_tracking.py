from align_videos import align_flick
from split_video import splitVideo
from track_joints import trackJoints
from comparator import compare_flick

import cv2

# define which video to perform analysis on 
video_ref = './Input Footage/Reference Video.avi'
folderName_ref = 'Ref Athlete'

video_athlete = './Input Footage/Athlete 3.mp4'
folderName_athlete = 'Athlete 3'

# convert video into frames
print("Splitting Videos...")
splitVideo(video_ref, folderName_ref)
splitVideo(video_athlete, folderName_athlete)
print('Video Split')

# track the joints from each image and return right arm anlge arrays
print("Applying Pose Estimation ...")
ref_angles = trackJoints( folderName_ref )
athlete_angles = trackJoints( folderName_athlete )        
print("Joints successfully tracked!")


# align videos 
print("Alinging videos")
aligned_athlete_angles = align_flick(ref_angles, athlete_angles, folderName_athlete, folderName_ref )
print("Videos Aligned Successfully")

# Compare athlete to reference video 
print("Calculating Score...")
score10, score20 = compare_flick(ref_angles, aligned_athlete_angles)

print("10 degree Score = " + str(score10))
print("20 degree Score = " + str(score20))

# Display final videos and score 
final_athlete_vid = cv2.VideoCapture('Final Videos/' + folderName_athlete + '.mp4')
final_ref_vid = cv2.VideoCapture('Final Videos/' + folderName_ref + '.mp4')

while True:

    okayAth, frameAth = final_athlete_vid.read()
    okayRef, frameRef = final_ref_vid.read()

    if final_athlete_vid:
        cv2.imshow("Athlete Final Video", frameAth)

    if final_ref_vid:
        cv2.imshow('Reference Final Video', frameRef)

    if not okayAth or not okayRef: 
        print("Cannot read the video, Exit!")
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.waitKey(1)
final_athlete_vid.release()
final_ref_vid.release()
cv2.destroyAllWindows()

