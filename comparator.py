# comparator file to compare two videos 
import numpy as np
from align_videos import calculate_error
from align_videos import calculate_score

def compare_flick (ref_angles, athlete_angles):
    # funtion to compare teh angles of the two athletes
    
    angle_diff = []
    # check which array of angles is longer 
    if len(ref_angles) < len(athlete_angles):
        for i in range(len(ref_angles)):
            # add to the angle_diff array the angle difference between the two frames 
            angle_diff.append(athlete_angles[i]-ref_angles[i])
    else:
        for i in range(len(athlete_angles)):
            # add to the angle_diff array the angle difference between the two frames 
            angle_diff.append(athlete_angles[i]-ref_angles[i])
    
    score10 = calculate_score(ref_angles,  athlete_angles, 10)
    score20 = calculate_score(ref_angles,  athlete_angles, 20)

    return score10, score20
    

 


