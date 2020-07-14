import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def takeSS():
    image = ImageGrab.grab().convert('L')
    return image

def isCollide(data):
    if data[100, 100]>150:                                     
        for  i in range(430, 470):                       # You have to make changes here accordingly for proper functioning of this bot
            for j in range(630, 670):                    # You have to make changes here accordingly for proper functioning of this bot
                if data[i, j] < 100:
                    hit('up')
                    pyautogui.keyUp('up')
                    return 
        for  i in range(430, 470):                       # You have to make changes here accordingly for proper functioning of this bot
            for j in range(380, 580):                    # You have to make changes here accordingly for proper functioning of this bot
                if data[i, j] < 100:
                    hit('down')
                    time.sleep(0.10)
                    pyautogui.keyUp('down')
                    return
    elif data[100, 100] < 100: 
        for  i in range(430, 470):                        # You have to make changes here accordingly for proper functioning of this bot
            for j in range(630, 670):                     # You have to make changes here accordingly for proper functioning of this bot
                if data[i, j] > 150:
                    hit('up')
                    pyautogui.keyUp('up')
                    return 
        for  i in range(430, 470):
            for j in range(380, 580):                     # You have to make changes here accordingly for proper functioning of this bot
                if data[i, j] > 150:                      # You have to make changes here accordingly for proper functioning of this bot
                    hit('down')
                    time.sleep(0.10)
                    pyautogui.keyUp('down')
                    return
            
    return 


if __name__ == "__main__":
    print("Starting game in 3 sec")
    time.sleep(3)
    while True:
        image = takeSS()
        data = image.load()
        
        isCollide(data)

##        for  i in range(325, 400):                              #########################################
##            for j in range(600, 665):                           # In this commented region you can test #
##                data[i, j] = 0                                  # your hit box.You can check output.png #
##                                                                # for output image of hitbox.           #
##        for  i in range(400, 500):                              #########################################
##            for j in range(380, 475):
##                data[i, j] = 71
##                    
##        image.show()
##        break
