from os import access
import cv2
import random
import dropbox
import time
from datetime import datetime

start_time = time.time()

def take_photo():

    #definig the videocapture object
    videoCaptureObject = cv2.VideoCapture(0)
    
    # condition for while loop
    result = True

    while(result):

        #reading the image
        ret, frame = videoCaptureObject.read()

        # getting the current time
        now = time.strftime("%Y%m%d-%H%M%S")

        #creating the image name
        img_name = f'Image{now}.png'

        #Saving the image
        cv2.imwrite(img_name, frame)

        #Setting the start time to initial value
        start_time = time.time()

        #Setting the result to false
        result = False
         
        #getting the image name
        return(img_name)
    
    videoCaptureObject.release()

    cv2.destroyAllWindows()
     

def upload_file(img_name):

    access_token = 'sl.BD7z1uQZgiaSWujkJJ38MsLrCfqS1ZdAuWUQWN9tq-RET_HZK_FzVsE8TQPyQlag2EpG1jz_iCXEVMUIFAj8rLT286ZIK9s9tRpS-G1ZDcmywwVktvtVZtBGuBhJ1dfYqrmB2Ao'
    file = img_name
    file_from = img_name
    file_to = "/Python/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if((time.time() - start_time) >= 4):
            name = take_photo()
            upload_file(name)

main()