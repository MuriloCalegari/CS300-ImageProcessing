import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

zeros = np.zeros(((5,5)))

def blackout(width, height):
    return np.zeros(((height,width)))

def see_points(width, height, points):
    pixels = np.zeros(((height,width)))
    for point in points:
        pixels[point[0], point[1]] = 1
        
    return pixels

def see_quadrant(image_name, quadrant):
    img = mpimg.imread(image_name)
    height = img.shape[0]
    width = img.shape[1]
    
    res = 0
    
    #print(img)
    
    #print("shape: ", img.shape)
    
    match quadrant:
        case "top_left":
            res = img[math.floor(height / 4), math.floor(width / 4)]
        case "top_right":
            res = img[math.floor(height / 4), math.floor(width * 3/4)]
        case "bottom_left":
            res = img[math.floor(height * 3/4), math.floor(width / 4)]
        case "bottom_right":
            res = img[math.floor(height * 3/4), math.floor(width * 3/4)]
            
    return round(res * 255)

def see_lines(width, height, lines):
    img = np.zeros(((height,width)))
    
    for line in lines:
        if(line[0] == line[2]): # horizontal lines
            img[line[0]][line[1]:line[3]] = 1
        else: # vertical lines
            img[line[0]:line[2], line[1]] = 1

    return img

def see_quadrant_complete(image_name, quadrant):
    img_grey = mpimg.imread(image_name)
    height = img_grey.shape[0]
    width = img_grey.shape[1]
    
    #print(img_grey)
    
    img = np.zeros((height, width, 3))
    
    point = 0
    
    match quadrant:
        case "top_left":
            point = (math.floor(height / 4), math.floor(width / 4))
        case "top_right":
            point = (math.floor(height / 4), math.floor(width * 3/4))
        case "bottom_left":
            point = (math.floor(height * 3/4), math.floor(width / 4))
        case "bottom_right":
            point = (math.floor(height * 3/4), math.floor(width * 3/4))

    img[:, :, 0] = img_grey[:, :]
    img[:, :, 1] = img_grey[:, :]
    img[:, :, 2] = img_grey[:, :]
     
    #draw axis
    img[0:height, math.floor(width / 2), 1] = 0 # vertical
    img[0:height, math.floor(width / 2), 2] = 0 # vertical
    img[math.floor(height / 2), 0:width, 1] = 0 # horizontal
    img[math.floor(height / 2), 0:width, 2] = 0 # horizontal
    
    img[0:height, math.floor(width / 2), 0] = 1 # vertical
    img[math.floor(height / 2), 0:width, 0] = 1 # horizontal
    
    #draw square
    img[(point[0] - 3):(point[0] + 4),  (point[1] - 3):(point[1] + 4) , 0] = 0
    img[(point[0] - 3):(point[0] + 4),  (point[1] - 3):(point[1] + 4) , 1] = 0
    img[(point[0] - 3):(point[0] + 4),  (point[1] - 3):(point[1] + 4) , 2] = 1
    
    #print(img)
    #plt.imshow(img)
    #plt.show()
    return img

    
#see_quadrant_complete("an_image.png", "top_left")
#see_quadrant_complet("an_image.png", "top_right")
#see_quadrant_complet("an_image.png", "bottom_left")
#see_quadrant_complet("an_image.png", "bottom_right")

#print(see_lines(4, 4, [(0 , 0 , 2, 0)]))