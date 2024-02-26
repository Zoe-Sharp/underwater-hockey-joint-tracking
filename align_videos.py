# comparator file to compare two videos 
import numpy as np
import cv2
import os
import re

def calculate_error(ref_array, athlete_array):
    # Function to calculate the error of angles between videos
    n = min(len(ref_array), len(athlete_array))
    sum = 0

    for i in range(n):
        sum += abs(ref_array[i]-athlete_array[i])
    
    error = sum/n
    return error

def calculate_score(ref_array, athlete_array, tolerance):
    # Function to calculate the score of the athlete
    min_length = min(len(ref_array), len(athlete_array))
    ref_array  = ref_array[:min_length]
    athlete_array  = athlete_array[:min_length]

    angle_diff = []

    for i in range(min_length):
        if (ref_array[i] != 0 and athlete_array[i] != 0):
            element_diff = np.abs(ref_array[i] - athlete_array[i])
            angle_diff.append(element_diff)

    within_tolerance = np.less_equal(angle_diff, tolerance)

    score = np.mean(within_tolerance) * 100
    return score


def left_shift_theorem (ref_angles, athlete_angles):
    # left shift theorem function to align videos
    n = 30
    i = 0
    error_array = []
    test_athlete_array = athlete_angles

    # for the first 30 frames calculate the error and then shift the athlete video one to the left 
    while i < n:
        error = calculate_error(ref_angles,  test_athlete_array)
        error_array.append(error)
        test_athlete_array = test_athlete_array[1:]
        i += 1

    # calculte and return the shift number that gave the lowest error
    shift_number = error_array.index(min(error_array))
    return shift_number


def save_aligned_frames_videos (shift_number, folderName_athlete ):

     # Create a folder specifically for the video
    try: 
        os.makedirs(os.path.join('Aligned Athlete Data', folderName_athlete))
    except OSError:
        print('Error: Creating directory of ' + folderName_athlete)


    newFrameNr = 1
    shiftCount = shift_number
    
    # for each frame of athlete resave it from the start of the realigned shift number
    while (True):
        frame = cv2.imread('./OutputData/' + folderName_athlete + '/output_frame' + str(shiftCount) + '.jpg')

        if frame is not None:
            name = './Aligned Athlete Data/' + folderName_athlete + '/output_frame' + str(newFrameNr) + '.jpg'
            cv2.imwrite(name, frame)
            newFrameNr += 1
            shiftCount += 1
        else: 
            break

def save_final_videos (image_folder, video_name):
    # save videos
    video_path  = 'Final Videos/' + video_name

    pre_imgs = os.listdir(image_folder)
    img = []

    for i in pre_imgs:
        i = image_folder+i
        img.append(i)

    img.sort(key=lambda x: int(re.findall(r'\d+', os.path.basename(x))[0]))

    cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    frame = cv2.imread(img[0])
    size = list(frame.shape)
    del size[2]
    size.reverse()
    video = cv2.VideoWriter(video_path, cv2_fourcc, 24, size ) # output video name, fourcc, fps, size

    for i in range(len(img)):
        video.write(cv2.imread(img[i]))

    video.release()

def align_flick (ref_angles, athlete_angles, folderName_athlete, folderName_ref): 
    #use the left shift theorm to caluculte the smallest error 
    shift_number = left_shift_theorem (ref_angles, athlete_angles)
    
    save_aligned_frames_videos(shift_number, folderName_athlete)

    # recalculate athlete angles 
    aligned_athlete_angles = athlete_angles[shift_number:]


    image_folder_athlete = 'Aligned Athlete Data/' + folderName_athlete +'/'
    video_name_athlete = folderName_athlete + '.mp4'

    # save frames as videos
    save_final_videos(image_folder_athlete, video_name_athlete)

    image_folder_ref = 'OutputData/' + folderName_ref +'/'
    video_name_ref = folderName_ref + '.mp4'
    # save frames as videos
    save_final_videos(image_folder_ref, video_name_ref)

    return aligned_athlete_angles




    

