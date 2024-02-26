import cv2
import mediapipe as mp
import os
import math
import numpy as np


def trackJoints (folderName):
    # initialize Pose estimator
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

    frameNr = 1

    right_arm_array = []


     # Create a folder specifically for the video
    try: 
        os.makedirs(os.path.join('OutputData', folderName))
    except OSError:
        print('Error: Creating directory of ' + folderName)


    while (True):
        try: 
            frame = cv2.imread('./data/' + folderName + '/frame' + str(frameNr) + '.jpg')
           
            # convert the frame to RGB format
            RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # process the RGB frame to get the result
            results = pose.process(RGB)
            #print(results.pose_landmarks)

            # draw detected skeleton on the frame
            mp_drawing.draw_landmarks(
                frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # show the final output
            #cv2.imshow('Output', frame)
            name = './OutputData/' + folderName + '/output_frame' + str(frameNr) + '.jpg'
            cv2.imwrite(name, frame)
        except:
            print('End of frames')
            break
        if cv2.waitKey(1) == ord('q'):
            break

        
        image_height, image_width, _ = frame.shape   

       

        # Calculate angles 
        if results.pose_landmarks is not None: 
            # elbow 
            e = [results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x * image_width,
                results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y * image_height]
            
            # shoulder 
            s = [results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * image_width,
                results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * image_height]
            
            # wrist 
            w = [results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x * image_width,
                results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y * image_height]
        
            arm_angle = angle(w, e, s)
        else: 
            arm_angle = 0
        #print('Angle of right arm:' + "{:.2f}".format(arm_angle) + "  (" + str(frameNr) + ")")
        
    
        right_arm_array.append(arm_angle)
        frameNr += 1

    return right_arm_array


def angle ( point1, point2, point3):

    def magnitude(vect):
            return math.sqrt(sum(x**2 for x in vect))

    def get_angle_between_vectors(unit_vector_1, unit_vector_2):	
        dot_product = np.dot(unit_vector_1, unit_vector_2)	
        if dot_product > 1:	
            dot_product = 1	
        angle = np.arccos(dot_product) / (magnitude(unit_vector_1)*magnitude(unit_vector_2))
        return angle	
        
    def make_unit_vector(point1, point2):	
        vector = [point2[0] - point1[0], point2[1] - point1[1]]	
        norm = np.linalg.norm(vector)	
        if norm == 0:	
            return None	
        return [vector[0] / norm, vector[1] / norm]        	
        
    vector1 = make_unit_vector(point1, point2)	
    vector2 = make_unit_vector(point3, point2)	
    if (vector1 is None or vector2 is None):	
        return None	
        
    angle_rad = get_angle_between_vectors(vector1, vector2)	
    angle_deg = math.degrees(angle_rad)

    return angle_deg


    











