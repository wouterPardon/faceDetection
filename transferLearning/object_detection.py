from vision_display import VisionDisplay
import cv2
import sys
import os  

if __name__ == "__main__":

    if(len(sys.argv) <= 1):
        raise Exception('No image folder was given')

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        raise Exception('Must be a folder')
    
    path_images = directory
    path_yolo = './'
    vision = VisionDisplay(path_yolo)

    for filename in os.listdir(directory):
        if filename.endswith(".png") or filename.endswith(".jpg"): 
            #print(os.path.join(directory, filename))
            img = cv2.imread(os.path.join(directory, filename),1)
            cv2.imshow("Image", img)
            cv2.waitKey(0)
            vision.detect_objects(img, str(filename).split('.')[0] + '.txt')
        else:
            continue


