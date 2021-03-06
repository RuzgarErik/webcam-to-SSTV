import cv2
from cv2 import VideoCapture, imshow, imwrite, putText, waitKey,destroyWindow
import os
import time
from cv2 import waitKeyEx
import numpy as np
import cvzone
from datetime import datetime
import sys
from pydub import AudioSegment
from pydub.playback import play


overlay_image = cv2.imread('assets/logo.png', cv2.IMREAD_UNCHANGED) 

overlay_image = cv2.resize(overlay_image, (0, 0), None, 0.4, 0.4)


a = r'''
                                                                        __                       ______    ______   ________  __     __ 
                                                                       /  |                     /      \  /      \ /        |/  |   /  |
  _______   ______   _____  ____    ______    ______   ______         _$$ |_     ______        /$$$$$$  |/$$$$$$  |$$$$$$$$/ $$ |   $$ |
 /       | /      \ /     \/    \  /      \  /      \ /      \       / $$   |   /      \       $$ \__$$/ $$ \__$$/    $$ |   $$ |   $$ |
/$$$$$$$/  $$$$$$  |$$$$$$ $$$$  |/$$$$$$  |/$$$$$$  |$$$$$$  |      $$$$$$/   /$$$$$$  |      $$      \ $$      \    $$ |   $$  \ /$$/ 
$$ |       /    $$ |$$ | $$ | $$ |$$    $$ |$$ |  $$/ /    $$ |        $$ | __ $$ |  $$ |       $$$$$$  | $$$$$$  |   $$ |    $$  /$$/  
$$ \_____ /$$$$$$$ |$$ | $$ | $$ |$$$$$$$$/ $$ |     /$$$$$$$ |        $$ |/  |$$ \__$$ |      /  \__$$ |/  \__$$ |   $$ |     $$ $$/   
$$       |$$    $$ |$$ | $$ | $$ |$$       |$$ |     $$    $$ |        $$  $$/ $$    $$/       $$    $$/ $$    $$/    $$ |      $$$/    
 $$$$$$$/  $$$$$$$/ $$/  $$/  $$/  $$$$$$$/ $$/       $$$$$$$/          $$$$/   $$$$$$/         $$$$$$/   $$$$$$/     $$/        $/     
                                                                                                                                        

    '''


def captureimage():
    try:
        cam_port = 0
        cam = VideoCapture(cam_port)
        result, image = cam.read()

        if result:
            dimensions = image.shape
            height = image.shape[0]
            width = image.shape[1]
            print(height,width)

            hf, wf, cf = overlay_image.shape
            hb, wb, cb = image.shape
            imgResult = cvzone.overlayPNG(image, overlay_image, [wb-wf,0 ])
            date = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
            filename = date + ".png"
            cv2.putText(img=imgResult, text='Sivas Fen Lisesi 2022 Bilim Fuari', org=(5, height-10), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 0, 255),thickness=2)
            cv2.putText(img=imgResult, text='TA7AGK', org=(5,30), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 0, 255),thickness=2)
            
            imshow("??ekilen Foto??raf", imgResult)
            imwrite(filename, imgResult)
            waitKey(0)
            print("SSTV Sinyaline D??n????t??r??l??yor")
            convertToSSTV(filename,date)
        else:
            print("Foto??raf Kaydetme Hatas??")
    except KeyboardInterrupt:
        print("Ba??a d??n??l??yor")




def convertToSSTV(imgpath,imgname):
    os.system("python -m pysstv {imgpath} {imgname}.wav --resize --keep-aspect-ratio --mode PD120".format(imgpath=imgpath,imgname=imgname))
    if os.path.exists(imgname+".wav"):
        print("SSTV Sinyali Ba??ar??yla Olu??turuldu")
        playSSTV(imgname)
    else:
        print("SSTV Sinyali Olu??turulamad??")



def playSSTV(filename):
    while True:
        path = filename + ".wav"
        i = input("G??nder : 1 | ??ptal Et: 2   : ")
        if i == "1":
            song = AudioSegment.from_wav("{a}".format(a=path))
            while True:
                try:
                    play(song)
                except KeyboardInterrupt:
                    print ("Stopping playing")
                    break #to exit out of loop, back to main program
                break
        elif i == "2":
            print("G??nderme ??ptal Edildi")
            break

        else:
            pass
            



print(a)

while 1:
    while 1:
        try:

            i = input('''
            Foto??raf ??ek: 1
            Program?? Kapat: 2

            Se??im: 
            ''')
            if i == '1':
                try: 
                    captureimage()
                except Exception as e:
                    print("B??R HATA OLU??TU")
                    print(e)
            elif i == "2":
                print("Program Kapat??l??yor")
                sys.exit()
        
        except KeyboardInterrupt:
            break
