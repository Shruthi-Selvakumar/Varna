import cv2
import numpy as np
from PIL import Image
import webcolors
import pyttsx3
from matplotlib import pyplot as plt
def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        colourname = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        colourname = closest_colour(requested_colour)
    return colourname
   
def PIX(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        r, g, b = rgbimg.getpixel((x,y))
        txt = str(r)+","+str(g)+","+str(b)
        requested_colour = (int(r), int(g), int(b))
        colourname = get_colour_name(requested_colour)
        print ("Colour Name = "+colourname)
        bg = np.zeros((200, 400, 3), np.uint8)
        bg[:,0:400] = (b,g,r)
        font = cv2.FONT_ITALIC
        cv2.putText(bg, txt, (10,100), font, 1, (255,255,255), 2, cv2.LINE_AA)
        cv2.putText(bg, str(colourname),(10,150),font, 1, (255,255,255), 2, cv2.LINE_AA)
        cv2.imshow('rgb',bg)
        test=colourname 
        engine = pyttsx3.init()
        en_voice_id = "com.apple.speech.synthesis.voice.Alex"
        engine.setProperty('voice', en_voice_id)
        engine.say(test)
        engine.runAndWait()

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    flipped = cv2.flip(frame, 1)
    cv2.imshow('vid', flipped)
    if cv2.waitKey(1) & 0xFF == ord('c'): #'c' to capture the 
        cv2.imwrite('1.png',flipped)
        imge = Image.open('1.png')
        rgbimg = imge.convert('RGB')
        cv2.imshow('pic',flipped)
        cv2.setMouseCallback('pic', PIX) #function that captures the current pixel and displays on a window
        
    elif cv2.waitKey(1) & 0xFF == ord(' '): #space to quit   
        break
cap.release()
cv2.destroyAllWindows()



