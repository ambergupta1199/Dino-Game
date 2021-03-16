import pyautogui
from PIL import Image,ImageGrab 
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    for i in range(350,400):
        for j in range(275,448):
            if data[i, j]<100:
                hit('down')

                return 


    for i in range(400,495):
        for j in range(448,525):
            if data[i, j]<100:
                hit('up')
                return 
    return 


    
    
if __name__ == "__main__":
    print("Game is going to Start")
    time.sleep(3)
    hit('up')

    image=ImageGrab.grab().convert('L')
    data=image.load()
     #BIRD
    for i in range(350,400):
        for j in range(275,448):
         data[i,j]=171 
#CACTUS
    for i in range(400,495):
        for j in range(448,525):
         data[i,j]=0    
    image.show() 

    #RECTANGLE FOR CACTUS      
    
    # while True:
    #      image=ImageGrab.grab().convert('L')
    #      data=image.load()
    #      isCollide(data)
             
            

#C360,405
#B330,380