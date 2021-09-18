
#guess what we're gonna use to take pictures?
#opencv!
import cv2
from datetime import datetime
import os
def take_and_save_picture():
    cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop)
    ret,frame = cap.read() # return a single frame in variable `frame`
    proper_date = str(datetime.now()).replace(".", "-").replace(":", "-")
    cv2.imwrite(os.path.join("images", proper_date)+".png", frame)


if __name__ == '__main__':
    take_and_save_picture()