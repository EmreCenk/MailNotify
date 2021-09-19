
#guess what we're gonna use to take pictures?
#opencv!
import cv2
from datetime import datetime
import os
from sending_images import send_image 
def take_and_save_picture():
    cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop)
    ret,frame = cap.read() # return a single frame in variable `frame`
    proper_date = str(datetime.now()).replace(".", "-").replace(":", "-")
    path_to_save = os.path.join("images", proper_date)+".png"
    cv2.imwrite(path_to_save, frame)
    return path_to_save

def take_and_upload():
    """Takes a picture, then sends to server"""
    try:
        path = take_and_save_picture()
    except:
        #A webcam doesn't exist
        print("there was an issue taking a picture. This is probably because you don't have a webcam. A stock photo will be used instead.")
        path = "images\pcletter.png"

    send_image(path)
    
if __name__ == '__main__':
    take_and_upload()